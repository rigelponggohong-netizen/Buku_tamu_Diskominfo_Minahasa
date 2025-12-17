@echo off
echo Menjalankan migrasi database...
python manage.py makemigrations
python manage.py migrate
echo.
echo Migrasi selesai! Tekan tombol apa saja untuk keluar...
pause >nul

