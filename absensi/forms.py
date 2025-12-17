from django import forms
from .models import AbsensiTamu


class AbsensiForm(forms.ModelForm):
    class Meta:
        model = AbsensiTamu
        fields = ['nama', 'jabatan', 'instansi', 'alamat', 'nomor_telepon', 'keperluan']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap',
                'required': True
            }),
            'jabatan': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan jabatan'
            }),
            'instansi': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan instansi/perusahaan',
                'required': True
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat lengkap',
                'rows': 2,
                'required': True
            }),
            'nomor_telepon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nomor telepon',
                'maxlength': 15,
                'pattern': r'\d{0,15}',
                'inputmode': 'numeric',
                'required': True
            }),
            'keperluan': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Maksud dan tujuan kunjungan',
                'rows': 3,
                'required': True
            }),
        }
        labels = {
            'nama': 'Nama Lengkap',
            'jabatan': 'Jabatan',
            'instansi': 'Instansi/Perusahaan',
            'alamat': 'Alamat',
            'nomor_telepon': 'Nomor Telepon',
            'keperluan': 'Maksud dan Tujuan',
        }


class DateRangeForm(forms.Form):
    tanggal_mulai = forms.DateField(
        label='Tanggal Mulai',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True
        })
    )
    tanggal_akhir = forms.DateField(
        label='Tanggal Akhir',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True
        })
    )


from django.contrib.auth.models import User

class AdminProfileForm(forms.ModelForm):
    new_password1 = forms.CharField(
        label='Password Baru',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Isi jika ingin mengubah password'}),
        required=False
    )
    new_password2 = forms.CharField(
        label='Konfirmasi Password Baru',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Konfirmasi password baru'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan username baru'}),
        }
        labels = {
            'username': 'Username',
        }

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('Password baru tidak cocok.')
        return new_password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if the username is changed and if it's unique
        if self.instance.pk and username != self.instance.username:
            if User.objects.exclude(pk=self.instance.pk).filter(username__iexact=username).exists():
                raise forms.ValidationError('Username ini sudah digunakan oleh pengguna lain.')
        elif not self.instance.pk and User.objects.filter(username__iexact=username).exists():
             raise forms.ValidationError('Username ini sudah digunakan.')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password1')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user


from django.contrib.auth.forms import UserCreationForm

class AddAdminForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username admin baru'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email admin baru (opsional)'}),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Konfirmasi Password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.fields:
            self.fields['password1'].label = "Password"
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        if 'password2' in self.fields:
            self.fields['password2'].label = "Konfirmasi Password"
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})
            
        for field in self.fields.values():
            if field.help_text:
                field.help_text = field.help_text.replace('Kata sandi', 'Password').replace('Sandi', 'Password').replace('sandi', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = False  # Or True, depending on requirements
        if commit:
            user.save()
        return user
