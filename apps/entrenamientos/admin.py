from django.contrib import admin
from .models import Entrenamiento, Categoria

# Register your models here.


class EntrenamientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'precioDescuento', 'porcentajeDescuento', 'tipoDePago')  # Campos a mostrar en la lista de objetos
    search_fields = ['titulo', 'descripcion']  # Campos por los que se puede buscar
    list_filter = ['categorias']  # Filtros en la lista
    readonly_fields = ('precioDescuento',)  # Campos que son de solo lectura

admin.site.register(Entrenamiento, EntrenamientoAdmin) 
admin.site.register(Categoria)