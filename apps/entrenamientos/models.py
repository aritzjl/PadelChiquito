from django.db import models

# Create your models here.


class Entrenamiento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    codigoDescuento = models.CharField(max_length=30, blank=True, null=True)
    precioDescuento = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)    
    imagen_portada = models.ImageField(upload_to='entrenamientos/')
    url = models.URLField()