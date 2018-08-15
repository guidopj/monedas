from django import forms
from .models import Moneda, MonedasUsuario
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
                format="%Y-%m-%d",
                attrs={'class': 'form-control', 'type': 'date'}),
        }

class ComprarMonedasForm(forms.Form):
    moneda = forms.ModelChoiceField(queryset=Moneda.objects.all(), empty_label="--", to_field_name="nombreMoneda")
    cantidad = forms.IntegerField(widget=forms.NumberInput)

class LoginForm(forms.Form):
    nombreUsuario = forms.CharField(max_length=100, widget=forms.TextInput)
    contrasena = forms.CharField(max_length=32, widget=forms.PasswordInput)

class EnviarMonedasForm(forms.Form):
    moneda = forms.ModelChoiceField(queryset=Moneda.objects.all(), empty_label="--", to_field_name="nombreMoneda")
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), empty_label="--", to_field_name="nombreUsuario")
    cantidad = forms.IntegerField(widget=forms.NumberInput)
