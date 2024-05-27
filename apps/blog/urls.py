from django.urls import path
from . import views

urlpatterns = [
   path('blog/<int:idBlog>',views.blog,name = 'blog'),
   path('blogs/',views.blogs,name = 'blogs'),
]
