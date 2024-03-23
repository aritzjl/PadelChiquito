from django.urls import path
from . import views

urlpatterns = [
    path('entrenamientos/', views.entrenamientos,name='entrenamientos'),
]
