from django.forms import ModelForm
from django import forms
from .models import Resena

class ResenaForm(ModelForm):
    class Meta:
        model = Resena
        fields = ['juego', 'puntuacion', 'comentario']

    def clean_comentario(self):
        comentario = self.cleaned_data['comentario']
        if len(comentario) < 25:
            raise forms.ValidationError("El comentario debe tener al menos unos 25 caracteres.")
        return comentario

    def clean_puntuacion(self):
        puntuacion = self.cleaned_data['puntuacion']
        if puntuacion < 1 or puntuacion > 10:
            raise forms.ValidationError("El puntuacion debe estar entre 1 y 10.")
        return puntuacion