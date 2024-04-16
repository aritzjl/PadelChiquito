from django.contrib import admin
from .models import BlogPost, SeccionBlog

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(SeccionBlog)