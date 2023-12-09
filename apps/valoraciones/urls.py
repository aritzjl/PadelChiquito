from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('pala/<int:pala_id>/comentar/', views.comentar_pala, name='comentar_pala'),
    path('pala/<int:pala_id>/valorar/', views.valorar_pala, name='valorar_pala'),
]
