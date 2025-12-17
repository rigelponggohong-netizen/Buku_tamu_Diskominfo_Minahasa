"""
Script untuk membuat database MySQL absen_db secara otomatis
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
            cursor.execute("CREATE DATABASE IF NOT EXISTS absen_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✓ Database 'absen_db' berhasil dibuat!")
            
            cursor.close()
            connection.close()
            print("✓ Koneksi MySQL ditutup.")
            
    except Error as e:
        print(f"✗ Error: {e}")
        print("\nAlternatif: Buat database secara manual melalui phpMyAdmin:")
        print("1. Buka http://localhost/phpmyadmin")
        print("2. Klik tab 'Databases'")
        print("3. Nama database: absen_db")
        print("4. Collation: utf8mb4_unicode_ci")
        print("5. Klik 'Create'")

if __name__ == "__main__":
    create_database()

