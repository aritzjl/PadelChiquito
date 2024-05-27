from django.contrib import admin
from .models import ContenidoPublicitario

# Register your models here.
class ContenidoPublicitarioAdmin(admin.ModelAdmin):
    #Añadir descripcion a los campos, del tamaño reocmendado para cada imagen
    def inicio_1(self, obj):
        return obj.inicio_1.url
    def inicio_2(self, obj):
        return obj.inicio_2.url
    def inicio_3(self, obj):
        return obj.inicio_3.url
    def comparador_1(self, obj):
        return obj.comparador_1.url
    def comparador_2(self, obj):
        return obj.comparador_2.url
    inicio_1.short_description = 'Inicio 1 (1920x1080)'
    
    inicio_2.short_description = 'Inicio 2 (1920x1080)'
    
    inicio_3.short_description = 'Inicio 3 (1920x1080)'
    
    comparador_1.short_description = 'Comparador 1 (1920x1080)'
    comparador_2.short_description = 'Comparador 2 (1920x1080)'
    
    
admin.site.register(ContenidoPublicitario, ContenidoPublicitarioAdmin)
