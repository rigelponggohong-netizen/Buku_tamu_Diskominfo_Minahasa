@echo off
echo ========================================
echo QUICK FIX: Jalankan Migrasi Database
echo ========================================
echo.
echo Hentikan server Django dulu (Ctrl+C) jika masih running!
echo.
pause
echo.
echo Menjalankan migrasi...
python do_migrate.py
echo.
echo Selesai! Sekarang jalankan: python manage.py runserver
pause



