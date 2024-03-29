from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.comparador.urls')),
    path('',include('apps.users.urls')),
    path('',include('apps.valoraciones.urls')),
    path('',include('apps.entrenamientos.urls')),
    path('',include('apps.blog.urls')),
    #path("__debug__/", include("debug_toolbar.urls")),
]

# Configuración de las URL para los archivos multimedia
#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)