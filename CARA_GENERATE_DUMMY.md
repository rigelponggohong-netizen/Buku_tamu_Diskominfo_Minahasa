# Cara Generate Data Dummy Absensi

Script ini akan membuat data dummy untuk testing PDF dengan berbagai variasi:
- 50+ nama Indonesia
- 50+ instansi BUMN dan perusahaan besar
- 50+ jenis keperluan yang variatif

## Cara Menggunakan

### Opsi 1: Menggunakan Django Management Command (Disarankan)

```bash
python manage.py generate_dummy --jumlah 50
```

Parameter `--jumlah` bisa diubah sesuai kebutuhan:
- `--jumlah 50` untuk 50 data
- `--jumlah 100` untuk 100 data
- `--jumlah 200` untuk 200 data

### Opsi 2: Menggunakan Script Langsung

Jika Django sudah terinstall di environment:

```bash
python generate_dummy_data.py
```

## Fitur Script

- ✅ Generate data dengan tanggal random dalam 7 hari terakhir (termasuk hari ini)
- ✅ Random jam antara 08:00 - 17:00
- ✅ Variasi instansi BUMN lengkap (Pertamina, PLN, Bank Mandiri, BRI, dll)
- ✅ 10% chance instansi kosong (untuk variasi)
- ✅ Keperluan yang variatif dan realistis
- ✅ Progress indicator setiap 10 data

## Setelah Generate

1. Buka admin panel: `http://localhost:8000/admin-panel/`
2. Klik tombol **"Download PDF Rekap Hari Ini"**
3. PDF akan berisi data absensi hari ini dengan tabel yang ramai!

## Menghapus Data Dummy

Jika ingin menghapus semua data (hati-hati!):

```bash
python manage.py shell
```

Lalu di shell:
```python
from absensi.models import AbsensiTamu
AbsensiTamu.objects.all().delete()
```

