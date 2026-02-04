from django.forms import ModelForm
from django import forms
from .models import Juego

class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo','plataforma','precio','fecha_lanzamiento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'plataforma': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio

