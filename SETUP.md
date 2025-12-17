# Setup Website Absensi Tamu

## Langkah-langkah Setup:

### 1. Buat Database MySQL di Laragon
- Buka phpMyAdmin Laragon atau gunakan HeidiSQL
- Buat database baru dengan nama: `absensi_tamu`
- Atau bisa menggunakan terminal MySQL:
  ```sql
  CREATE DATABASE absensi_tamu CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```

### 2. Install Dependencies
```bash
pip install Django mysqlclient
```
Atau jika mysqlclient bermasalah, bisa install:
```bash
pip install Django mysql-connector-python
```
Lalu ubah ENGINE di settings.py menjadi: `'ENGINE': 'django.db.backends.mysql',`

### 3. Jalankan Migrasi
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Buat Superuser (Optional untuk Admin)
```bash
python manage.py createsuperuser
```

### 5. Jalankan Server
```bash
python manage.py runserver
```

### 6. Akses Website
- Buka browser: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Catatan:
- Database MySQL default Laragon: host=localhost, user=root, password=(kosong)
- Jika password MySQL tidak kosong, update di `absen/settings.py` pada bagian DATABASES

