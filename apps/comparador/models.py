from django.db import models

# Create your models here.

class Pala(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    imagen = models.ImageField(upload_to='palas', null=True, blank=True)
    marca = models.CharField(max_length=255)
    precio = models.FloatField()
    precio_rebaja = models.FloatField()
    temporada = models.IntegerField()
    material_marco = models.CharField(max_length=255)
    material_plano = models.CharField(max_length=255)
    material_goma = models.CharField(max_length=255)
    tacto = models.TextField()
    forma_choices = [
        ('diamante', 'Diamante'),
        ('redonda', 'Redonda'),
        ('hibrida', 'Híbrida'),
    ]
    forma = models.CharField(max_length=10, choices=forma_choices)
    peso = models.CharField(max_length=20)  # Guardado como cadena, por ejemplo, "365-400"

    total_padelzoom = models.FloatField()
    potencia = models.FloatField()
    control = models.FloatField()
    salida_bola = models.FloatField()
    manejabilidad = models.FloatField()
    punto_dulce = models.FloatField()
    fondo_de_pista = models.FloatField()
    volea = models.FloatField()
    bajada_de_pared = models.FloatField()
    bandeja = models.FloatField()
    remate = models.FloatField()
    defensa = models.FloatField()
    ataque = models.FloatField()
    puntuacion_total = models.FloatField()

    balance_choices = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    ]
    balance = models.CharField(max_length=10, choices=balance_choices)

    def __str__(self):
        return self.nombre