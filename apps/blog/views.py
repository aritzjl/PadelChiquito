from django.shortcuts import render
from .models import BlogPost
from .models import Categoria
# Create your views here.
def blog(request,idBlog):
    
    blog = BlogPost.objects.get(pk=idBlog)    
    return render(request,'blog.html',{'blog':blog})


def blogs(request):
    categorias = Categoria.objects.all()
    if request.method == "GET":
        blogs = BlogPost.objects.all().order_by('-fecha')
        return render(request,'blogs.html',{'blogs':blogs,'categorias':categorias})
    else:
        categoria = request.POST['categoria']
        if categoria!="todas":
            blogs = BlogPost.objects.filter(categorias__pk=categoria).order_by('-fecha')
        else:
            blogs = BlogPost.objects.all().order_by('-fecha')
        return render(request,'blogs.html',{'blogs':blogs,'categorias':categorias,'categoriaSeleccionada':categoria})