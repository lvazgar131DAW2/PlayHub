from django.contrib import admin
from .models import Juego

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'precio', 'fecha_lanzamiento', 'get_categorias')
    search_fields = ('titulo', 'plataforma')
    list_filter = ('plataforma', 'fecha_lanzamiento','categorias')
    ordering = ('-titulo',)
    filter_horizontal = ('categorias',)
    fieldsets = (
        ('Información del Juego', {
            'fields': ('titulo', 'plataforma'),
        }),
        ('Detalles', {
            'fields': ('precio', 'fecha_lanzamiento'),
        }),
        ('Categorías', {
            'fields': ('categorias',),
        }),
    )

    def get_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categorias.all()])
    get_categorias.short_description = 'Categorías'


