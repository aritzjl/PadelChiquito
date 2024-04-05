from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from apps.comparador.sitemap import PalaSitemap
from django.urls import re_path
from django.views.static import serve


sitemaps = {
    'Pala': PalaSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('',include('apps.comparador.urls')),
    path('',include('apps.users.urls')),
    path('',include('apps.valoraciones.urls')),
    path('',include('apps.entrenamientos.urls')),
    path('',include('apps.blog.urls')),
    path('',include('apps.chatbot.urls')),
    #path("__debug__/", include("debug_toolbar.urls")),
    
    
    ###SITEMAPS
    path('sitemap-palas.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# Configuración de las URL para los archivos multimedia
#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


