# 🚀 Panduan Instalasi Tesseract OCR untuk Windows (Langkah Cepat)

## ⚡ Install Cepat (5 Menit)

### Langkah 1: Download Tesseract OCR

1. **Buka link berikut:**
   - https://github.com/UB-Mannheim/tesseract/wiki
   - Atau langsung download: https://digi.bib.uni-mannheim.de/tesseract/

2. **Pilih versi terbaru:**
   - Cari file dengan nama seperti: `tesseract-ocr-w64-setup-5.x.x.exe` (untuk Windows 64-bit)
   - Klik download

### Langkah 2: Install Tesseract

1. **Jalankan installer** yang sudah didownload
2. **Pilih lokasi instalasi:**
   - Default: `C:\Program Files\Tesseract-OCR` ✅ (Recommended)
   - Atau bisa: `C:\laragon\bin\tesseract` (jika ingin di Laragon)

3. **⚠️ PENTING - Saat instalasi:**
   - ✅ **Centang "Add Tesseract to PATH"** (SANGAT PENTING!)
   - ✅ **Pilih bahasa Indonesia (ind)** jika ingin OCR bahasa Indonesia lebih akurat
   - ✅ Install komponen tambahan jika diminta

4. **Klik Install** dan tunggu selesai

### Langkah 3: Verifikasi Instalasi

1. **Buka Command Prompt baru** (penting: harus buka baru setelah install!)
2. **Test Tesseract:**
   ```bash
   tesseract --version
   ```
   Jika berhasil, akan muncul versi Tesseract (contoh: `tesseract 5.3.0`)

3. **Test script verifikasi:**
   ```bash
   python check_tesseract.py
   ```
   Seharusnya sekarang muncul: ✅ Tesseract OCR siap digunakan!

### Langkah 4: Restart Django Server

1. **Hentikan server Django** (jika sedang running) - tekan `Ctrl+C`
2. **Jalankan lagi:**
   ```bash
   python manage.py runserver
   ```
3. **Test fitur OCR** di halaman utama

## 📋 Screenshot Panduan (Visual)

### Saat Installer Berjalan:

```
┌─────────────────────────────────────────┐
│   Setup - Tesseract OCR                 │
├─────────────────────────────────────────┤
│   Select Additional Tasks:              │
│                                         │
│   ☑ Add Tesseract to PATH               │  ← PENTING! Centang ini
│   ☑ Install additional language data    │  ← Centang ini juga
│                                         │
│   [Cancel]  [< Back]  [Next >]          │
└─────────────────────────────────────────┘
```

### Pilih Bahasa:

```
┌─────────────────────────────────────────┐
│   Select Components                     │
├─────────────────────────────────────────┤
│   ☑ English (eng)                       │
│   ☑ Indonesian (ind)                    │  ← Pilih ini
│   ☐ Other languages...                  │
│                                         │
│   [Cancel]  [< Back]  [Install]         │
└─────────────────────────────────────────┘
```

## 🔧 Jika Installer Tidak Menambahkan PATH

Jika setelah install, Tesseract masih tidak terdeteksi:

### Opsi A: Tambahkan PATH Manual

1. **Buka System Properties:**
   - Tekan `Win + Pause/Break`
   - Klik "Advanced system settings"
   - Klik "Environment Variables"

2. **Edit System Variables:**
   - Pilih "Path" di bagian "System variables"
   - Klik "Edit"
   - Klik "New"
   - Tambahkan: `C:\Program Files\Tesseract-OCR`
   - Klik OK di semua window

3. **Restart Command Prompt** (buka CMD/PowerShell baru)

### Opsi B: Set Path di Code

1. **Edit file:** `absensi/views.py`
2. **Cari baris sekitar line 34:**
   ```python
   # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
3. **Uncomment dan pastikan path benar:**
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
4. **Save file dan restart Django server**

## ✅ Verifikasi Setelah Install

Jalankan perintah berikut untuk verifikasi:

```bash
# 1. Test Tesseract langsung
tesseract --version

# 2. Test via Python
python check_tesseract.py

# 3. Test bahasa yang tersedia
tesseract --list-langs
```

## 🐛 Troubleshooting

### Error: "tesseract is not installed or it's not in your PATH"

**Solusi 1:** Pastikan sudah install dan restart CMD/PowerShell
```bash
# Tutup semua CMD/PowerShell, buka baru, lalu:
tesseract --version
```

**Solusi 2:** Set path manual di `absensi/views.py`
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

**Solusi 3:** Install ulang dengan memastikan "Add to PATH" dicentang

### Error: "Language 'ind' not found"

**Solusi:** Install ulang Tesseract dan pilih bahasa Indonesia saat instalasi
- Atau download `ind.traineddata` dari: https://github.com/tesseract-ocr/tessdata
- Copy ke folder: `C:\Program Files\Tesseract-OCR\tessdata\`

### Tesseract sudah terinstall tapi tidak terdeteksi

**Cek lokasi instalasi:**
1. Buka File Explorer
2. Cari file `tesseract.exe` di komputer Anda
3. Catat path lengkapnya (contoh: `C:\Program Files\Tesseract-OCR\tesseract.exe`)
4. Set path manual di `absensi/views.py`

## 📦 Download Links

- **Official Windows Installer:** https://github.com/UB-Mannheim/tesseract/wiki
- **Direct Download (Latest):** https://digi.bib.uni-mannheim.de/tesseract/
- **Language Data:** https://github.com/tesseract-ocr/tessdata

## 📝 Catatan Penting

1. **Harus restart CMD/PowerShell** setelah install (jika PATH ditambahkan)
2. **Harus restart Django server** setelah set path di code
3. **Default path:** `C:\Program Files\Tesseract-OCR\tesseract.exe`
4. **Minimal size:** ~100 MB untuk instalasi dasar

## 🎯 Quick Checklist

- [ ] Download Tesseract installer
- [ ] Install Tesseract dengan "Add to PATH" dicentang
- [ ] Pilih bahasa Indonesia (opsional)
- [ ] Restart CMD/PowerShell
- [ ] Test: `tesseract --version`
- [ ] Test: `python check_tesseract.py`
- [ ] Restart Django server
- [ ] Test fitur OCR di website

---

**Setelah semua checklist selesai, fitur OCR akan berfungsi!** ✅

