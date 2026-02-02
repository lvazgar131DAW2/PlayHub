from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator
# Create your models here.

PLATAFORMAS = [
    ('PC', 'PC'),
    ('PS5', 'PlayStation 5'),
    ('XBOX', 'Xbox Series X'),
    ('SWITCH', 'Nintendo Switch')]

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50,choices=PLATAFORMAS)
    precio = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(0.01)])
    fecha_lanzamiento = models.DateField()


    def __str__(self):
        return self.titulo