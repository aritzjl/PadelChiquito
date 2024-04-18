# apps/comparador/sitemap.py

from django.contrib import sitemaps
from .models import BlogPost
from django.urls import reverse

class Blog(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.fecha  # Assuming you have a field named "fecha" in your model

    def location(self, obj):
        return reverse("blog", args=[obj.pk])