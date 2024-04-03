from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from apps.entrenamientos.sitemap import EntrenamientoSitemap

sitemaps = {
    'Entrenamiento': EntrenamientoSitemap,
}



urlpatterns = [
    path('entrenamientos/', views.entrenamientos,name='entrenamientos'),
    #path('sitemap-entrenamientos.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
