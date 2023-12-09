from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.comparador.urls')),
    path('',include('apps.users.urls')),
    path('',include('apps.valoraciones.urls')),
]