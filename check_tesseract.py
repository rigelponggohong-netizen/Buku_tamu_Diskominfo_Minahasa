"""
Script untuk memeriksa apakah Tesseract OCR sudah terinstall dan dapat diakses
"""
import os
import sys

def check_tesseract():
    """Cek apakah Tesseract sudah terinstall"""
    print("=" * 60)
    print("Pemeriksaan Instalasi Tesseract OCR")
    print("=" * 60)
    print()
    
    # Cek import pytesseract
    try:
        import pytesseract
        print("✅ pytesseract library sudah terinstall")
    except ImportError:
        print("❌ pytesseract library belum terinstall")
        print("   Jalankan: pip install pytesseract")
        return False
    
    # Cek Tesseract executable
    if os.name == 'nt':  # Windows
        possible_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
            r'C:\laragon\bin\tesseract\tesseract.exe',
            r'C:\Users\{}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'.format(os.getenv('USERNAME', 'User')),
        ]
        
        print("\n🔍 Mencari Tesseract di lokasi umum...")
        found = False
        for path in possible_paths:
            if os.path.exists(path):
                print(f"✅ Tesseract ditemukan di: {path}")
                pytesseract.pytesseract.tesseract_cmd = path
                found = True
                break
        
        if not found:
            print("❌ Tesseract tidak ditemukan di lokasi umum")
            print("\n💡 Solusi:")
            print("   1. Install Tesseract OCR dari: https://github.com/UB-Mannheim/tesseract/wiki")
            print("   2. Atau set path manual di absensi/views.py")
            print("      Edit baris: pytesseract.pytesseract.tesseract_cmd = r'C:\\...\\tesseract.exe'")
            return False
    else:
        # Linux/Mac - cek di PATH
        try:
            import subprocess
            result = subprocess.run(['tesseract', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("✅ Tesseract ditemukan di PATH")
                print(f"   Versi: {result.stdout.split()[1]}")
                found = True
            else:
                found = False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            found = False
            print("❌ Tesseract tidak ditemukan di PATH")
            print("\n💡 Solusi:")
            print("   Linux: sudo apt-get install tesseract-ocr tesseract-ocr-ind")
            print("   Mac: brew install tesseract tesseract-lang")
            return False
    
    # Test Tesseract
    print("\n🧪 Menguji Tesseract...")
    try:
        version = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract berfungsi! Versi: {version}")
        
        # Cek bahasa yang tersedia
        try:
            langs = pytesseract.get_languages(config='')
            print(f"✅ Bahasa yang tersedia: {', '.join(langs)}")
            if 'ind' in langs:
                print("✅ Bahasa Indonesia tersedia!")
            else:
                print("⚠️  Bahasa Indonesia tidak ditemukan (opsional)")
        except:
            print("⚠️  Tidak dapat membaca daftar bahasa")
        
        return True
        
    except Exception as e:
        print(f"❌ Error menguji Tesseract: {e}")
        print("\n💡 Kemungkinan penyebab:")
        print("   - Tesseract tidak terinstall dengan benar")
        print("   - Tesseract tidak ada di PATH")
        print("   - Path Tesseract belum dikonfigurasi di views.py")
        return False


if __name__ == '__main__':
    success = check_tesseract()
    print("\n" + "=" * 60)
    if success:
        print("✅ Tesseract OCR siap digunakan!")
    else:
        print("❌ Tesseract OCR belum siap")
        print("\n📖 Lihat INSTALL_TESSERACT.md untuk panduan instalasi")
    print("=" * 60)
    sys.exit(0 if success else 1)

