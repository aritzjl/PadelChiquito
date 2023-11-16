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
    TACTO_CHOICES = [
            ('Blando', 'Blando'),
            ('Medio-Duro', 'Medio-Duro'),
            ('Duro', 'Duro'),
            ('Medio-Blando', 'Medio-Blando'),
            ('Medio', 'Medio'),
        ]

    tacto = models.CharField(max_length=20, choices=TACTO_CHOICES, null=True, blank=True)
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

class Tienda(models.Model):
    nombre = models.CharField(max_length=255)
    codigo_promocional = models.CharField(max_length=50, null=True, blank=True)
    descuento = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class PrecioPala(models.Model):
    pala = models.ForeignKey(Pala, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    precio = models.FloatField()
    url = models.URLField()
    fecha = models.DateTimeField(auto_now_add=True)
    # Aquí podrías añadir otros detalles, como precio más bajo, si lo deseas

    def __str__(self):
        return f"{self.pala.nombre} - {self.tienda.nombre} - {self.precio}"

