from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Min
from .models import Pala, Tienda
from django.db.models import Subquery, OuterRef
import re
import json
from .models import Pala, PrecioPala, Versus, Favorito
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import JsonResponse
from io import BytesIO
import base64
from django.db.models import Q
from apps.reviews.models import Review
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg  
from .models import PalaBuscada
from apps.valoraciones.models import Comentario,Estrella
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.contrib import messages
from .forms import UploadExcelForm

def inicio(request):
    top_10_2024 = Pala.objects.filter(temporada=2024).order_by('-puntuacion_total')[:10]
    top_10_ataque = Pala.objects.order_by('-potencia')[:10]
    top_10_defensa = Pala.objects.order_by('-control')[:10]
    for pala in Pala.objects.all():
        pala.update_total_favoritos()
    top_favoritas = Pala.objects.order_by('-total_favoritos')[:10]

    
    context = {
        'top_2024' : top_10_2024,
        'top_ataque' : top_10_ataque,
        'top_defensa' : top_10_defensa,
        'top_favoritas' : top_favoritas,
    }
    return render(request, 'home.html', context)


@login_required
def versus(request):
    usuario = request.user
    try:
        versus = Versus.object.get(usuario=usuario)
    except:
        versus = Versus(usuario=usuario)
        versus.save()
    palas = versus.palas.all()
    
    pala_peor_dureza = palas.order_by('tacto').first()
    pala_mejor_dureza = palas.order_by('-tacto').first()
    pala_peor_fondo = palas.order_by('fondo_de_pista').first()
    pala_mejor_fondo = palas.order_by('-fondo_de_pista').first()
    pala_peor_bajada = palas.order_by('bajada_de_pared').first()
    pala_mejor_bajada = palas.order_by('-bajada_de_pared').first()
    pala_peor_volea = palas.order_by('volea').first()
    pala_mejor_volea = palas.order_by('-volea').first()
    pala_peor_bandeja = palas.order_by('bandeja').first()
    pala_mejor_bandeja = palas.order_by('-bandeja').first()
    pala_peor_remate = palas.order_by('remate').first()
    pala_mejor_remate = palas.order_by('-remate').first()
    pala_peor_manejabilidad = palas.order_by('manejabilidad').first()
    pala_mejor_manejabilidad = palas.order_by('-manejabilidad').first()
    pala_peor_punto_dulce = palas.order_by('punto_dulce').first()
    pala_mejor_punto_dulce = palas.order_by('-punto_dulce').first()
    pala_peor_salida = palas.order_by('salida_bola').first()
    pala_mejor_salida = palas.order_by('-salida_bola').first()
    
    
    print(pala_mejor_remate)
    
    conext = {
        'palas': palas,
        'pala_peor_fondo': pala_peor_fondo,
        'pala_mejor_fondo': pala_mejor_fondo,
        'pala_peor_bajada': pala_peor_bajada,
        'pala_mejor_bajada': pala_mejor_bajada,
        'pala_peor_volea': pala_peor_volea,
        'pala_mejor_volea': pala_mejor_volea,
        'pala_peor_bandeja': pala_peor_bandeja,
        'pala_mejor_bandeja': pala_mejor_bandeja,
        'pala_peor_remate': pala_peor_remate,
        'pala_mejor_remate': pala_mejor_remate,
        'pala_peor_manejabilidad': pala_peor_manejabilidad,
        'pala_mejor_manejabilidad': pala_mejor_manejabilidad,
        'pala_peor_punto_dulce': pala_peor_punto_dulce,
        'pala_mejor_punto_dulce': pala_mejor_punto_dulce,
        'pala_peor_salida': pala_peor_salida,
        'pala_mejor_salida': pala_mejor_salida,
        
    }
    
    
    return render(request, 'versus.html', conext)

@login_required
def versus_quitar(request, idPala):
    usuario = request.user
    try:
        versus = Versus.objects.get(usuario=usuario)
        pala = Pala.objects.get(pk=idPala)
        versus.palas.remove(pala)
    except:
        pass
    return redirect('versus')


@login_required
def favoritos(request):
    usuario = request.user
    try:
        favorito = Favorito.objects.get(usuario=usuario)
    except:
        favorito = Favorito(usuario=usuario)
        favorito.save()
    palas = favorito.palas.all()
    return render(request, 'favoritos.html', {'palas': palas})



def versus_agregar(request, idPala):
    try:
        usuario = request.user
        if usuario.is_anonymous:
            return JsonResponse({'status': 'error', 'error': 'Debes iniciar sesión para agregar palas al comparador'})
        
        try:
            versus = Versus.objects.get(usuario=usuario)
        except Versus.DoesNotExist:
            versus = Versus(usuario=usuario)
            versus.save()
        
        try:
            pala = Pala.objects.get(pk=idPala)
        except Pala.DoesNotExist:
            return JsonResponse({'status': 'error', 'error': 'La pala no existe'})
        
        if pala in versus.palas.all():
            print(pala.nombre)
            return JsonResponse({'status': 'error', 'error': 'La pala ya está en el comparador'})
        
        if versus.palas.count() < 6:
            versus.palas.add(pala)
            return JsonResponse({'status': 'success', 'message': 'Pala agregada al comparador'})
        else:
            return JsonResponse({'status': 'error', 'error': 'No puedes agregar más de 6 palas al comparador'})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'error': f'Error al agregar la pala al comparador'})

    
    

def agregar_favorito(request, idPala):
    try:
        usuario = request.user
        if usuario.is_anonymous:
            return JsonResponse({'status': 'error', 'error': 'Debes iniciar sesión para agregar palas a favoritos'})
        
        try:
            favorito = Favorito.objects.get(usuario=usuario)
        except:
            favorito = Favorito(usuario=usuario)
            favorito.save()
            
        
        
        pala = Pala.objects.get(pk=idPala)
        
        
        if pala in favorito.palas.all():
            return JsonResponse({'status': 'error', 'error': 'La pala ya está en favoritos'})
        
        
        favorito.palas.add(pala)
        favorito.save()
        return JsonResponse({'status': 'success', 'message': 'Pala agregada a favoritos'})
    

    except Exception as e:
        print(str(e))
        return JsonResponse({'status': 'error', 'error': f'Error al agregar la pala a favoritos'})
    
@login_required
def quitar_favorito(request, idPala):
    usuario = request.user
    favorito = Favorito.objects.get(usuario=usuario)
    pala = Pala.objects.get(pk=idPala)
    pala.update_total_favoritos()
    favorito.palas.remove(pala)
    return redirect('favoritos')
    


# Create your views here.
def obtener_precio_mas_barato(pala):
    # Obtener el precio más reciente de cada tienda para esta pala
    tiendas = Tienda.objects.all()
    precios_mas_recientes = []
    for tienda in tiendas:
        precios_tienda = PrecioPala.objects.filter(pala=pala, tienda=tienda).order_by('-fecha')
        if precios_tienda.exists():
            precio_mas_reciente = precios_tienda.first()
            precios_mas_recientes.append(precio_mas_reciente)
    
    # Obtener el historial de precios para la gráfica
    historial_precios = PrecioPala.objects.filter(pala=pala).order_by('fecha')
    fechas = [precio.fecha.strftime('%Y-%m-%d') for precio in historial_precios]
    precios = [precio.precio for precio in historial_precios]
    lowest=pala.precio
    isLower=False
    
    for precio in precios_mas_recientes:
        if precio.precio<lowest:

            lowest=precio.precio
            isLower=True
            
    return lowest


def comparador_pala(request):
    if request.method == 'POST':
        forma = request.POST.get('forma')
        dureza = request.POST.get('dureza')
        balance = request.POST.get('balance')
        precio_min = request.POST.get('precio_min')
        precio_max = request.POST.get('precio_max')
        potencia_min = request.POST.get('potencia_min')
        potencia_max = request.POST.get('potencia_max')
        bandeja_min = request.POST.get('bandeja_min')
        bandeja_max = request.POST.get('bandeja_max')
        bajada_pared_min = request.POST.get('bajada_pared_min')
        bajada_pared_max = request.POST.get('bajada_pared_max')
        fondo_pista_min = request.POST.get('fondo_pista_min')
        fondo_pista_max = request.POST.get('fondo_pista_max')
        remate_min = request.POST.get('remate_min')
        remate_max = request.POST.get('remate_max')
        volea_min = request.POST.get('volea_min')
        volea_max = request.POST.get('volea_max')
        nivel=request.POST.get('nivel')
        
        orden = request.POST.get('orden')
        
    
        
        #Si algun valor no etá en el post, poneemos por defecto: todas, min 0, o max 99999
        if forma==None:
            forma="todas"
        if dureza==None:
            dureza="todas"
        if balance==None:
            balance="todas"
        if nivel==None:
            nivel="todas"
        
        if precio_min==None:
            precio_min=0
        if precio_max==None:
            precio_max=99999
        if potencia_min==None:
            potencia_min=0
        if potencia_max==None:
            potencia_max=99999
        if bandeja_min==None:
            bandeja_min=0
        if bandeja_max==None:
            bandeja_max=99999
        if bajada_pared_min==None:
            bajada_pared_min=0
        if bajada_pared_max==None:
            bajada_pared_max=99999
        if fondo_pista_min==None:
            fondo_pista_min=0
        if fondo_pista_max==None:
            fondo_pista_max=99999
        if remate_min==None:
            remate_min=0
        if remate_max==None:
            remate_max=99999
        if volea_min==None:
            volea_min=0
        if volea_max==None:
            volea_max=99999
            
            
        
        
        
        

        palas = Pala.objects.all()
        
        if forma != 'todas':
            palas = palas.filter(forma=forma.capitalize())
        if dureza != 'todas':
            tempDureza = ""
            tempDureza = " " + dureza.split("-")[0].capitalize()
            try:
                tempDureza = tempDureza + "-" + dureza.split("-")[1].capitalize()
            except:
                pass
            
    
            palas = palas.filter(tacto=tempDureza)
        if balance != 'todas':
            palas = palas.filter(balance=balance.capitalize())
            
        if nivel != 'todas':
            palas = palas.filter(nivel=nivel.capitalize())


        
        marcasSeleccionadas = request.POST.getlist('marcas')
        if marcasSeleccionadas:
            palas = palas.filter(marca__in=marcasSeleccionadas)
        
        
        palas = palas.filter(
            #(precio__range=(precio_min, precio_max)) |
            #Q(precio=obtener_precio_mas_barato(pala)),
            potencia__range=(potencia_min, potencia_max),
            bandeja__range=(bandeja_min, bandeja_max),
            bajada_de_pared__range=(bajada_pared_min, bajada_pared_max),
            fondo_de_pista__range=(fondo_pista_min, fondo_pista_max),
            remate__range=(remate_min, remate_max),
            volea__range=(volea_min, volea_max),
        )

        
        #Ordenamos
        if orden=="puntuacion":
            palas=palas.order_by('-puntuacion_total')
        elif orden == "control":
            palas=palas.order_by('-control')
        elif orden == "potencia":
            palas=palas.order_by('-potencia')
        elif orden == "precioMayorMenor":
            palas=palas.order_by('-precio')
        elif orden == "precioMenorMayor":
            palas=palas.order_by('precio')
        elif orden == "deseadas":
            for pala in palas:
                pala.update_total_favoritos()
            palas=palas.order_by('-total_favoritos')
        elif orden == 'descuento':
            for pala in palas:
                pala.get_porcentaje_desucento()
            palas = palas.order_by('-descuento')
        """
        elif orden == "descuento":
            palas=palas.order_by('-descuento')
        elif orden == "deseadas":
            palas=palas.order_by('-deseada')
        """
        
        
        palasfinal=[]
        for pala in palas:
            if(obtener_precio_mas_barato(pala)>float(precio_min)) and (obtener_precio_mas_barato(pala)<float(precio_max)):
                palasfinal.append(pala)
                

                
                
        palas=palasfinal

        formas = [
            ('diamante', 'Diamante'),
            ('redonda', 'Redonda'),
            ('hibrida', 'Híbrida'),
        ]
        balances = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
        ]
        tactos = [
            ('Blando', 'Blando'),
            ('Medio-Duro', 'Medio-Duro'),
            ('Duro', 'Duro'),
            ('Medio-Blando', 'Medio-Blando'),
            ('Medio', 'Medio'),
        ]
        niveles = [
            ('Principiante', 'Principiante'),
            ('Intermedio', 'Intermedio'),
            ('Avanzado', 'Avanzado'),
        ]
        precio_max=int(precio_max)+1
        
        

        
        marcas = []
        for pala in Pala.objects.all():
            if (pala.marca not in marcas) and pala.marca != None and pala.marca != "":
                marcas.append(pala.marca)
        
        context = {
            'formas': formas,
            'palas': palas,
            'balances':balances,
            'tactos':tactos,
            'niveles':niveles,
            'precio_max': precio_max,
           # 'precio_min': precio_min,
           'precio_min': 1,
            'potencia_max': potencia_max,
            'potencia_min': potencia_min,
            'bandeja_max': bandeja_max,
            'bandeja_min': bandeja_min,
            'bajada_pared_max': bajada_pared_max,
            'bajada_pared_min': bajada_pared_min,
            'fondo_pista_max': fondo_pista_max,
            'fondo_pista_min': fondo_pista_min,
            'remate_max': remate_max,
            'remate_min': remate_min,
            'volea_max': volea_max,
            'volea_min': volea_min,
            'forma_seleccionada': forma,  # Agrega la forma seleccionada al contexto
            'dureza_seleccionada': dureza,  # Agrega la dureza seleccionada al contexto
            'balance_seleccionado': balance,  # Agrega el balance seleccionado al contexto
            'filtro':True,
            'ordenSeleccionado' : orden,
            
            'marcas': marcas,
            'marcasSeleccionadas': marcasSeleccionadas
        }
        
        try:
            palasFavoritas = Favorito.objects.get(usuario=request.user).palas.all()
            context['palasFavoritas'] = palasFavoritas
        except:
            pass
        
        try:
            palasVersus = Versus.objects.get(usuario=request.user).palas.all()
            context['palasVersus'] = palasVersus
        except:
            pass

        return render(request, 'comparador_pala.html', context)

        
    else:
        # Obtener valores máximos y mínimos
        precio_max = Pala.objects.aggregate(Max('precio'))['precio__max']
        precio_min = Pala.objects.aggregate(Min('precio'))['precio__min']
        potencia_max = Pala.objects.aggregate(Max('potencia'))['potencia__max']
        potencia_min = Pala.objects.aggregate(Min('potencia'))['potencia__min']

        bandeja_max = Pala.objects.aggregate(Max('bandeja'))['bandeja__max']
        bandeja_min = Pala.objects.aggregate(Min('bandeja'))['bandeja__min']

        bajada_pared_max = Pala.objects.aggregate(Max('bajada_de_pared'))['bajada_de_pared__max']
        bajada_pared_min = Pala.objects.aggregate(Min('bajada_de_pared'))['bajada_de_pared__min']

        fondo_pista_max = Pala.objects.aggregate(Max('fondo_de_pista'))['fondo_de_pista__max']
        fondo_pista_min = Pala.objects.aggregate(Min('fondo_de_pista'))['fondo_de_pista__min']

        remate_max = Pala.objects.aggregate(Max('remate'))['remate__max']
        remate_min = Pala.objects.aggregate(Min('remate'))['remate__min']

        volea_max = Pala.objects.aggregate(Max('volea'))['volea__max']
        volea_min = Pala.objects.aggregate(Min('volea'))['volea__min']
        formas = [
            ('diamante', 'Diamante'),
            ('redonda', 'Redonda'),
            ('hibrida', 'Híbrida'),
        ]
        balances = [
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
        ]
        tactos = [
            ('Blando', 'Blando'),
            ('Medio-Duro', 'Medio-Duro'),
            ('Duro', 'Duro'),
            ('Medio-Blando', 'Medio-Blando'),
            ('Medio', 'Medio'),
        ]
        
        niveles = [
            ('Principiante', 'Principiante'),
            ('Intermedio', 'Intermedio'),
            ('Avanzado', 'Avanzado'),
        ]
        precio_max=int(precio_max)+1
        palas=Pala.objects.all().order_by('-puntuacion_total')
        marcas = []
        for pala in Pala.objects.all():
            if (pala.marca not in marcas) and pala.marca != None and pala.marca != "":
                marcas.append(pala.marca)

        context = {
            'formas': formas,
            'palas': palas,
            'balances':balances,
            'tactos':tactos,
            'niveles':niveles,
            'precio_max': precio_max,
            'precio_min': 0,
            'potencia_max': 10,
            'potencia_min': 0,
            'bandeja_max': 10,
            'bandeja_min': 0,
            'bajada_pared_max': 10,
            'bajada_pared_min': 0,
            'fondo_pista_max': 10,
            'fondo_pista_min': 0,
            'remate_max': 10,
            'remate_min': 0,
            'volea_max': 10,
            'volea_min': 0,
            'filtro':True,
            
            'marcas': marcas,

            
        }
        
        try:
            palasFavoritas = Favorito.objects.get(usuario=request.user).palas.all()
            context['palasFavoritas'] = palasFavoritas
        except:
            pass
        
        try:
            palasVersus = Versus.objects.get(usuario=request.user).palas.all()
            context['palasVersus'] = palasVersus
        except:
            pass

        return render(request, 'comparador_pala.html', context)

# Vista para las mejores palas del 2024
def mejores_palas_2024(request):
    top_10_2024 = Pala.objects.filter(temporada=2024).order_by('-puntuacion_total')[:30]
    # Obtener valores máximos y mínimos
    precio_max = Pala.objects.aggregate(Max('precio'))['precio__max']
    precio_min = Pala.objects.aggregate(Min('precio'))['precio__min']
    potencia_max = Pala.objects.aggregate(Max('potencia'))['potencia__max']
    potencia_min = Pala.objects.aggregate(Min('potencia'))['potencia__min']

    bandeja_max = Pala.objects.aggregate(Max('bandeja'))['bandeja__max']
    bandeja_min = Pala.objects.aggregate(Min('bandeja'))['bandeja__min']

    bajada_pared_max = Pala.objects.aggregate(Max('bajada_de_pared'))['bajada_de_pared__max']
    bajada_pared_min = Pala.objects.aggregate(Min('bajada_de_pared'))['bajada_de_pared__min']

    fondo_pista_max = Pala.objects.aggregate(Max('fondo_de_pista'))['fondo_de_pista__max']
    fondo_pista_min = Pala.objects.aggregate(Min('fondo_de_pista'))['fondo_de_pista__min']

    remate_max = Pala.objects.aggregate(Max('remate'))['remate__max']
    remate_min = Pala.objects.aggregate(Min('remate'))['remate__min']

    volea_max = Pala.objects.aggregate(Max('volea'))['volea__max']
    volea_min = Pala.objects.aggregate(Min('volea'))['volea__min']
    formas = [
        ('diamante', 'Diamante'),
        ('redonda', 'Redonda'),
        ('hibrida', 'Híbrida'),
    ]
    balances = [
    ('alto', 'Alto'),
    ('medio', 'Medio'),
    ('bajo', 'Bajo'),
    ]
    tactos = [
        ('Blando', 'Blando'),
        ('Medio-Duro', 'Medio-Duro'),
        ('Duro', 'Duro'),
        ('Medio-Blando', 'Medio-Blando'),
        ('Medio', 'Medio'),
    ]
    niveles = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    palas=top_10_2024
    marcas = []
    for pala in Pala.objects.all():
        if (pala.marca not in marcas) and pala.marca != None and pala.marca != "":
            marcas.append(pala.marca)

    context = {
        'formas': formas,
        'palas': palas,
        'balances':balances,
        'tactos':tactos,
        'niveles':niveles,
        'precio_max': precio_max,
        'precio_min': 1,
        #'precio_min': precio_min,
        'potencia_max': potencia_max,
        'potencia_min': potencia_min,
        'bandeja_max': bandeja_max,
        'bandeja_min': bandeja_min,
        'bajada_pared_max': bajada_pared_max,
        'bajada_pared_min': bajada_pared_min,
        'fondo_pista_max': fondo_pista_max,
        'fondo_pista_min': fondo_pista_min,
        'remate_max': remate_max,
        'remate_min': remate_min,
        'volea_max': volea_max,
        'volea_min': volea_min,
        'marcas': marcas,

    }
    try:
        palasFavoritas = Favorito.objects.get(usuario=request.user).palas.all()
        context['palasFavoritas'] = palasFavoritas
    except:
        pass
    
    try:
        palasVersus = Versus.objects.get(usuario=request.user).palas.all()
        context['palasVersus'] = palasVersus
    except:
        pass
    return render(request, 'comparador_pala.html', context)

# Vista para las mejores palas por precio menor a 150€
def mejores_palas_150(request):
    top_10_150 = Pala.objects.filter(precio__lt=150).order_by('-puntuacion_total')[:30]
    # Obtener valores máximos y mínimos
    precio_max = Pala.objects.aggregate(Max('precio'))['precio__max']
    precio_min = Pala.objects.aggregate(Min('precio'))['precio__min']
    potencia_max = Pala.objects.aggregate(Max('potencia'))['potencia__max']
    potencia_min = Pala.objects.aggregate(Min('potencia'))['potencia__min']

    bandeja_max = Pala.objects.aggregate(Max('bandeja'))['bandeja__max']
    bandeja_min = Pala.objects.aggregate(Min('bandeja'))['bandeja__min']

    bajada_pared_max = Pala.objects.aggregate(Max('bajada_de_pared'))['bajada_de_pared__max']
    bajada_pared_min = Pala.objects.aggregate(Min('bajada_de_pared'))['bajada_de_pared__min']

    fondo_pista_max = Pala.objects.aggregate(Max('fondo_de_pista'))['fondo_de_pista__max']
    fondo_pista_min = Pala.objects.aggregate(Min('fondo_de_pista'))['fondo_de_pista__min']

    remate_max = Pala.objects.aggregate(Max('remate'))['remate__max']
    remate_min = Pala.objects.aggregate(Min('remate'))['remate__min']

    volea_max = Pala.objects.aggregate(Max('volea'))['volea__max']
    volea_min = Pala.objects.aggregate(Min('volea'))['volea__min']
    formas = [
        ('diamante', 'Diamante'),
        ('redonda', 'Redonda'),
        ('hibrida', 'Híbrida'),
    ]
    balances = [
    ('alto', 'Alto'),
    ('medio', 'Medio'),
    ('bajo', 'Bajo'),
    ]
    tactos = [
        ('Blando', 'Blando'),
        ('Medio-Duro', 'Medio-Duro'),
        ('Duro', 'Duro'),
        ('Medio-Blando', 'Medio-Blando'),
        ('Medio', 'Medio'),
    ]
    niveles = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    palas=top_10_150
    
    context = {
        'formas': formas,
        'palas': palas,
        'balances':balances,
        'tactos':tactos,
        'precio_max': precio_max,
        'niveles':niveles,
       # 'precio_min': precio_min,
       'precio_min': 1,
        'potencia_max': potencia_max,
        'potencia_min': potencia_min,
        'bandeja_max': bandeja_max,
        'bandeja_min': bandeja_min,
        'bajada_pared_max': bajada_pared_max,
        'bajada_pared_min': bajada_pared_min,
        'fondo_pista_max': fondo_pista_max,
        'fondo_pista_min': fondo_pista_min,
        'remate_max': remate_max,
        'remate_min': remate_min,
        'volea_max': volea_max,
        'volea_min': volea_min,
    }
    return render(request, 'comparador_pala.html', context)

# Vista para las mejores palas de ataque
def mejores_palas_ataque(request):
    top_10_ataque = Pala.objects.order_by('-potencia')[:30]
    # Obtener valores máximos y mínimos
    precio_max = Pala.objects.aggregate(Max('precio'))['precio__max']
    precio_min = Pala.objects.aggregate(Min('precio'))['precio__min']
    potencia_max = Pala.objects.aggregate(Max('potencia'))['potencia__max']
    potencia_min = Pala.objects.aggregate(Min('potencia'))['potencia__min']

    bandeja_max = Pala.objects.aggregate(Max('bandeja'))['bandeja__max']
    bandeja_min = Pala.objects.aggregate(Min('bandeja'))['bandeja__min']

    bajada_pared_max = Pala.objects.aggregate(Max('bajada_de_pared'))['bajada_de_pared__max']
    bajada_pared_min = Pala.objects.aggregate(Min('bajada_de_pared'))['bajada_de_pared__min']

    fondo_pista_max = Pala.objects.aggregate(Max('fondo_de_pista'))['fondo_de_pista__max']
    fondo_pista_min = Pala.objects.aggregate(Min('fondo_de_pista'))['fondo_de_pista__min']

    remate_max = Pala.objects.aggregate(Max('remate'))['remate__max']
    remate_min = Pala.objects.aggregate(Min('remate'))['remate__min']

    volea_max = Pala.objects.aggregate(Max('volea'))['volea__max']
    volea_min = Pala.objects.aggregate(Min('volea'))['volea__min']
    formas = [
        ('diamante', 'Diamante'),
        ('redonda', 'Redonda'),
        ('hibrida', 'Híbrida'),
    ]
    balances = [
    ('alto', 'Alto'),
    ('medio', 'Medio'),
    ('bajo', 'Bajo'),
    ]
    tactos = [
        ('Blando', 'Blando'),
        ('Medio-Duro', 'Medio-Duro'),
        ('Duro', 'Duro'),
        ('Medio-Blando', 'Medio-Blando'),
        ('Medio', 'Medio'),
    ]
    niveles = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    palas=top_10_ataque
    marcas = []
    for pala in Pala.objects.all():
        if (pala.marca not in marcas) and pala.marca != None and pala.marca != "":
            marcas.append(pala.marca)
    context = {
        'formas': formas,
        'palas': palas,
        'balances':balances,
        'tactos':tactos,
        'precio_max': precio_max,
        'precio_min': 1,
        'niveles':niveles,
      #  'precio_min': precio_min,
        'potencia_max': potencia_max,
        'potencia_min': potencia_min,
        'bandeja_max': bandeja_max,
        'bandeja_min': bandeja_min,
        'bajada_pared_max': bajada_pared_max,
        'bajada_pared_min': bajada_pared_min,
        'fondo_pista_max': fondo_pista_max,
        'fondo_pista_min': fondo_pista_min,
        'remate_max': remate_max,
        'remate_min': remate_min,
        'volea_max': volea_max,
        'volea_min': volea_min,
        'marcas': marcas,
    }
    
    
    try:
        palasFavoritas = Favorito.objects.get(usuario=request.user).palas.all()
        context['palasFavoritas'] = palasFavoritas
    except:
        pass
    
    try:
        palasVersus = Versus.objects.get(usuario=request.user).palas.all()
        context['palasVersus'] = palasVersus
    except:
        pass    
    return render(request, 'comparador_pala.html', context)

# Vista para las mejores palas de defensa
def mejores_palas_defensa(request):
    top_10_defensa = Pala.objects.order_by('-control')[:30]

    # Obtener valores máximos y mínimos
    precio_max = Pala.objects.aggregate(Max('precio'))['precio__max']
    precio_min = Pala.objects.aggregate(Min('precio'))['precio__min']
    potencia_max = Pala.objects.aggregate(Max('potencia'))['potencia__max']
    potencia_min = Pala.objects.aggregate(Min('potencia'))['potencia__min']

    bandeja_max = Pala.objects.aggregate(Max('bandeja'))['bandeja__max']
    bandeja_min = Pala.objects.aggregate(Min('bandeja'))['bandeja__min']

    bajada_pared_max = Pala.objects.aggregate(Max('bajada_de_pared'))['bajada_de_pared__max']
    bajada_pared_min = Pala.objects.aggregate(Min('bajada_de_pared'))['bajada_de_pared__min']

    fondo_pista_max = Pala.objects.aggregate(Max('fondo_de_pista'))['fondo_de_pista__max']
    fondo_pista_min = Pala.objects.aggregate(Min('fondo_de_pista'))['fondo_de_pista__min']

    remate_max = Pala.objects.aggregate(Max('remate'))['remate__max']
    remate_min = Pala.objects.aggregate(Min('remate'))['remate__min']

    volea_max = Pala.objects.aggregate(Max('volea'))['volea__max']
    volea_min = Pala.objects.aggregate(Min('volea'))['volea__min']
    formas = [
        ('diamante', 'Diamante'),
        ('redonda', 'Redonda'),
        ('hibrida', 'Híbrida'),
    ]
    balances = [
    ('alto', 'Alto'),
    ('medio', 'Medio'),
    ('bajo', 'Bajo'),
    ]
    tactos = [
        ('Blando', 'Blando'),
        ('Medio-Duro', 'Medio-Duro'),
        ('Duro', 'Duro'),
        ('Medio-Blando', 'Medio-Blando'),
        ('Medio', 'Medio'),
    ]
    niveles = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    palas=top_10_defensa
    marcas = []
    for pala in Pala.objects.all():
        if (pala.marca not in marcas) and pala.marca != None and pala.marca != "":
            marcas.append(pala.marca)
    context = {
        'formas': formas,
        'palas': palas,
        'balances':balances,
        'niveles':niveles,
        'tactos':tactos,
        'precio_max': precio_max,
      #  'precio_min': precio_min,
      'precio_min': 1,
        'potencia_max': potencia_max,
        'potencia_min': potencia_min,
        'bandeja_max': bandeja_max,
        'bandeja_min': bandeja_min,
        'bajada_pared_max': bajada_pared_max,
        'bajada_pared_min': bajada_pared_min,
        'fondo_pista_max': fondo_pista_max,
        'fondo_pista_min': fondo_pista_min,
        'remate_max': remate_max,
        'remate_min': remate_min,
        'volea_max': volea_max,
        'volea_min': volea_min,
        'marcas': marcas,
    }
    
    
    try:
        palasFavoritas = Favorito.objects.get(usuario=request.user).palas.all()
        context['palasFavoritas'] = palasFavoritas
    except:
        pass
    
    try:
        palasVersus = Versus.objects.get(usuario=request.user).palas.all()
        context['palasVersus'] = palasVersus
    except:
        pass    
    return render(request, 'comparador_pala.html', context)

def mostrar_pala(request, pk):

    # Obtener la información detallada de la pala
    pala = Pala.objects.get(pk=pk)
    stats_actualesOld = [
        pala.potencia, pala.control, pala.salida_bola,
        pala.manejabilidad, pala.punto_dulce, pala.fondo_de_pista,
        pala.volea, pala.bajada_de_pared, pala.bandeja,
        pala.remate, pala.defensa, pala.ataque,
        pala.puntuacion_total
    ]
    stats_actuales=[]
    for stat in stats_actualesOld:
        if stat==None:
            stats_actuales.append(1)
        else:
            stats_actuales.append(stat)
    #print(stats_actuales)
    #print("test")
    comentarios = Comentario.objects.filter(pala=pala)
    palaBuscada=PalaBuscada(pala=pala)
    palaBuscada.save()
    # Calcular las palas similares
    palas_similares = Pala.objects.filter(~Q(pk=pala.pk))  # Excluir la pala actual

    palas_similares = sorted(palas_similares, key=lambda p: sum(
        ((getattr(p, field) or 1) - stat) ** 2 for field, stat in zip(
            ['potencia', 'control', 'salida_bola', 'manejabilidad', 'punto_dulce',
            'fondo_de_pista', 'volea', 'bajada_de_pared', 'bandeja', 'remate',
            'defensa', 'ataque', 'puntuacion_total'], stats_actuales
        )
    ))

    # Obtener el precio más reciente de cada tienda para esta pala
    tiendas = Tienda.objects.all()
    precios_mas_recientes = []
    for tienda in tiendas:
        precios_tienda = PrecioPala.objects.filter(pala=pala, tienda=tienda).order_by('-fecha')
        if precios_tienda.exists():
            precio_mas_reciente = precios_tienda.first()
            precios_mas_recientes.append(precio_mas_reciente)
    
    # Obtener el historial de precios para la gráfica
    historial_precios = PrecioPala.objects.filter(pala=pala).order_by('fecha')
    fechas = [precio.fecha.strftime('%Y-%m-%d') for precio in historial_precios]
    precios = [precio.precio for precio in historial_precios]
    lowest=pala.precio
    isLower=False
    
    for precio in precios_mas_recientes:
        if precio.precio<lowest:

            lowest=precio.precio
            isLower=True
            
    # Crear la gráfica con Matplotlib
    plt.figure(figsize=(8, 6), facecolor='none')

    # Modificar estilo de la gráfica
    plot = plt.plot(fechas, precios, marker='o', linestyle='-', color='#ccff00')
    plt.xticks(rotation=45, ha='right', fontsize=8) 
    
    # Eliminar títulos y ejes
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')


    # Eliminar el borde del gráfico
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)

    # Guardar la gráfica en un buffer de BytesIO y convertirla a base64 para mostrarla en HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    grafica_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

# Obtener la valoración media de la pala
    valoracion_media = Estrella.objects.filter(pala=pala).aggregate(Avg('valoracion'))['valoracion__avg']
    try:
        usuario_actual = request.user
        ha_valorado = Estrella.objects.filter(usuario=usuario_actual, pala=pala).exists()
    except:
        ha_valorado=False
    # Obtener comentarios principales (no respuestas)
    comentarios = Comentario.objects.filter(pala=pala, comentariorespondido=None)
    
    reviews=Review.objects.filter(pala=pala)
    ytURL="https://www.youtube.com/embed/AQUILAID?autoplay=1&origin=https://padelchiquito.com"
    def obtener_id_youtube(url):
        # Expresión regular para extraer el ID del video de YouTube
        patron = re.compile(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
        
        # Busca el patrón en la URL
        coincidencia = patron.search(url)
        
        if coincidencia:
            # Retorna el ID del video de YouTube
            return coincidencia.group(1)
        else:
            # Retorna None si no se encuentra el ID
            return None
    # Itera sobre las reviews y realiza el reemplazo de la URL de YouTube si es necesario
    for review in reviews:
        if review.plataforma == 'YOUTUBE':
            videoID=obtener_id_youtube(review.video_url)
            review.video_url = ytURL.replace("AQUILAID",videoID)

    
    return render(request, 'mostrar_pala.html', {
        'pala': pala,
        'precios_mas_recientes': precios_mas_recientes,
        'lowest': lowest,
        'isLower': isLower,
        'grafica_base64': grafica_base64,
        'palas_similares': palas_similares[:5],  # Mostrar las 5 palas más similares
        'valoracion_media': valoracion_media,
        'ha_valorado': ha_valorado,
        'comentarios': comentarios,
        'reviews': reviews,
    })

@csrf_exempt
def subir_precio(request):
    if request.method == 'POST':
        nombre=request.POST.get('nombre_pala')
        precio=request.POST.get('precio_mas_bajo').replace(',','.')
        tiendaNombre=request.POST.get('tienda')
        tienda=Tienda.objects.get(nombre=tiendaNombre)
        pala=Pala.objects.get(nombre=nombre)
        
        newPrecio=PrecioPala(pala=pala,tienda=tienda,precio=float(precio))
        newPrecio.save()
        
    else:
        palas=Pala.objects.all()
        nombres=[]
        for pala in palas:
            nombres.append(pala.nombre)
            
        return JsonResponse({'nombres': nombres})
        
    


@csrf_exempt
def subir_palas(request):
    if request.method == 'POST':
        # Obtener la información de la pala enviada
        marca = request.POST.get('Marca')
        nombre = request.POST.get('Nombre')
        precio = float(request.POST.get('Precio PVP'))
        precio_rebaja = float(request.POST.get('Precio Rebajado'))
        temporada = int(request.POST.get('Temporada'))
        material_marco = request.POST.get('Material Marco')
        material_plano = request.POST.get('Material Plano')
        material_goma = request.POST.get('Material Goma')
        tacto = request.POST.get('Tacto')
        forma = request.POST.get('Forma')
        peso = request.POST.get('Peso')
        total_padelzoom = float(request.POST.get('Total PadelZoom'))
        potencia = float(request.POST.get('Potencia'))
        control = float(request.POST.get('Control'))
        salida_bola = float(request.POST.get('Salida Bola'))
        manejabilidad = float(request.POST.get('Manejabilidad'))
        punto_dulce = float(request.POST.get('Punto Dulce'))
        fondo_de_pista = float(request.POST.get('Fondo de Pista'))
        volea = float(request.POST.get('Volea'))
        bajada_de_pared = float(request.POST.get('Bajada de Pared'))
        bandeja = float(request.POST.get('Bandeja'))
        remate = float(request.POST.get('Remate'))
        defensa = float(request.POST.get('Defensa'))
        ataque = float(request.POST.get('Ataque'))
        puntuacion_total = float(request.POST.get('Puntuación Total'))
        balance = request.POST.get('Balance')

        # Obtener la imagen enviada
        imagen_pala = request.FILES['image']

        # Crear una instancia de Pala con los datos recibidos
        pala = Pala(
            nombre=nombre,
            imagen=imagen_pala,
            marca=marca,
            precio=precio,
            precio_rebaja=precio_rebaja,
            temporada=temporada,
            material_marco=material_marco,
            material_plano=material_plano,
            material_goma=material_goma,
            tacto=tacto,
            forma=forma,
            peso=peso,
            total_padelzoom=total_padelzoom,
            potencia=potencia,
            control=control,
            salida_bola=salida_bola,
            manejabilidad=manejabilidad,
            punto_dulce=punto_dulce,
            fondo_de_pista=fondo_de_pista,
            volea=volea,
            bajada_de_pared=bajada_de_pared,
            bandeja=bandeja,
            remate=remate,
            defensa=defensa,
            ataque=ataque,
            puntuacion_total=puntuacion_total,
            balance=balance
            # Agrega cualquier otro campo que sea necesario
        )

        # Guardar la pala en la base de datos
        pala.save()
        
        #print(f'Ruta de la imagen guardada: {pala.imagen.path}')
        
        
def buscar_pala(request):
    busqueda = request.GET.get('q', '') 

    precio_max = Pala.objects.aggregate(Max('precio'))['precio__max']
    precio_min = Pala.objects.aggregate(Min('precio'))['precio__min']
    potencia_max = Pala.objects.aggregate(Max('potencia'))['potencia__max']
    potencia_min = Pala.objects.aggregate(Min('potencia'))['potencia__min']

    bandeja_max = Pala.objects.aggregate(Max('bandeja'))['bandeja__max']
    bandeja_min = Pala.objects.aggregate(Min('bandeja'))['bandeja__min']

    bajada_pared_max = Pala.objects.aggregate(Max('bajada_de_pared'))['bajada_de_pared__max']
    bajada_pared_min = Pala.objects.aggregate(Min('bajada_de_pared'))['bajada_de_pared__min']

    fondo_pista_max = Pala.objects.aggregate(Max('fondo_de_pista'))['fondo_de_pista__max']
    fondo_pista_min = Pala.objects.aggregate(Min('fondo_de_pista'))['fondo_de_pista__min']

    remate_max = Pala.objects.aggregate(Max('remate'))['remate__max']
    remate_min = Pala.objects.aggregate(Min('remate'))['remate__min']

    volea_max = Pala.objects.aggregate(Max('volea'))['volea__max']
    volea_min = Pala.objects.aggregate(Min('volea'))['volea__min']
    formas = [
        ('diamante', 'Diamante'),
        ('redonda', 'Redonda'),
        ('hibrida', 'Híbrida'),
    ]
    balances = [
    ('alto', 'Alto'),
    ('medio', 'Medio'),
    ('bajo', 'Bajo'),
    ]
    tactos = [
        ('Blando', 'Blando'),
        ('Medio-Duro', 'Medio-Duro'),
        ('Duro', 'Duro'),
        ('Medio-Blando', 'Medio-Blando'),
        ('Medio', 'Medio'),
    ]
    
    niveles = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    precio_max=int(precio_max)+1
    palas = Pala.objects.filter(nombre__icontains=busqueda).order_by('-puntuacion_total')
    context = {
        'formas': formas,
        'palas': palas,
        'balances':balances,
        'tactos':tactos,
        'niveles':niveles,
        'precio_max': precio_max,
        'precio_min': 0,
        'potencia_max': 10,
        'potencia_min': 0,
        'bandeja_max': 10,
        'bandeja_min': 0,
        'bajada_pared_max': 10,
        'bajada_pared_min': 0,
        'fondo_pista_max': 10,
        'fondo_pista_min': 0,
        'remate_max': 10,
        'remate_min': 0,
        'volea_max': 10,
        'volea_min': 0,
        'filtro':True,
    }
    try:
        palasFavoritas = Favorito.objects.get(usuario=request.user).palas.all()
        context['palasFavoritas'] = palasFavoritas
    except:
        pass
    
    try:
        palasVersus = Versus.objects.get(usuario=request.user).palas.all()
        context['palasVersus'] = palasVersus
    except:
        pass
    return render(request, 'comparador_pala.html', context)


def obtener_palas_y_precios(request):
    palas = Pala.objects.all()
    data = []
    for pala in palas:
        precios = PrecioPala.objects.filter(pala=pala)
        precios_data = []
        for precio in precios:
            precios_data.append({
                'tienda': precio.tienda.nombre,
                'precio': precio.precio
            })
        pala_data = {
            'palaID': pala.palaID,
            'nombre': pala.nombre,
            'imagen': str(pala.imagen),
            'marca': pala.marca,
            'precio': pala.precio,
            'precio_rebaja': pala.precio_rebaja,
            'temporada': pala.temporada,
            'material_marco': pala.material_marco,
            'material_plano': pala.material_plano,
            'material_goma': pala.material_goma,
            'tacto': pala.tacto,
            'forma': pala.forma,
            'peso': pala.peso,
            'balance': pala.balance,
            'nivel': pala.nivel,
            'precios': precios_data
        }
        data.append(pala_data)
    return JsonResponse(data, safe=False)

@login_required
def upload_excel(request):
    user = request.user
    if not user.is_staff:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UploadExcelForm(request.POST, request.FILES)
            if form.is_valid():
                excel_file = request.FILES['excel_file']
                df = pd.read_excel(excel_file)

                for index, row in df.iterrows():
                    Pala.objects.create(
                        nombre=row['nombre'],
                        marca=row['marca'],
                        precio=row['precio'],
                        temporada=row['temporada'],
                        material_marco=row['material_marco'],
                        material_plano=row['material_plano'],
                        material_goma=row['material_goma'],
                        tacto=row['tacto'],
                        forma=row['forma'],
                        peso=row['peso'],
                        potencia=row['potencia'],
                        control=row['control'],
                        salida_bola=row['salida_bola'],
                        punto_dulce=row['punto_dulce'],
                        fondo_de_pista=row['fondo_de_pista'],
                        volea=row['volea'],
                        bajada_de_pared=row['bajada_de_pared'],
                        bandeja=row['bandeja'],
                        remate=row['remate'],
                        defensa=row['defensa'],
                        ataque=row['ataque'],
                        puntuacion_total=row['puntuacion_total'],
                        balance=row['balance'],
                        nivel=row['nivel'],
                    )
                messages.success(request, 'Las palas se han cargado correctamente.')
                return redirect('upload_excel')
        else:
            form = UploadExcelForm()
        return render(request, 'upload_excel.html', {'form': form})
