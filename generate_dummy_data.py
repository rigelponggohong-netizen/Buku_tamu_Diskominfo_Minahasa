"""
Script untuk generate data dummy absensi tamu dengan variasi instansi BUMN
Jalankan dengan: python generate_dummy_data.py
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'absen.settings')
django.setup()

from absensi.models import AbsensiTamu
from django.utils import timezone

# Daftar nama-nama Indonesia
nama_dummy = [
    "Budi Santoso", "Siti Nurhaliza", "Ahmad Yani", "Dewi Sartika", "Joko Widodo",
    "Mega Waty", "Agus Harimurti", "Sri Mulyani", "Bambang Soesatyo", "Puan Maharani",
    "Ganjar Pranowo", "Prabowo Subianto", "Anies Baswedan", "Ridwan Kamil", "Tri Rismaharini",
    "Erick Thohir", "Luhut Binsar", "Puan Maharani", "Bahlil Lahadalia", "Johnny G. Plate",
    "Sakti Wahyu Trenggono", "Arifin Tasrif", "Tito Karnavian", "Yasonna Laoly", "Muhadjir Effendy",
    "Teten Masduki", "Abdul Halim Iskandar", "Sandiaga Uno", "Suharso Monoarfa", "Ida Fauziyah",
    "Edhy Prabowo", "Andika Perkasa", "Marsetio", "Yudo Margono", "Agus Suhartono",
    "Rini Soemarno", "Novel Baswedan", "Ema Sumarna", "Rudy Gunawan", "Wawan Setiawan",
    "Ayu Ting Ting", "Iwan Fals", "Titi Kamal", "Bunga Citra Lestari", "Rossa",
    "Agnes Monica", "Maudy Ayunda", "Raisa Andriana", "Isyana Sarasvati", "Rizky Febrian",
    "Ardhito Pramono", "Rich Brian", "NIKI", "Warren Hue", "Brian Imanuel",
]

# Daftar instansi BUMN dan perusahaan besar
instansi_dummy = [
    "PT Pertamina (Persero)", "PT PLN (Persero)", "PT Bank Mandiri (Persero) Tbk",
    "PT Bank Rakyat Indonesia (Persero) Tbk", "PT Bank Negara Indonesia (Persero) Tbk",
    "PT Telekomunikasi Indonesia Tbk", "PT Jasa Marga (Persero) Tbk", "PT Wijaya Karya (Persero) Tbk",
    "PT Adhi Karya (Persero) Tbk", "PT Waskita Karya (Persero) Tbk", "PT Perusahaan Listrik Negara (Persero)",
    "PT Kereta Api Indonesia (Persero)", "PT Angkasa Pura I (Persero)", "PT Angkasa Pura II (Persero)",
    "PT Garuda Indonesia (Persero) Tbk", "PT Pelabuhan Indonesia I (Persero)", "PT Pelabuhan Indonesia II (Persero)",
    "PT Pelabuhan Indonesia III (Persero)", "PT Pelabuhan Indonesia IV (Persero)", "PT Krakatau Steel (Persero) Tbk",
    "PT Semen Indonesia (Persero) Tbk", "PT Pupuk Indonesia (Persero)", "PT Kimia Farma (Persero) Tbk",
    "PT Indofood Sukses Makmur Tbk", "PT Unilever Indonesia Tbk", "PT Astra International Tbk",
    "PT Djarum", "PT Gudang Garam Tbk", "PT HM Sampoerna Tbk", "PT Bank Central Asia Tbk",
    "PT Bank CIMB Niaga Tbk", "PT Bank Danamon Indonesia Tbk", "PT Bank Maybank Indonesia Tbk",
    "PT Bank OCBC NISP Tbk", "PT Bank UOB Indonesia", "PT Bank Tabungan Negara (Persero) Tbk",
    "PT Asuransi Jiwa Sinarmas MSIG Tbk", "PT Asuransi Central Asia", "PT Asuransi Jasa Indonesia",
    "PT Reasuransi Nasional Indonesia", "PT Perusahaan Gas Negara (Persero) Tbk", "PT Aneka Tambang (Persero) Tbk",
    "PT Timah (Persero) Tbk", "PT Freeport Indonesia", "PT Chevron Pacific Indonesia",
    "PT ExxonMobil Oil Indonesia", "PT Total Energies", "PT ConocoPhillips Indonesia",
    "PT Medco Energi Internasional Tbk", "PT Energi Mega Persada Tbk", "PT Bayan Resources Tbk",
    "PT Indika Energy Tbk", "PT Adaro Energy Tbk", "PT Bumi Resources Tbk",
]

# Daftar keperluan yang variatif
keperluan_dummy = [
    "Konsultasi keuangan dan investasi",
    "Meeting koordinasi proyek infrastruktur",
    "Presentasi proposal kerjasama bisnis",
    "Kunjungan kerja bidang teknologi informasi",
    "Koordinasi tender pengadaan barang dan jasa",
    "Meeting evaluasi kinerja perusahaan",
    "Konsultasi hukum dan perizinan usaha",
    "Kunjungan kerja lapangan proyek konstruksi",
    "Koordinasi program CSR dan pengembangan masyarakat",
    "Presentasi laporan keuangan triwulan",
    "Meeting strategi ekspansi bisnis",
    "Konsultasi manajemen risiko operasional",
    "Koordinasi pengadaan material konstruksi",
    "Kunjungan audit internal perusahaan",
    "Meeting review kontrak kerjasama",
    "Presentasi rencana strategis jangka panjang",
    "Konsultasi teknologi digitalisasi perusahaan",
    "Koordinasi proyek pembangkit listrik",
    "Meeting evaluasi investasi infrastruktur",
    "Kunjungan inspeksi fasilitas produksi",
    "Koordinasi program pelatihan SDM",
    "Presentasi hasil riset pasar dan kompetitor",
    "Meeting strategi pemasaran dan branding",
    "Konsultasi environmental impact assessment",
    "Koordinasi logistik dan distribusi produk",
    "Kunjungan due diligence untuk merger",
    "Meeting evaluasi performa portofolio investasi",
    "Presentasi proposal joint venture",
    "Koordinasi pengadaan teknologi terbaru",
    "Konsultasi tata kelola perusahaan dan compliance",
    "Meeting koordinasi dengan regulator",
    "Kunjungan monitoring proyek EPC",
    "Koordinasi program sustainability dan ESG",
    "Presentasi laporan keberlanjutan perusahaan",
    "Meeting strategi diversifikasi bisnis",
    "Konsultasi restrukturisasi organisasi",
    "Koordinasi pengadaan peralatan berat",
    "Kunjungan audit kualitas sistem manajemen",
    "Meeting review anggaran dan forecast",
    "Presentasi inovasi produk dan layanan baru",
    "Pinjam WC",  # Ada yang request seperti data user
    "TumarendemPenelitian",  # Ada yang request seperti data user
    "Culik pa alfa",  # Ada yang request seperti data user
    "Rapat koordinasi emergency response",
    "Meeting darurat untuk crisis management",
    "Koordinasi pengadaan alat kesehatan",
    "Kunjungan monitoring project milestone",
    "Meeting review kontrak vendor",
    "Presentasi business intelligence dan analytics",
    "Koordinasi program employee engagement",
]

def generate_dummy_data(jumlah=50):
    """Generate data dummy absensi tamu"""
    
    # Hapus data lama jika ada (optional)
    # AbsensiTamu.objects.all().delete()
    
    print(f"Generating {jumlah} data dummy...")
    
    # Generate data untuk hari ini dan beberapa hari terakhir
    hari_ini = timezone.now().date()
    
    for i in range(jumlah):
        # Random tanggal dalam 7 hari terakhir (termasuk hari ini)
        hari_offset = random.randint(0, 6)
        tanggal_target = hari_ini - timedelta(days=hari_offset)
        
        # Random jam antara 08:00 - 17:00
        jam = random.randint(8, 17)
        menit = random.randint(0, 59)
        
        # Buat datetime aware
        tanggal_waktu = timezone.make_aware(
            datetime.combine(tanggal_target, datetime.min.time().replace(hour=jam, minute=menit))
        )
        
        # Random pilih data
        nama = random.choice(nama_dummy)
        instansi = random.choice(instansi_dummy)
        keperluan = random.choice(keperluan_dummy)
        
        # Kadang-kadang instansi kosong (10% chance)
        if random.random() < 0.1:
            instansi = None
        
        # Buat objek AbsensiTamu
        absensi = AbsensiTamu.objects.create(
            nama=nama,
            instansi=instansi,
            keperluan=keperluan,
            tanggal_waktu=tanggal_waktu
        )
        
        if (i + 1) % 10 == 0:
            print(f"  Generated {i + 1}/{jumlah} data...")
    
    print(f"\n✅ Successfully generated {jumlah} dummy data!")
    print(f"\nStatistik:")
    print(f"  - Total data: {AbsensiTamu.objects.count()}")
    print(f"  - Data hari ini: {AbsensiTamu.objects.filter(tanggal_waktu__date=hari_ini).count()}")
    print(f"  - Data 7 hari terakhir: {AbsensiTamu.objects.filter(tanggal_waktu__gte=timezone.make_aware(datetime.combine(hari_ini - timedelta(days=7), datetime.min.time()))).count()}")

if __name__ == "__main__":
    try:
        # Generate 50 data dummy (bisa diubah jumlahnya)
        generate_dummy_data(50)
        
        print("\n🎉 Data dummy berhasil dibuat!")
        print("Silakan buka admin panel dan download PDF untuk melihat hasilnya.")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

