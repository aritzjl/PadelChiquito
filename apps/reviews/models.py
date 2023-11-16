from django.db import models
from apps.comparador.models import Pala
# Create your models here.

class Review(models.Model):
    PALA_CHOICES = [(pala.pk, pala.nombre) for pala in Pala.objects.all()]
    
    pala = models.ForeignKey(Pala, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    video_url = models.URLField()
    
    PLATFORM_CHOICES = [
        ('INSTA', 'Instagram'),
        ('TIKTOK', 'TikTok'),
        ('YOUTUBE', 'YouTube'),
    ]
    plataforma = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pala.nombre} - {self.titulo} - {self.get_plataforma_display()}"