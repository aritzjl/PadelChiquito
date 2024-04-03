from django.urls import path
from . import views

urlpatterns = [
    path('message-to-bot/', views.message_bot,name='message_bot'),
    
]
