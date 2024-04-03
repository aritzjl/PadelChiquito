from django.urls import path
from . import views

urlpatterns = [
    path('', views.comparador_pala,name='comparador_pala'),
    path('mostrar-pala/<str:pk>/', views.mostrar_pala, name='mostrar_pala'),
    #path('randompalas/',views.crear_palas_aleatorias),
    path('mejores-palas-2024/', views.mejores_palas_2024, name='mejores_palas_2024'),
    path('mejores-palas-150/', views.mejores_palas_150, name='mejores_palas_150'),
    path('mejores_palas-ataque/', views.mejores_palas_ataque, name='mejores_palas_ataque'),
    path('mejores_palas-defensa/', views.mejores_palas_defensa, name='mejores_palas_defensa'),
    path('padelzoom/',views.subir_palas),
    path('subir-precio/',views.subir_precio),
    path('buscar/', views.buscar_pala, name='buscar_pala'),
    path('palas-y-precios/', views.obtener_palas_y_precios, name='obtener_palas_y_precios'),
    
]
