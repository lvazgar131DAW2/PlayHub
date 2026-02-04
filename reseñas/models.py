from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from juegos.models import Juego


# Create your models here.
class Resena(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE,related_name='resenas',verbose_name="Juego")
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario")
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comentario = models.TextField(validators=[MinLengthValidator(25), MaxValueValidator(500)])
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Resena"
        verbose_name_plural = "Resenas"
        ordering = ['-fecha']
        unique_together = ['juego', 'usuario']

    def __str__(self):
        return self.juego

class PerfilUsuario(models.Model):
        """
        Modelo para extender el User de Django con información adicional.
        Relación One to One con el modelo User.
        """

        PLATAFORMAS = [
            ('PC', 'PC'),
            ('PS5', 'PlayStation 5'),
            ('XBOX', 'Xbox Series X'),
            ('SWITCH', 'Nintendo Switch'),
            ('Múltiples', 'Múltiples plataformas')
        ]

        user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario", related_name='perfil')
        bio = models.TextField(blank=True, verbose_name="Biografia",
                               help_text='Cuentanos algo sobre ti y tus gustos en videojuegos.')
        plataforma = models.CharField(max_length=20, choices=PLATAFORMAS, default='PC',
                                      verbose_name="Plataforma favorita")
        avatar_url = models.URLField(
            blank=True,
            verbose_name="Avatar URL",
            help_text="URL de tu imagen de perfil."
        )

        def __str__(self):
            return f"Perfil de usuario: {self.user.username}"

