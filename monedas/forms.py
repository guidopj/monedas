from django import forms
from .models import Moneda
from .models import Usuario

class MonedaForm(forms.ModelForm):

    class Meta:
        model = Moneda
        fields = ['nombreMoneda', 'signo', 'peso', 'espesor']
        widgets = {
            'nombreMoneda': forms.TextInput(
                 attrs={'class': 'form-control'}),
            'signo': forms.TextInput(
                attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'espesor': forms.NumberInput(
                attrs={'class': 'form-control'})
        }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombreUsuario', 'contrasena', 'nombre', 'apellido', 'fecha_nac']
        widgets = {
            'nombreUsuario': forms.TextInput(
                 attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(
                attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(
                attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(
                attrs={'class': 'form-control'}),
        }

class LoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombreUsuario', 'contrasena']
        widgets = {
            'nombreUsuario': forms.TextInput(
                 attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(
                attrs={'class': 'form-control'}),
        }
