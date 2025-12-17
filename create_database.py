"""
Script untuk membuat database MySQL secara otomatis
"""
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Koneksi ke MySQL tanpa database (karena database belum ada)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Buat database jika belum ada
            cursor.execute("CREATE DATABASE IF NOT EXISTS absensi_tamu CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✓ Database 'absensi_tamu' berhasil dibuat!")
            
            cursor.close()
            connection.close()
            print("✓ Koneksi MySQL ditutup.")
            
    except Error as e:
        print(f"✗ Error: {e}")
        print("\nAlternatif: Buat database secara manual melalui phpMyAdmin atau HeidiSQL:")
        print("CREATE DATABASE absensi_tamu CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")

if __name__ == "__main__":
    create_database()

