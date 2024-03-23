from django.db import models

# Create your models here.


class Entrenamiento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen_portada = models.ImageField(upload_to='entrenamientos/')
    url = models.URLField()