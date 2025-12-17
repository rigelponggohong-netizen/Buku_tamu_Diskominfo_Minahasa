@echo off
chcp 65001 >nul
echo ============================================================
echo  Instalasi Tesseract OCR - Helper Script
echo ============================================================
echo.
echo Script ini akan membantu Anda menginstall Tesseract OCR.
echo.
echo Pilih opsi:
echo   1. Download Tesseract OCR installer (akan membuka browser)
echo   2. Install via Chocolatey (jika sudah terinstall)
echo   3. Cek apakah Tesseract sudah terinstall di sistem lain
echo   4. Set path manual (jika sudah terinstall tapi tidak terdeteksi)
echo   5. Keluar
echo.
set /p choice="Pilih opsi (1-5): "

if "%choice%"=="1" goto download
if "%choice%"=="2" goto chocolatey
if "%choice%"=="3" goto check
if "%choice%"=="4" goto setpath
if "%choice%"=="5" goto end
goto invalid

:download
echo.
echo Membuka browser untuk download Tesseract OCR...
echo Link download: https://github.com/UB-Mannheim/tesseract/wiki
echo.
start https://github.com/UB-Mannheim/tesseract/wiki
timeout /t 2 >nul
start https://digi.bib.uni-mannheim.de/tesseract/
echo.
echo ============================================================
echo  Instruksi Instalasi:
echo ============================================================
echo.
echo 1. Download installer Tesseract OCR (sudah dibuka di browser)
echo 2. Jalankan installer yang didownload
echo 3. PENTING saat instalasi:
echo    - Centang "Add Tesseract to PATH"
echo    - Pilih bahasa Indonesia (ind) jika ingin OCR Indonesia lebih akurat
echo    - Pilih lokasi default: C:\Program Files\Tesseract-OCR
echo 4. Setelah instalasi selesai, tutup CMD/PowerShell ini dan buka baru
echo 5. Jalankan: python check_tesseract.py untuk verifikasi
echo.
pause
goto end

:chocolatey
echo.
echo Menginstall Tesseract via Chocolatey...
choco install tesseract
if %errorlevel%==0 (
    echo.
    echo Instalasi berhasil! Restart CMD/PowerShell dan jalankan: python check_tesseract.py
) else (
    echo.
    echo Error: Chocolatey tidak terinstall atau error saat instalasi
    echo Silakan install manual dari https://github.com/UB-Mannheim/tesseract/wiki
)
pause
goto end

:check
echo.
echo Mencari Tesseract di lokasi umum...
echo.
set found=0
if exist "C:\Program Files\Tesseract-OCR\tesseract.exe" (
    echo [FOUND] C:\Program Files\Tesseract-OCR\tesseract.exe
    set found=1
)
if exist "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" (
    echo [FOUND] C:\Program Files (x86)\Tesseract-OCR\tesseract.exe
    set found=1
)
if exist "C:\laragon\bin\tesseract\tesseract.exe" (
    echo [FOUND] C:\laragon\bin\tesseract\tesseract.exe
    set found=1
)
if %found%==0 (
    echo Tesseract tidak ditemukan di lokasi umum.
    echo Silakan install Tesseract atau set path manual (opsi 4).
) else (
    echo.
    echo Tesseract ditemukan! Edit file absensi/views.py untuk set path.
)
pause
goto end

:setpath
echo.
echo Untuk set path manual:
echo.
echo 1. Edit file: absensi\views.py
echo 2. Cari baris sekitar line 34-35
echo 3. Uncomment baris berikut:
echo    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
echo 4. Sesuaikan path dengan lokasi Tesseract Anda
echo 5. Save file dan restart Django server
echo.
set /p tesseract_path="Masukkan path lengkap ke tesseract.exe (atau tekan Enter untuk skip): "
if not "%tesseract_path%"=="" (
    if exist "%tesseract_path%" (
        echo.
        echo Path valid! Edit absensi\views.py dan set:
        echo pytesseract.pytesseract.tesseract_cmd = r'%tesseract_path%'
    ) else (
        echo.
        echo Error: Path tidak ditemukan. Pastikan path benar.
    )
)
pause
goto end

:invalid
echo.
echo Opsi tidak valid! Pilih 1-5.
pause
goto end

:end
echo.
echo ============================================================
echo  Selesai!
echo ============================================================
echo.
echo Setelah install Tesseract:
echo   1. Restart CMD/PowerShell
echo   2. Jalankan: python check_tesseract.py
echo   3. Restart Django server
echo.
pause

