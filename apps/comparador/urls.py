from django.urls import path
from . import views

urlpatterns = [
    path('', views.comparador_pala,name='comparador_pala'),
    path('mostrar_pala/<str:pk>/', views.mostrar_pala, name='mostrar_pala'),
    #path('randompalas/',views.crear_palas_aleatorias),
    path('mejores_palas_2024/', views.mejores_palas_2024, name='mejores_palas_2024'),
    path('mejores_palas_150/', views.mejores_palas_150, name='mejores_palas_150'),
    path('mejores_palas_ataque/', views.mejores_palas_ataque, name='mejores_palas_ataque'),
    path('mejores_palas_defensa/', views.mejores_palas_defensa, name='mejores_palas_defensa'),
    path('padelzoom/',views.subir_palas),
    path('subir-precio/',views.subir_precio),
    path('buscar/', views.buscar_pala, name='buscar_pala'),
    
]
