from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class BlogPost(models.Model):
    titulo = models.CharField(max_length=100)
    portada = models.ImageField(upload_to='blog/', null=False, blank=False)
    #contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    secciones = models.ManyToManyField('SeccionBlog')

    def __str__(self):
        return self.titulo
    
class SeccionBlog(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='blog/', null=True, blank=True)
    
    
    def __str__(self):
        return self.titulo
    
