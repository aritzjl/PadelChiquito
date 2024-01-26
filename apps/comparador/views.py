from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Min
from .models import Pala, Tienda
from django.db.models import Subquery, OuterRef
import json
from .models import Pala, PrecioPala
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


# Create your views here.

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

        palas = Pala.objects.all()

        if forma != 'todas':
            palas = palas.filter(forma=forma)
        if dureza != 'todas':
            palas = palas.filter(tacto=dureza)
        if balance != 'todas':
            palas = palas.filter(balance=balance)
            
        if nivel != 'todas':
            palas = palas.filter(nivel=nivel)

        palas = palas.filter(
            precio__range=(precio_min, precio_max),
            potencia__range=(potencia_min, potencia_max),
            bandeja__range=(bandeja_min, bandeja_max),
            bajada_de_pared__range=(bajada_pared_min, bajada_pared_max),
            fondo_de_pista__range=(fondo_pista_min, fondo_pista_max),
            remate__range=(remate_min, remate_max),
            volea__range=(volea_min, volea_max),
        ).order_by('-puntuacion_total')

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
        }

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
    }
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
    }
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
    }
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

    return render(request, 'mostrar_pala.html', {
        'pala': pala,
        'precios_mas_recientes': precios_mas_recientes,
        'lowest':lowest,
        'isLower':isLower,
        'grafica_base64': grafica_base64,
        'palas_similares': palas_similares[:5],  # Mostrar las 5 palas más similares
        'valoracion_media': valoracion_media,
        'ha_valorado': ha_valorado,
        'comentarios': comentarios,
        'reviews':reviews,
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
        
        print(f'Ruta de la imagen guardada: {pala.imagen.path}')
        
        
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

    return render(request, 'comparador_pala.html', context)