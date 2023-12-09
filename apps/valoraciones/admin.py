from django.contrib import admin
from .models import Estrella, Comentario

class EstrellaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pala', 'valoracion', 'fecha')
    list_filter = ('usuario', 'pala', 'valoracion')
    search_fields = ('usuario__username', 'pala__nombre')  # Reemplaza 'nombre' por el campo apropiado de tu modelo Pala


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pala', 'fecha', 'comentariorespondido')
    list_filter = ('usuario', 'pala')
    search_fields = ('usuario__username', 'pala__nombre')  # Reemplaza 'nombre' por el campo apropiado de tu modelo Pala
    raw_id_fields = ('comentariorespondido',)  # Esto permite una selección más eficiente del comentariorespondido

admin.site.register(Estrella, EstrellaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
