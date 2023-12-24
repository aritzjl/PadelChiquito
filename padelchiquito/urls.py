from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.comparador.urls')),
    path('',include('apps.users.urls')),
    path('',include('apps.valoraciones.urls')),
]

# Configuración de las URL para los archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)