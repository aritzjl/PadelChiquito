from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Permission, User

class Verification(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

class UserCreationForm(UserCreationForm):
    email = models.EmailField(("Email address"), max_length=254)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

class UserData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    acepta_politica = models.BooleanField(default=False)
    desea_recibir_info = models.BooleanField(default=False)


class PassRecover(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    email_token=models.CharField(max_length=200)    


    
    

    

    
    

    
