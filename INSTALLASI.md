# Instalasi dan Setup Website Absensi Tamu

## Database sudah dibuat otomatis! ✓

Database `absensi_tamu` sudah dibuat. Sekarang ikuti langkah berikut:

## Langkah-langkah:

### 1. Pastikan Virtual Environment Aktif
```bash
# Jika belum aktif, aktifkan dengan:
venv\Scripts\activate
```

### 2. Install Dependencies
Pastikan sudah terinstall:
```bash
pip install Django mysql-connector-python
```

### 3. Jalankan Migrasi
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. (Optional) Buat Superuser untuk Admin Panel
```bash
python manage.py createsuperuser
```

### 5. Jalankan Server
```bash
python manage.py runserver
```

### 6. Akses Website
- **Halaman Utama**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Catatan Penting:

- **Database**: Sudah dikonfigurasi untuk Laragon MySQL
  - Database: `absensi_tamu`
  - User: `root`
  - Password: (kosong)
  - Host: `localhost`
  - Port: `3306`

- **Jika password MySQL tidak kosong**: Edit file `absen/settings.py` pada bagian `DATABASES`, isi `PASSWORD` sesuai password MySQL Anda.

- **Jika ada error**: Pastikan MySQL Laragon sudah running (cek di Laragon menu)

