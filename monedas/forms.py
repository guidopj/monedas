from django import forms
from .models import Moneda

class MonedaForm(forms.ModelForm):

    class Meta:
        model = Moneda
        fields = ['nombreMoneda', 'signo']
        widgets = {
            'nombreMoneda': forms.TextInput(
            attrs={'class': 'form-control'}),
            'signo': forms.TextInput(
                attrs={'class': 'form-control'})
        }
