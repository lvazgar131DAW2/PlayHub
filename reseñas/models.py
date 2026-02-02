from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.
class Resena(models.Model):
    juego_titulo = models.CharField(max_length=100)
    usuario_username = models.CharField(max_length=100)
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comentario = models.TextField(validators=[MinLengthValidator(25), MaxValueValidator(500)])
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.juego_titulo