from django.shortcuts import render
from .models import Entrenamiento, Categoria


# Create your views here.


def entrenamientos(request):
    if request.method=='GET':
        entrenamientos = Entrenamiento.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'entrenamientos.html', {'entrenamientos': entrenamientos, 'categorias': categorias, 'categoriaSeleccionada':'todas'})
    else:
        categoriaID = None
        categoria = request.POST['categoria']
        if categoria.lower() == 'todas':
            entrenamientos = Entrenamiento.objects.all()
        else:
            categoriaID = int(categoria)
            for categoria in Categoria.objects.all():
                if categoria.id == categoriaID:
                    entrenamientos = categoria.entrenamientos.all()
                    break
        categorias = Categoria.objects.all()
        context= {'entrenamientos': entrenamientos, 'categorias': categorias, 'categoriaSeleccionada':'todas'}
        if categoriaID != None:
            context['categoriaSeleccionada'] = categoriaID
            
        return render(request, 'entrenamientos.html',context)
        
        