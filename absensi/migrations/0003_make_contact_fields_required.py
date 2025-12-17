from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0002_absensitamu_jabatan_alamat_nomor_telepon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absensitamu',
            name='alamat',
            field=models.TextField(default='', help_text='Alamat wajib diisi'),
        ),
        migrations.AlterField(
            model_name='absensitamu',
            name='instansi',
            field=models.CharField(default='', help_text='Instansi/Perusahaan wajib diisi', max_length=200),
        ),
        migrations.AlterField(
            model_name='absensitamu',
            name='nomor_telepon',
            field=models.CharField(default='', help_text='Nomor telepon wajib diisi', max_length=15, validators=[django.core.validators.RegexValidator(message='Nomor telepon harus berupa angka maks. 15 digit', regex='^\\d{0,15}$')]),
        ),
    ]

