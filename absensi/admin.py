from django.contrib import admin
from .models import AbsensiTamu


@admin.register(AbsensiTamu)
class AbsensiTamuAdmin(admin.ModelAdmin):
    list_display = ['nama', 'jabatan', 'instansi', 'alamat', 'nomor_telepon', 'keperluan', 'tanggal_waktu']
    list_filter = ['tanggal_waktu']
    search_fields = ['nama', 'jabatan', 'instansi', 'alamat', 'nomor_telepon', 'keperluan']
    readonly_fields = ['tanggal_waktu']

