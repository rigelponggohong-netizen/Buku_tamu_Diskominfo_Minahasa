# Sistem Absensi Tamu dengan OCR dan AI

[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-red.svg)](https://github.com/tesseract-ocr/tesseract)
[![Gemini AI](https://img.shields.io/badge/Google-Gemini_AI-purple.svg)](https://ai.google.dev/)

Sistem absensi tamu berbasis web yang menggunakan teknologi OCR (Optical Character Recognition) dan AI untuk memproses kartu identitas secara otomatis. Sistem ini dirancang khusus untuk instansi pemerintah dan perusahaan yang membutuhkan manajemen tamu yang efisien dan akurat.

## ✨ Fitur Utama

### 🎯 **Pengenalan Pintar dengan AI**
- **OCR Canggih**: Menggunakan Tesseract OCR dengan preprocessing gambar yang dioptimasi
- **AI Gemini**: Integrasi Google Gemini AI untuk ekstraksi nama dan instansi yang akurat
- **Deteksi Otomatis**: Membedakan nama orang vs nama instansi secara cerdas
- **Multi-format**: Mendukung berbagai jenis kartu identitas (KTP, SIM, kartu pegawai, dll)

### 📊 **Manajemen Data**
- **Database MySQL**: Penyimpanan data yang handal dan scalable
- **Admin Panel**: Interface admin lengkap untuk mengelola data absensi
- **Filter Tanggal**: Pencarian data berdasarkan rentang tanggal
- **Real-time**: Pencatatan waktu absensi secara otomatis

### 📄 **Laporan & Ekspor**
- **PDF Report**: Generate laporan PDF dengan format profesional
- **Excel Export**: Ekspor data ke format Excel untuk analisis lebih lanjut
- **Custom Period**: Laporan berdasarkan periode tanggal yang dipilih
- **Responsive Design**: Tampilan yang responsif di berbagai device

### 🔒 **Keamanan & Akses**
- **Authentication**: Sistem login untuk admin
- **Role-based Access**: Kontrol akses berdasarkan peran pengguna
- **Data Validation**: Validasi input data yang ketat
- **Error Handling**: Penanganan error yang komprehensif

## 🛠️ Tech Stack

### Backend
- **Django 5.2.7** - Web framework utama
- **Python 3.8+** - Bahasa pemrograman
- **MySQL 8.0+** - Database utama

### AI & OCR
- **Tesseract OCR** - Engine OCR untuk ekstraksi teks
- **Google Gemini AI** - AI untuk analisis teks dan klasifikasi
- **OpenCV** - Preprocessing gambar
- **Pillow** - Manipulasi gambar

### Frontend & UI
- **HTML5/CSS3** - Struktur dan styling
- **JavaScript** - Interaktivitas
- **Bootstrap** - Framework CSS responsif

### Libraries & Tools
- **ReportLab** - Generate PDF reports
- **OpenPyXL** - Generate Excel files
- **Google Generative AI** - Integrasi Gemini AI

## 📋 Prerequisites

Sebelum menjalankan aplikasi ini, pastikan sistem Anda memiliki:

- **Python 3.8 atau lebih tinggi**
- **MySQL Server 8.0+**
- **Tesseract OCR** (lihat panduan instalasi)
- **Git** (untuk cloning repository)

## 🚀 Instalasi & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/absensi-tamu-ocr.git
cd absensi-tamu-ocr
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Database MySQL
```bash
# Buat database baru di phpMyAdmin atau MySQL CLI
CREATE DATABASE absen_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Install Tesseract OCR
Ikuti panduan instalasi di file `INSTALL_TESSERACT.md` atau `INSTALL_TESSERACT_WINDOWS.md`

### 5. Konfigurasi Environment
```bash
# Setup Gemini AI API Key (opsional, tapi direkomendasikan)
# Dapatkan API key dari: https://makersuite.google.com/app/apikey
set GEMINI_API_KEY=your_api_key_here
```

### 6. Migrasi Database
```bash
# Jalankan migrasi Django
python manage.py migrate

# (Opsional) Generate dummy data untuk testing
python manage.py generate_dummy
```

### 7. Buat Superuser Admin
```bash
python manage.py createsuperuser
```

### 8. Jalankan Server
```bash
python manage.py runserver
```

Akses aplikasi di: `http://127.0.0.1:8000`

## 📖 Penggunaan

### Untuk Tamu (User)
1. **Akses Halaman Utama**: Kunjungi `http://127.0.0.1:8000`
2. **Isi Form Manual**: Masukkan nama, instansi, dan keperluan
3. **Upload Gambar**: Upload foto kartu identitas untuk OCR otomatis
4. **Auto-fill**: Sistem akan mengisi form secara otomatis menggunakan AI
5. **Submit**: Klik submit untuk menyimpan data absensi

### Untuk Admin
1. **Login Admin**: Kunjungi `http://127.0.0.1:8000/login/`
2. **Dashboard**: Lihat semua data absensi tamu
3. **Filter Data**: Gunakan filter tanggal untuk mencari data spesifik
4. **Export Data**: Download laporan dalam format PDF atau Excel
5. **Kelola Data**: Edit atau hapus data absensi jika diperlukan

## 🔧 API Endpoints

### OCR Processing
```
POST /ocr/process/
```
Upload gambar kartu identitas untuk diproses OCR dan AI.

**Request:**
- `image`: File gambar (PNG, JPG, JPEG)

**Response:**
```json
{
  "success": true,
  "raw_text": "teks OCR mentah",
  "detected_name": "Nama Lengkap",
  "detected_institution": "Nama Instansi",
  "using_ai": true
}
```

### Admin Endpoints
- `GET /admin-panel/` - Dashboard admin (login required)
- `GET /login/` - Halaman login admin
- `POST /logout/` - Logout admin
- `GET /download/pdf/` - Download laporan PDF
- `GET /download/excel/` - Download laporan Excel

## 📁 Struktur Project

```
absen/
├── absen/                    # Konfigurasi Django utama
│   ├── settings.py          # Pengaturan aplikasi
│   ├── urls.py              # Routing utama
│   └── wsgi.py              # WSGI config
├── absensi/                  # Aplikasi utama
│   ├── models.py            # Model database
│   ├── views.py             # Logic aplikasi
│   ├── forms.py             # Form Django
│   ├── ocr_utils.py         # Utilities OCR
│   ├── urls.py              # Routing aplikasi
│   ├── admin.py             # Konfigurasi admin
│   └── templates/           # Template HTML
├── static/                   # Static files (CSS, JS, images)
├── requirements.txt          # Dependencies Python
├── manage.py                 # Django management script
└── README.md                 # Dokumentasi ini
```

## ⚙️ Konfigurasi

### Settings Database
Edit file `absen/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'absen_db',
        'USER': 'root',
        'PASSWORD': '',  # Sesuaikan dengan password MySQL Anda
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### Gemini AI API Key
```python
# Di settings.py atau environment variable
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'your-api-key-here')
```

### Tesseract Path (Windows)
Jika Tesseract tidak ada di PATH:
```python
# Di views.py, uncomment dan sesuaikan path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 🐛 Troubleshooting

### Error Database Connection
```
django.db.utils.OperationalError: (2003, "Can't connect to MySQL server")
```
**Solusi:**
- Pastikan MySQL server sedang berjalan
- Periksa kredensial database di `settings.py`
- Pastikan database `absen_db` sudah dibuat

### Error Tesseract Not Found
```
pytesseract.pytesseract.TesseractNotFoundError
```
**Solusi:**
- Install Tesseract OCR (lihat `INSTALL_TESSERACT.md`)
- Pastikan path Tesseract sudah benar
- Restart terminal/command prompt

### Error Gemini AI
```
GEMINI_API_KEY tidak dikonfigurasi
```
**Solusi:**
- Dapatkan API key dari Google AI Studio
- Set environment variable atau edit `settings.py`
- Sistem akan fallback ke metode OCR tradisional jika AI gagal

## 🤝 Contributing

Kontribusi sangat diterima! Silakan ikuti langkah berikut:

1. **Fork** repository ini
2. **Buat branch** untuk fitur baru: `git checkout -b feature/AmazingFeature`
3. **Commit** perubahan: `git commit -m 'Add some AmazingFeature'`
4. **Push** ke branch: `git push origin feature/AmazingFeature`
5. **Buat Pull Request**

### Development Guidelines
- Ikuti PEP 8 untuk Python code style
- Tambahkan docstring pada function baru
- Test functionality sebelum commit
- Update dokumentasi jika diperlukan

## 📄 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- **Django Framework** - Web framework yang powerful
- **Tesseract OCR** - Engine OCR open source
- **Google Gemini AI** - AI untuk text analysis
- **OpenCV** - Computer vision library
- **ReportLab** - PDF generation library

## 📞 Support

Jika Anda mengalami masalah atau memiliki pertanyaan:

- **Issues**: Buat issue di GitHub repository ini
- **Email**: [your-email@example.com]
- **Documentation**: Lihat file-file panduan di folder project

---

**Catatan**: Pastikan untuk mengganti placeholder seperti `your-username`, `your-email@example.com`, dll dengan informasi yang sesuai sebelum publish ke GitHub.

---

<div align="center">
  <p>Dibuat dengan ❤️ untuk kemudahan manajemen absensi tamu</p>
  <p>
    <a href="#sistem-absensi-tamu-dengan-ocr-dan-ai">Kembali ke atas</a>
  </p>
</div>
