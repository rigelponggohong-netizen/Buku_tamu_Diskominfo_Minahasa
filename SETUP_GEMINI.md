# 🚀 Setup Gemini AI untuk OCR

Gemini AI digunakan untuk meningkatkan akurasi deteksi nama dan instansi dari hasil OCR kartu pegawai.

## 📋 Cara Mendapatkan Gemini API Key

### Langkah 1: Daftar/Akses Google AI Studio

1. **Buka Google AI Studio:**
   - Kunjungi: https://aistudio.google.com/
   - Atau: https://makersuite.google.com/app/apikey

2. **Login dengan Google Account:**
   - Gunakan akun Google Anda (pastikan sudah login)

### Langkah 2: Buat API Key

1. **Klik "Get API Key" atau "Create API Key":**
   - Di halaman Google AI Studio, cari tombol "Get API Key"
   - Atau klik menu "API Key"

2. **Pilih Project:**
   - Pilih project Google Cloud yang ada
   - Atau buat project baru (gratis)

3. **Copy API Key:**
   - Setelah API key dibuat, copy API key tersebut
   - Format: `AIzaSy...` (panjang sekitar 39 karakter)

### Langkah 3: Setup API Key di Project

#### Opsi 1: Set di Environment Variable (Recommended)

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**Windows (CMD):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Atau tambahkan ke `.env` file:**
```env
GEMINI_API_KEY=your-api-key-here
```

#### Opsi 2: Set Manual di settings.py (Untuk Testing)

1. **Edit file:** `absen/settings.py`
2. **Cari baris:**
   ```python
   GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
   ```
3. **Ubah menjadi (untuk testing):**
   ```python
   GEMINI_API_KEY = 'your-api-key-here'  # Ganti dengan API key Anda
   ```
4. **⚠️ PERINGATAN:** Jangan commit API key ke Git! Gunakan environment variable untuk production.

### Langkah 4: Install Library

```bash
pip install google-generativeai
```

Atau install semua requirements:
```bash
pip install -r requirements.txt
```

### Langkah 5: Verifikasi

1. **Restart Django server:**
   ```bash
   python manage.py runserver
   ```

2. **Test fitur OCR:**
   - Upload gambar kartu pegawai
   - Sistem akan otomatis menggunakan Gemini AI untuk analisis
   - Hasil akan lebih akurat dalam mendeteksi nama dan instansi

## 📊 Cara Kerja

1. **OCR Tesseract:** Ekstrak teks dari gambar kartu pegawai
2. **Gemini AI Analysis:** Analisis teks OCR menggunakan Gemini AI untuk:
   - Mengidentifikasi nama orang (bukan ID, bukan kode)
   - Mengidentifikasi nama instansi lengkap
   - Memisahkan informasi yang relevan dari noise
3. **Auto-fill Form:** Hasil analisis otomatis mengisi form

## 🎯 Keuntungan Menggunakan Gemini AI

- ✅ **Lebih Akurat:** AI memahami konteks lebih baik dari rule-based
- ✅ **Mengabaikan Noise:** Tidak mengambil nomor ID sebagai nama
- ✅ **Deteksi Instansi Lengkap:** Bisa menggabungkan beberapa baris menjadi satu
- ✅ **Adaptif:** Bisa menangani berbagai format kartu pegawai

## 🔒 Keamanan

- **Jangan commit API key ke Git!**
- Gunakan environment variable untuk production
- API key bersifat rahasia, jangan share ke orang lain
- Jika API key ter-expose, langsung revoke di Google AI Studio

## 💰 Biaya

- **Gratis untuk penggunaan terbatas:** Gemini API memiliki free tier yang cukup untuk penggunaan umum
- **Rate Limit:** Ada batasan request per menit (gratis tier)
- **Lihat pricing:** https://ai.google.dev/pricing

## 🐛 Troubleshooting

### Error: "GEMINI_API_KEY tidak dikonfigurasi"

**Solusi:**
- Pastikan API key sudah di-set di environment variable atau settings.py
- Restart Django server setelah set API key
- Cek apakah API key valid di https://aistudio.google.com/

### Error: "Library google-generativeai belum terinstall"

**Solusi:**
```bash
pip install google-generativeai
```

### Error: "API key tidak valid"

**Solusi:**
- Cek kembali API key di Google AI Studio
- Pastikan API key sudah di-copy dengan lengkap (tidak ada spasi)
- Coba buat API key baru di Google AI Studio

### Gemini tidak digunakan, masih pakai metode tradisional

**Kemungkinan:**
- API key tidak dikonfigurasi → Set API key di settings.py atau environment variable
- Error saat menggunakan Gemini → Cek error message di response JSON
- Sistem otomatis fallback ke metode tradisional jika Gemini gagal

## 📚 Link Penting

- **Google AI Studio:** https://aistudio.google.com/
- **Gemini API Docs:** https://ai.google.dev/docs
- **Pricing:** https://ai.google.dev/pricing
- **API Key Management:** https://aistudio.google.com/app/apikey

## ✅ Checklist Setup

- [ ] Dapatkan Gemini API key dari Google AI Studio
- [ ] Set API key di environment variable atau settings.py
- [ ] Install library: `pip install google-generativeai`
- [ ] Restart Django server
- [ ] Test fitur OCR dengan gambar kartu pegawai
- [ ] Verifikasi hasil lebih akurat dengan Gemini AI

---

**Setelah setup selesai, fitur OCR akan menggunakan Gemini AI untuk analisis yang lebih akurat!** ✅

