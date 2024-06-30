from django.db import models

# Create your models here.
class ContenidoPublicitario(models.Model):
    
    nombre = models.CharField(max_length=255, help_text='Nombre de la campaña publiciaria, por ejemplo: "Black Friday 2021"')
    inicio_1 = models.ImageField(upload_to='publi', null=True, blank=True, help_text='Tamaño recomendado: 1920x1080')
    inicio_1_url = models.URLField(blank=True, null=True)
    inicio_2 = models.ImageField(upload_to='publi', null=True, blank=True, help_text='Tamaño recomendado: 1920x1080')
    inicio_2_url = models.URLField(blank=True, null=True)
    inicio_3 = models.ImageField(upload_to='publi', null=True, blank=True, help_text='Tamaño recomendado: 1920x1080')
    inicio_3_url = models.URLField(blank=True, null=True)
    
    filtros_1 = models.ImageField(upload_to='publi', null=True, blank=True, help_text='Tamaño recomendado: 1920x1080')
    filtros_1_url = models.URLField(blank=True, null=True)
    filtros_2 = models.ImageField(upload_to='publi', null=True, blank=True, help_text='Tamaño recomendado: 1920x1080')
    filtros_2_url = models.URLField(blank=True, null=True)
    
    activo = models.BooleanField(default=False)
    fecha_inicio = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre