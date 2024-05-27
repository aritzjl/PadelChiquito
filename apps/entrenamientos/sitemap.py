from django.contrib import sitemaps
from django.urls import reverse
from .models import Entrenamiento

class EntrenamientoSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Entrenamiento.objects.filter(activo=True)