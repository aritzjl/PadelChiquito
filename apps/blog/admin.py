from django.contrib import admin
from .models import BlogPost, SeccionBlog, VisitaBlog

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(SeccionBlog)
admin.site.register(VisitaBlog)