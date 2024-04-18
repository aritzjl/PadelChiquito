from django.shortcuts import render
from .models import BlogPost
# Create your views here.
def blog(request,idBlog):
    
    blog = BlogPost.objects.get(pk=idBlog)    
        
    return render(request,'blog.html',{'blog':blog})


def blogs(request):
    
    blogs = BlogPost.objects.all().order_by('-fecha')
    return render(request,'blogs.html',{'blogs':blogs})