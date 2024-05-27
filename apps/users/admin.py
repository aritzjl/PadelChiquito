from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Verification,PassRecover,UserData
from django.contrib.auth.models import User

class UserDataAdmin(admin.ModelAdmin):
    pass
class VerificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Verification, VerificationAdmin)
admin.site.register(PassRecover)
admin.site.register(UserData, UserDataAdmin)
