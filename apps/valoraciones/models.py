from django.db import models
from django.contrib.auth.models import User
from apps.comparador.models import Pala
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.




class Estrella(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pala = models.ForeignKey(Pala, on_delete=models.CASCADE)
    valoracion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['usuario', 'pala']

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pala = models.ForeignKey(Pala, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    comentariorespondido = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    contenido = models.TextField()