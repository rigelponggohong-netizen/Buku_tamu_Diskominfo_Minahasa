import cv2
import numpy as np
from PIL import Image
import pytesseract
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Tuple, List, Dict

def _pil_to_cv(image: Image.Image) -> np.ndarray:
    arr = np.array(image)
    if len(arr.shape) == 3 and arr.shape[2] == 3:
        # PIL RGB -> OpenCV BGR
        return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    return arr

def _deskew(gray: np.ndarray) -> np.ndarray:
    # Estimate skew using moments of edges / non-zero pixels
    coords = np.column_stack(np.where(gray > 0))
    if coords.shape[0] < 10:
        return gray
    rect = cv2.minAreaRect(coords)
    angle = rect[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = gray.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def _resize_for_dpi(img: np.ndarray, target_width=1600) -> np.ndarray:
    h, w = img.shape[:2]
    if w >= target_width:
        return img
    scale = target_width / float(w)
    new_size = (int(w * scale), int(h * scale))
    return cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)

def _enhance_contrast(gray: np.ndarray) -> np.ndarray:
    if len(gray.shape) == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(gray)

def _binarize(gray: np.ndarray) -> np.ndarray:
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th

def _sharpen(img: np.ndarray) -> np.ndarray:
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

def _preprocess_variants(image: Image.Image) -> List[Tuple[str, Image.Image]]:
    """Create a small set of preprocessed image variants optimized for OCR."""
    bgr = _pil_to_cv(image)
    variants = []

    # Convert to gray
    if len(bgr.shape) == 3:
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    else:
        gray = bgr.copy()

    # Resize for small images
    gray_resized = _resize_for_dpi(gray)
    variants.append(('gray_resized', Image.fromarray(gray_resized)))

    # Contrast enhanced
    enhanced = _enhance_contrast(gray_resized)
    variants.append(('enhanced_clahe', Image.fromarray(enhanced)))

    # Binarized
    bin_img = _binarize(enhanced)
    variants.append(('binarized', Image.fromarray(bin_img)))

    # Deskewed + enhanced
    try:
        deskewed = _deskew(enhanced)
        variants.append(('deskewed', Image.fromarray(deskewed)))
        variants.append(('deskewed_binarized', Image.fromarray(_binarize(deskewed))))
    except Exception:
        pass

    # Sharpened color for photos
    try:
        color_sharp = _sharpen(bgr)
        variants.append(('color_sharp', Image.fromarray(cv2.cvtColor(color_sharp, cv2.COLOR_BGR2RGB))))
    except Exception:
        pass

    # Keep original as last resort
    variants.append(('original', image))

    # Deduplicate by mode
    seen = set()
    dedup = []
    for name, img in variants:
        if name in seen:
            continue
        seen.add(name)
        dedup.append((name, img))

    return dedup

def _run_tesseract(pil_img: Image.Image, lang: str = 'ind+eng', psm: int = 6, oem: int = 1, whitelist: str = None) -> Dict:
    conf = f'--oem {oem} --psm {psm}'
    if whitelist:
        conf += f" -c tessedit_char_whitelist={whitelist}"
    # Use image_to_data to get confidences
    try:
        data = pytesseract.image_to_data(pil_img, lang=lang, config=conf, output_type=pytesseract.Output.DICT)
    except Exception as e:
        # In case tesseract fails for this variant, return empty
        return {'text': '', 'conf_avg': 0.0, 'raw': None, 'error': str(e)}

    texts = []
    confs = []
    n_boxes = len(data.get('text', []))
    for i in range(n_boxes):
        txt = (data['text'][i] or '').strip()
        if txt:
            try:
                conf = float(data['conf'][i])
            except Exception:
                conf = -1.0
            texts.append(txt)
            confs.append(conf)

    combined = '\n'.join(texts)
    avg_conf = float(sum([c for c in confs if c >= 0]) / max(1, sum(1 for c in confs if c >= 0))) if confs else 0.0
    return {'text': combined, 'conf_avg': avg_conf, 'raw': data, 'error': None}

def preprocess_and_ocr(image: Image.Image, lang: str = 'ind+eng', psm: int = 6, oem: int = 1, max_workers: int = 2) -> Tuple[str, Dict]:
    """Create variants, run OCR (in parallel up to max_workers), and merge best results.

    Returns (combined_text, metadata)
    """
    variants = _preprocess_variants(image)

    # Limit workers
    max_workers = max(1, min(max_workers, len(variants)))

    results = []
    metadata = {'variants': []}

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(_run_tesseract, img, lang, psm, oem): name for name, img in variants}
        for fut in as_completed(futures):
            name = futures[fut]
            try:
                res = fut.result()
            except Exception as e:
                res = {'text': '', 'conf_avg': 0.0, 'raw': None, 'error': str(e)}
            res['name'] = name
            metadata['variants'].append(res)
            results.append(res)

    # Select best variant by avg confidence and text length
    # Score each result by conf_avg * log(1 + len_text)
    import math
    best = None
    best_score = -1
    for r in results:
        txt_len = len(r['text'])
        score = r.get('conf_avg', 0.0) * math.log(1 + txt_len)
        if score > best_score:
            best_score = score
            best = r

    # Merge lines from all variants preferring lines from higher-confidence variants
    line_map = {}  # line -> best_conf
    for r in sorted(results, key=lambda x: x.get('conf_avg', 0.0), reverse=True):
        for line in (r.get('text') or '').split('\n'):
            l = line.strip()
            if not l:
                continue
            # store if new or higher confidence
            prev_conf = line_map.get(l, 0.0)
            if r.get('conf_avg', 0.0) >= prev_conf:
                line_map[l] = r.get('conf_avg', 0.0)

    # Order lines by confidence then by length
    merged_lines = sorted(line_map.keys(), key=lambda x: (line_map.get(x, 0.0), len(x)), reverse=True)
    combined_text = '\n'.join(merged_lines)

    metadata['best_variant'] = best['name'] if best else None
    metadata['best_conf'] = best.get('conf_avg', 0.0) if best else 0.0
    metadata['variant_count'] = len(results)

    return combined_text, metadata
