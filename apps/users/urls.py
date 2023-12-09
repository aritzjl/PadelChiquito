from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.signup, name = "signup" ),
    path('verify/<str:token>/', views.verify),
    path('signin/',views.signin,name = "signin"),
    path('recover/',views.olvidada),
    path('change-password/<str:token>',views.changepassword),
]
