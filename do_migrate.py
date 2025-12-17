"""
Script untuk menjalankan migrasi database secara otomatis
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'absen.settings')
django.setup()

from django.core.management import call_command

print("=" * 50)
print("Menjalankan Migrasi Database...")
print("=" * 50)

try:
    print("\n1. Membuat migration files...")
    call_command('makemigrations')
    print("✓ Migration files dibuat!")
    
    print("\n2. Menjalankan migrasi ke database...")
    call_command('migrate', verbosity=2)
    print("✓ Migrasi berhasil!")
    
    print("\n" + "=" * 50)
    print("SUKSES! Tabel database sudah dibuat.")
    print("Silakan refresh browser Anda di http://127.0.0.1:8000/")
    print("=" * 50)
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    print("\nPastikan:")
    print("1. MySQL Laragon sudah running")
    print("2. Database 'absen_db' sudah dibuat")
    print("3. Virtual environment sudah aktif")
    print("4. mysqlclient atau pymysql sudah terinstall")
    sys.exit(1)

