
from django.db import models


class Pala(models.Model):
    palaID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='palas', null=True, blank=True)
    marca = models.CharField(max_length=255)
    precio = models.FloatField(blank=True, null=True)
    precio_rebaja = models.FloatField(blank=True, null=True)
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
        ('Diamante', 'Diamante'),
        ('Redonda', 'Redonda'),
        ('Hibrida', 'Híbrida'),
    ]
    forma = models.CharField(max_length=10, choices=forma_choices)
    peso = models.CharField(max_length=20)  # Guardado como cadena, por ejemplo, "365-400"

    total_padelzoom = models.FloatField(blank=True, null=True)
    potencia = models.FloatField(blank=True, null=True)
    control = models.FloatField(blank=True, null=True)
    salida_bola = models.FloatField(blank=True, null=True)
    manejabilidad = models.FloatField(blank=True, null=True)
    punto_dulce = models.FloatField(blank=True, null=True)
    fondo_de_pista = models.FloatField(blank=True, null=True)
    volea = models.FloatField(blank=True, null=True)
    bajada_de_pared = models.FloatField(blank=True, null=True)
    bandeja = models.FloatField(blank=True, null=True)
    remate = models.FloatField(blank=True, null=True)
    defensa = models.FloatField(blank=True, null=True)
    ataque = models.FloatField(blank=True, null=True)
    puntuacion_total = models.FloatField(blank=True, null=True)

    balance_choices = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    ]
    balance = models.CharField(max_length=12, choices=balance_choices)
    
    NIVEL_CHOICES = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]

    nivel = models.CharField(
        max_length=12,
        choices=NIVEL_CHOICES,
        default='NINGUNO',
        blank=True,
    )   


    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
            fields_to_round = [
                'precio', 'precio_rebaja', 'total_padelzoom', 'potencia', 'control', 'salida_bola',
                'manejabilidad', 'punto_dulce', 'fondo_de_pista', 'volea', 'bajada_de_pared',
                'bandeja', 'remate', 'defensa', 'ataque', 'puntuacion_total'
            ]

            # Redondea los campos Float a 2 decimales antes de guardar
            for field_name in fields_to_round:
                field_value = getattr(self, field_name)
                if isinstance(field_value, float):
                    setattr(self, field_name, round(field_value, 2))

            super().save(*args, **kwargs)  # Llama al método save de la clase base (models.Model)
            
    def getInfo(self):
        
        return {
            'nombre': self.nombre,
            'marca': self.marca,
            'precio_rebaja': self.precio_rebaja,
            'temporada': self.temporada,
            'material_marco': self.material_marco,
            'material_plano': self.material_plano,
            'material_goma': self.material_goma,
            'tacto': self.tacto,
            'forma': self.forma,
            'peso': self.peso,
            'total_padelzoom': self.total_padelzoom,
            'potencia': self.potencia,
            'control': self.control,
            'salida_bola': self.salida_bola,
            'manejabilidad': self.manejabilidad,
            'punto_dulce': self.punto_dulce,
            'fondo_de_pista': self.fondo_de_pista,
            'volea': self.volea,
            'bajada_de_pared': self.bajada_de_pared,
            'bandeja': self.bandeja,
            'remate': self.remate,
            'defensa': self.defensa,
            'ataque': self.ataque,
            'puntuacion_total': self.puntuacion_total,
            'balance': self.balance,
            'nivel': self.nivel,
        }

class PalaBuscada(models.Model):
    pala = models.ForeignKey(Pala, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class Tienda(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='tiendas', null=True, blank=True)
    codigo_promocional = models.CharField(max_length=50, null=True, blank=True)
    descuento = models.FloatField(null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.nombre

class PrecioPala(models.Model):
    pala = models.ForeignKey(Pala, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    precio = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    # Aquí podrías añadir otros detalles, como precio más bajo, si lo deseas

    def __str__(self):
        return f"{self.pala.nombre} - {self.tienda.nombre} - {self.precio}"
    def save(self, *args, **kwargs):
        self.precio = round(self.precio, 2)  # Redondea el precio a 2 decimales
        super().save(*args, **kwargs)  # Llama al método save de la clase base (models.Model)

