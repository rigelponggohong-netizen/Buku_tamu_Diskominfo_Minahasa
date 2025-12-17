# Panduan Instalasi Tesseract OCR untuk Windows

Tesseract OCR diperlukan untuk fitur OCR (Optical Character Recognition) pada sistem absensi.

## Cara Instalasi di Windows:

### Opsi 1: Install dengan Installer (Recommended)

1. **Download Tesseract OCR:**
   - Kunjungi: https://github.com/UB-Mannheim/tesseract/wiki
   - Download installer untuk Windows (pilih versi terbaru)
   - Atau langsung: https://digi.bib.uni-mannheim.de/tesseract/

2. **Jalankan Installer:**
   - Pilih lokasi instalasi default: `C:\Program Files\Tesseract-OCR`
   - **PENTING:** Saat instalasi, pastikan untuk:
     - ✅ Centang "Add Tesseract to PATH" (opsi ini akan menambahkan Tesseract ke environment PATH)
     - ✅ Pilih bahasa Indonesia (ind) jika ingin mendukung OCR bahasa Indonesia

3. **Restart Command Prompt/PowerShell** setelah instalasi selesai (jika PATH ditambahkan)

4. **Verifikasi Instalasi:**
   ```bash
   tesseract --version
   ```
   Jika berhasil, akan menampilkan versi Tesseract.

### Opsi 2: Install dengan Chocolatey

Jika Anda menggunakan Chocolatey:

```bash
choco install tesseract
```

### Opsi 3: Manual Setup Path (Jika Tesseract sudah terinstall)

Jika Tesseract sudah terinstall tapi tidak di PATH, Anda bisa:

1. **Edit file `absensi/views.py`:**
   - Cari baris yang berisi `pytesseract.pytesseract.tesseract_cmd`
   - Uncomment dan sesuaikan path sesuai lokasi instalasi Tesseract Anda
   - Contoh:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```

2. **Atau tambahkan ke Environment Variables:**
   - Buka System Properties → Advanced → Environment Variables
   - Edit "Path" di System Variables
   - Tambahkan path folder Tesseract (contoh: `C:\Program Files\Tesseract-OCR`)
   - Klik OK dan restart aplikasi

## Install Language Pack Indonesia (Opsional):

Untuk meningkatkan akurasi OCR teks bahasa Indonesia:

1. **Download language data:**
   - Download dari: https://github.com/tesseract-ocr/tessdata
   - File yang dibutuhkan: `ind.traineddata`

2. **Copy ke folder tessdata:**
   - Lokasi: `C:\Program Files\Tesseract-OCR\tessdata\`
   - Copy file `ind.traineddata` ke folder tersebut

3. **Atau install via installer:**
   - Saat instalasi Tesseract, pilih bahasa Indonesia dari daftar bahasa

## Verifikasi Setelah Instalasi:

1. **Test dari Command Prompt:**
   ```bash
   tesseract --version
   tesseract --list-langs
   ```

2. **Test dari Python:**
   ```python
   import pytesseract
   print(pytesseract.get_tesseract_version())
   ```

## Troubleshooting:

### Error: "tesseract is not installed or it's not in your PATH"

**Solusi 1:** Pastikan Tesseract sudah terinstall dan ada di PATH
- Cek dengan: `tesseract --version` di Command Prompt
- Jika error, install ulang atau tambahkan ke PATH

**Solusi 2:** Set path manual di Python
- Edit `absensi/views.py`
- Uncomment baris: `pytesseract.pytesseract.tesseract_cmd = r'C:\...'`
- Sesuaikan path dengan lokasi instalasi Tesseract Anda

**Solusi 3:** Restart aplikasi
- Setelah mengubah PATH atau install Tesseract, restart Django server dan browser

### Error: "Language 'ind' tidak ditemukan"

- Download dan install language pack Indonesia (ind.traineddata)
- Letakkan di folder `tessdata` Tesseract
- Atau install ulang Tesseract dengan memilih bahasa Indonesia saat instalasi

## Catatan:

- Tesseract OCR adalah software open-source yang terpisah dari Python
- Perlu diinstall terpisah, bukan hanya via pip install
- Default path di Windows: `C:\Program Files\Tesseract-OCR\tesseract.exe`
- Jika menggunakan Laragon, bisa install di: `C:\laragon\bin\tesseract\`

## Link Penting:

- **Official Tesseract OCR:** https://github.com/tesseract-ocr/tesseract
- **Windows Installer:** https://github.com/UB-Mannheim/tesseract/wiki
- **Language Data:** https://github.com/tesseract-ocr/tessdata

