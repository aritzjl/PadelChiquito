from django.shortcuts import render
from .models import Entrenamiento


# Create your views here.


def entrenamientos(reuqest):
    entrenamientos = Entrenamiento.objects.all()
    return render(reuqest, 'entrenamientos.html', {'entrenamientos': entrenamientos})