from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('versus/', views.versus,name='versus'),
    path('quitar-pala-versus/<int:idPala>/',views.versus_quitar,name='versus_quitar'),
    path('agregar-pala-versus/<int:idPala>/',views.versus_agregar,name='versus_agregar'),
    
    path('favoritos/', views.favoritos,name='favoritos'),
    path('agregar-pala-favorito/<int:idPala>/',views.agregar_favorito,name='agregar_favorito'),
    path('quitar-pala-favorito/<int:idPala>/',views.quitar_favorito,name='quitar_favorito'),
    
    path('filtros/', views.comparador_pala,name='comparador_pala'),
    path('mostrar-pala/<str:pk>/', views.mostrar_pala, name='mostrar_pala'),
    #path('randompalas/',views.crear_palas_aleatorias),
    path('mejores-palas-2024/', views.mejores_palas_2024, name='mejores_palas_2024'),
    path('mejores-palas-150/', views.mejores_palas_150, name='mejores_palas_150'),
    path('mejores-palas-ataque/', views.mejores_palas_ataque, name='mejores_palas_ataque'),
    path('mejores-palas-defensa/', views.mejores_palas_defensa, name='mejores_palas_defensa'),
    path('padelzoom/',views.subir_palas),
    path('subir-precio/',views.subir_precio),
    path('buscar/', views.buscar_pala, name='buscar_pala'),
    path('palas-y-precios/', views.obtener_palas_y_precios, name='obtener_palas_y_precios'),
    path('importar-excel/', views.upload_excel, name='upload_excel'),
    
]
