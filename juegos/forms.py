from django.forms import ModelForm
from django import forms
from .models import Juego

class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo','plataforma','precio','fecha_lanzamiento']

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio

