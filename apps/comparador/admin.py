from django.contrib import admin
from django.utils.html import format_html
from .models import Pala
from .models import Tienda, PrecioPala

class PalaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'display_image','marca', 'precio', 'puntuacion_total')
    list_filter = ('marca', 'temporada', 'forma', 'balance')
    search_fields = ('nombre', 'marca')
    ordering = ('-temporada', 'precio')

    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'imagen', 'marca', 'precio', 'precio_rebaja', 'temporada')
        }),
        ('Materiales', {
            'fields': ('material_marco', 'material_plano', 'material_goma', 'tacto')
        }),
        ('Características Físicas', {
            'fields': ('forma', 'peso')
        }),
        ('Estadísticas', {
            'fields': (
                'total_padelzoom', 'potencia', 'control', 'salida_bola',
                'manejabilidad', 'punto_dulce', 'fondo_de_pista', 'volea',
                'bajada_de_pared', 'bandeja', 'remate', 'defensa', 'ataque',
                'puntuacion_total'
            )
        }),
        ('Equilibrio', {
            'fields': ('balance',)
        }),
    )

    def display_image(self, obj):
        return format_html('<img src="{}" height="50"/>', obj.imagen.url) if obj.imagen else ''
    display_image.short_description = 'Imagen'

admin.site.register(Pala, PalaAdmin)



class PrecioPalaInline(admin.TabularInline):
    model = PrecioPala
    extra = 1

class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_promocional', 'descuento')
    search_fields = ['nombre']
    inlines = [PrecioPalaInline]

class PrecioPalaAdmin(admin.ModelAdmin):
    list_display = ('pala', 'tienda', 'precio', 'fecha')
    list_filter = ['tienda', 'fecha']
    search_fields = ['pala__nombre', 'tienda__nombre']
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['pala', 'tienda', 'fecha']
        else:
            return []

    def has_add_permission(self, request):
        return False

admin.site.register(Tienda, TiendaAdmin)
admin.site.register(PrecioPala, PrecioPalaAdmin)
