# apps/comparador/sitemap.py

from django.contrib import sitemaps
from .models import Pala
from django.urls import reverse

class PalaSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Pala.objects.all()

    def lastmod(self, obj):
        return obj.get_last_price_update_date()  # Assuming you have a field named "fecha" in your model

    def location(self, obj):
        return reverse("mostrar_pala", args=[obj.pk])