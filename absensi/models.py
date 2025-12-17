from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class AbsensiTamu(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100, blank=True, null=True)
    instansi = models.CharField(max_length=200, blank=False, null=False, default='')
    alamat = models.TextField(blank=False, null=False, default='')
    nomor_telepon = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        default='',
        validators=[
            RegexValidator(
                regex=r'^\d{0,15}$',
                message='Nomor telepon harus berupa angka maks. 15 digit'
            )
        ],
    )
    keperluan = models.TextField()
    tanggal_waktu = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-tanggal_waktu']
        verbose_name = 'Absensi Tamu'
        verbose_name_plural = 'Data Absensi Tamu'
    
    def __str__(self):
        return f"{self.nama} - {self.instansi or 'Tidak ada instansi'}"

