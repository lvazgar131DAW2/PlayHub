from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

PLATAFORMAS = [
    ('PC', 'PC'),
    ('PS5', 'PlayStation 5'),
    ('XBOX', 'Xbox Series X'),
    ('SWITCH', 'Nintendo Switch')]



class Categoria(models.Model):
    """
    Modelo que representa una categoría de juego.
    """
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Nombre")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return f"Categoría: {self.nombre}"



class Juego(models.Model):
    titulo = models.CharField(max_length=100,verbose_name="Título")
    plataforma = models.CharField(max_length=50,choices=PLATAFORMAS)
    precio = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(0.01)])
    fecha_lanzamiento = models.DateField()
    categorias = models.ManyToManyField(Categoria, blank=True, related_name='juegos', verbose_name="Categorías")



    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ['-fecha_lanzamiento']

    def __str__(self):
        return self.titulo
