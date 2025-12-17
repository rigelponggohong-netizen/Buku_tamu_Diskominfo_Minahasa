from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='absensitamu',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='absensitamu',
            name='jabatan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='absensitamu',
            name='nomor_telepon',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Nomor telepon harus berupa angka maks. 15 digit', regex='^\\d{0,15}$')]),
        ),
    ]

