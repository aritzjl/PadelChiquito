from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from openpyxl import Workbook
from .models import UserCreationForm, Verification,PassRecover, UserData
import uuid
from datetime import datetime
from .utils import *
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import random
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .utils import send_email_token, is_valid_email,send_recovery_mail


@login_required
def logout(request):
    django_logout(request)
    return redirect('comparador_pala')

def check_errors(user,mail,pass1,pass2):
    user2 = User.objects.filter(username = user)
    user3 = User.objects.filter(email=mail)
    if len(user2) != 0:
        return "Nombre no disponible."
    elif len(user) < 3:
        return "Nombre demasiado corto."
    elif len(pass1) < 6:
        return "Contraseña demasiado corta (mínimo 6 caracteres)."
        
    elif is_valid_email(mail) != True:
        return "Introduce un email real."
    elif len(user3) != 0:
        return "Ya existe una cuenta con este email."
    elif pass1 != pass2:
        return "Las contraseñas no coinciden."
    
    return None

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        surnames=request.POST["surnames"]
        # Obtener la fecha en el formato ingresado
        fecha = request.POST["fecha"].replace('/','-')
        email = request.POST["email"]
        
        try:
            # Convertir la fecha al formato YYYY-MM-DD
            formatted_fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            # Manejar un error si el formato no es válido
            return render(request, 'signup.html', {
                "form" : UserCreationForm,
                "error": "El formato de fecha es incorrecto.",
                "username": username,
                "email": email,
            })
        dni=request.POST["dni"]

        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        acepta_politica = request.POST.get("acepta_politica") == "1"
        if not acepta_politica:
            return render(request, 'signup.html', {
                "form" : UserCreationForm,
                "error":"Por favor, acepta nuestras politcas para poder crear una cuenta.",
                "username":username,
                "email":email,
            })
        desea_recibir_info = request.POST.get("desea_recibir_info") == "1"
        error = check_errors(username,email,password1,password2)
        if error:
            return render(request, 'signup.html', {
                "form" : UserCreationForm,
                "error":error,
                "username":username,
                "email":email,
            })
        # Genera un número aleatorio de 6 dígitos para el username
        random_username = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        # Crea un nuevo usuario con el email y contraseña proporcionados, usando el username aleatorio
        user = User.objects.create_user(username=random_username, email=request.POST["email"], password=request.POST['password1'])
        use = user
        user.save()
        verification_object = Verification(
            user = user,
            email_token = str(uuid.uuid4())
        )
        login(request, use)
        v = verification_object
        verification_object.save()
        send_email_token(email, v.email_token)

        create_userData(use,username,surnames,fecha,dni,desea_recibir_info)
        return render(request, "check_verification.html")
    else:
        return render(request, 'signup.html', {
            "form" : UserCreationForm,
        })
        

def create_userData(user,nombre,apellidos,fecha,dni,desea):
    usuario=UserData(user=user,nombre=nombre,apellidos=apellidos,fecha_nacimiento=fecha,dni=dni,acepta_politica=True,desea_recibir_info=desea)
    usuario.save()

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm
        })
    else:
        email = request.POST["email"]
        password = request.POST["password1"]
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        try:
            verificacion=Verification.objects.get(user=user)
            
            
            if verificacion.is_verified!=True:
                return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": "Verifica tu email, revisa tus correos."
            })
        except Exception as e:
            
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": "Verifica tu email, revisa tus correos."
            })

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect("comparador_pala")
        else:
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": "Usuario o contraseña incorrectos."
            })
        

            
        
def verify(request, token):
    try: 

        obj = Verification.objects.get(email_token = token)
    
        obj.is_verified = True
        obj.save()
        return redirect('comparador_pala')
    except Exception as e:
        return render(request,"verification_failed.html")
    
    

def olvidada(request):
    if request.method=='GET':
        return render(request,'olvidada.html')
    else:
        email = request.POST["email"]
        
        users = User.objects.filter(email=email)
        
        
        if len(users)<1:
            return render(request,'olvidada.html',{
                'error':'No existe ninguna cuenta con ese email.',
                'mail':email,
            })
        else:
            recover=PassRecover(
                user=users[0],
            )
            token = str(uuid.uuid4())
            recover.email_token=token  
            recover.save()
            

            send_recovery_mail(email, token)
            
            return render(request,'check_verification.html')
        
def changepassword(request,token):
    if request.method=='GET':
        return render(request,'changepass.html')
    else:
        recover = PassRecover.objects.get(email_token=token)
        if recover.active:
            user = recover.user
            password=request.POST['password']
            if len(password)>7:
                    user.set_password(password)
                    user.save()
                    # Optionally, you can mark the PassRecover instance as inactive after password change
                    recover.active = False
                    recover.save()
                    login(request, user)
                    return redirect("comparador_pala")
            else:
                return render(request,'changepass.html',{
                    'error':'La contraseña debe tener al menos 8 caracteres'
                })
                
                
@login_required
def exportar(request):
    """
    Genra un excel con los datos de los usuarios.
    Solo accesible para usuarios administradores.
    SI no es admin, redirige a la página principal.

    """
    
    user = request.user
    if not user.is_staff:
        return redirect('comparador_pala')
    
    datos_usuarios = []
    
    for user in User.objects.all():
        id = user.id
        username = user.username
        email = user.email
        fecha = user.date_joined.strftime("%d/%m/%Y")
        
        #Datos extra
        try:
            datos = UserData.objects.get(user=user)
            nombre = datos.nombre
            apellidos = datos.apellidos
            fecha_nacimiento = datos.fecha_nacimiento.strftime("%d/%m/%Y")
            dni = datos.dni
            acepta_politica = datos.acepta_politica
            desea_recibir_info = datos.desea_recibir_info
        except:
            nombre = ''
            apellidos = ''
            fecha_nacimiento = ''
            dni = ''
            acepta_politica = ''
            desea_recibir_info = ''
            
        datos_usuarios.append([id, username, email, fecha, nombre, apellidos, fecha_nacimiento, dni, acepta_politica, desea_recibir_info])
        
    # Crear el excel con openpyxl
    wb = Workbook()
    ws = wb.active
    ws.title = "Usuarios"
    
    # Cabecera
    ws.append(["ID", "Username", "Email", "Fecha de registro", "Nombre", "Apellidos", "Fecha de nacimiento", "DNI", "Acepta política", "Desea recibir info"])
    
    # Datos
    for datos in datos_usuarios:
        ws.append(datos)
        
    # Guardar el excel
    wb.save("usuarios.xlsx")
    
    # Enviar el excel para descarga
    with open("usuarios.xlsx", "rb") as excel:
        response = HttpResponse(excel.read())
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response['Content-Disposition'] = 'attachment; filename=usuarios.xlsx'
    
    return response