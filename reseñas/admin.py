from django.contrib import admin
from django.contrib.auth.models import User
from reseñas.models import Resena,PerfilUsuario
@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    """
    Configuracion del panel de administrador para reseña (resena)
    """
    list_display = ('get_juego', 'get_usuario','puntuacion','fecha')
    search_fields = ('comentario',)
    list_filter = ('puntuacion','fecha')
    ordering = ('-fecha',)
    readonly_fields = ('fecha',)
    fieldsets = (
        ('Relaciones', {
            'fields': ('juego', 'usuario')
        }),
        ('Valoración', {
            'fields': ('puntuacion', 'comentario')
        }),
        ('Metadadtos', {
            'fields': ('fecha',)
        })


    )

    def get_usuario(self,obj):
        return obj.usuario.username
    get_usuario.short_description = 'Usuario'
    get_usuario.admin_order_field = 'usuario__username'

    def get_juego(self,obj):
        return obj.juego.titulo
    get_juego.short_description = 'Juego'
    get_juego.admin_order_field = 'juego'
