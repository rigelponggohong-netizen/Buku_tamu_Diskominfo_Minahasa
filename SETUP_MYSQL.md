# Panduan Setup MySQL Laragon untuk Django

## ⚙️ Langkah 1: Pastikan MySQL aktif di Laragon

1. Jalankan **Laragon**.
2. Pastikan tombol **MySQL** berwarna hijau (berarti aktif).
3. Buka **phpMyAdmin** (klik kanan tray icon Laragon → *MySQL → phpMyAdmin*).
   - Biasanya bisa dibuka di browser: http://localhost/phpmyadmin
   - Default credentials:
     ```
     username: root
     password: (kosong)
     ```

---

## 🗃️ Langkah 2: Buat database baru untuk Django

Di phpMyAdmin → tab **Databases** → buat database baru:

```
Nama: absen_db
Collation: utf8_general_ci (atau utf8mb4_unicode_ci)
```

Klik **Create**.

**ATAU** jalankan script otomatis:
```bash
python create_database.py
```
(Tapi ubah nama database menjadi `absen_db` di script tersebut)

---

## 🧩 Langkah 3: Install konektor MySQL untuk Python

Di terminal proyek (aktifkan virtual env dulu):

```bash
pip install mysqlclient
```

> ⚠️ Kalau gagal (kadang error di Windows karena compiler), coba alternatif:
>
> ```bash
> pip install pymysql
> ```
>
> Kalau pakai `pymysql`, edit file `absen/__init__.py` dan uncomment baris:
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

---

## 🛠️ Langkah 4: Settings sudah dikonfigurasi

File `absen/settings.py` sudah dikonfigurasi untuk MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'absen_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

---

## 🧩 Langkah 5 (opsional): Jika pakai `pymysql`

Edit file `absen/__init__.py` dan uncomment baris:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

## 🔁 Langkah 6: Terapkan migrasi ke MySQL

Jalankan di terminal:

```bash
python manage.py makemigrations
python manage.py migrate
```

Kalau berhasil, Django akan membuat tabel-tabel di database `absen_db`.

---

## ✅ Langkah 7: Uji koneksi

Jalankan server:

```bash
python manage.py runserver
```

Kalau tidak ada error, buka phpMyAdmin → lihat database `absen_db`
📂 Kamu akan lihat tabel seperti:

* `auth_user`
* `django_session`
* `django_migrations`
* `django_admin_log`
* `absensi_absensitamu` (tabel untuk data absensi)
* dll.

Berarti Django sudah **terhubung dengan MySQL Laragon** 🎉

---

## 🧠 Ringkasan cepat

| Langkah | Perintah / Tindakan                          | Tujuan                   |
| :------ | :------------------------------------------- | :----------------------- |
| 1       | Aktifkan MySQL di Laragon                    | Jalankan database server |
| 2       | Buat DB `absen_db` di phpMyAdmin             | Siapkan wadah data       |
| 3       | `pip install mysqlclient`                    | Instal driver MySQL      |
| 4       | Edit `settings.py` ✅ (sudah selesai)         | Konfigurasi koneksi      |
| 5       | (Opsional) Tambah `pymysql` di `__init__.py` | Alternatif driver        |
| 6       | `python manage.py migrate`                   | Buat tabel di MySQL      |
| 7       | `python manage.py runserver`                 | Jalankan proyek          |

---

## 📝 Catatan Penting

- Pastikan nama database di phpMyAdmin adalah **`absen_db`** (sesuai dengan settings.py)
- Jika password MySQL tidak kosong, edit `PASSWORD` di settings.py
- Jika masih error, coba ganti `HOST` dari `'127.0.0.1'` ke `'localhost'` atau sebaliknya

