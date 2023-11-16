from django.shortcuts import render
from django.db.models import Max, Min
from .models import Pala
from .models import Pala, PrecioPala
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random
from faker import Faker


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

        palas = Pala.objects.all()

        if forma != 'todas':
            palas = palas.filter(forma=forma)
        if dureza != 'todas':
            palas = palas.filter(dureza=dureza)
        if balance != 'todas':
            palas = palas.filter(balance=balance)

        palas = palas.filter(
            precio__range=(precio_min, precio_max),
            potencia__range=(potencia_min, potencia_max),
            bandeja__range=(bandeja_min, bandeja_max),
            bajada_de_pared__range=(bajada_pared_min, bajada_pared_max),
            fondo_de_pista__range=(fondo_pista_min, fondo_pista_max),
            remate__range=(remate_min, remate_max),
            volea__range=(volea_min, volea_max),
        )

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
        context = {
            'formas': formas,
            'palas': palas,
            'balances':balances,
            'tactos':tactos,
            'precio_max': precio_max,
            'precio_min': precio_min,
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
        palas=Pala.objects.all()
        context = {
            'formas': formas,
            'palas': palas,
            'balances':balances,
            'tactos':tactos,
            'precio_max': precio_max,
            'precio_min': precio_min,
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
    palas=Pala.objects.all()
    print(pk)
    for pala in palas:
        print(pala.pk)
    # Obtener la información detallada de la pala
    pala = Pala.objects.get(pk=pk)
    
    # Obtener el precio más reciente de cada tienda para esta pala
    tiendas = pala.tienda_set.all()
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
    
    # Crear la gráfica con matplotlib
    plt.figure(figsize=(8, 6))
    plt.plot(fechas, precios, marker='o', linestyle='-')
    plt.title('Historial de precios')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar la gráfica en un buffer de BytesIO y convertirla a base64 para mostrarla en HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafica_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    return render(request, 'mostrar_pala.html', {
        'pala': pala,
        'precios_mas_recientes': precios_mas_recientes,
        'grafica_base64': grafica_base64,
    })



fake = Faker()

def crear_palas_aleatorias(request):
    for _ in range(10):
        pala = Pala.objects.create(
            nombre=fake.word(),  # Genera una palabra aleatoria
            marca=fake.company(),  # Genera un nombre de compañía aleatorio
            precio=random.uniform(50, 300),  # Genera un precio aleatorio entre 50 y 300
            precio_rebaja=random.uniform(40, 250),  # Genera un precio de rebaja aleatorio
            temporada=random.randint(2010, 2023),  # Genera un año de temporada aleatorio entre 2010 y 2023
            material_marco=fake.word(),
            material_plano=fake.word(),
            material_goma=fake.word(),
            tacto=random.choice(['Blando', 'Medio-Duro', 'Duro', 'Medio-Blando', 'Medio']),  # Elige un tacto aleatorio
            forma=random.choice(['diamante', 'redonda', 'hibrida']),  # Elige una forma aleatoria
            peso=fake.word(),  # Genera una cadena aleatoria para el peso
            total_padelzoom=random.uniform(1, 10),  # Genera valores aleatorios entre 1 y 10 para las características
            potencia=random.uniform(1, 10),
            control=random.uniform(1, 10),
            salida_bola=random.uniform(1, 10),
            manejabilidad=random.uniform(1, 10),
            punto_dulce=random.uniform(1, 10),
            fondo_de_pista=random.uniform(1, 10),
            volea=random.uniform(1, 10),
            bajada_de_pared=random.uniform(1, 10),
            bandeja=random.uniform(1, 10),
            remate=random.uniform(1, 10),
            defensa=random.uniform(1, 10),
            ataque=random.uniform(1, 10),
            puntuacion_total=random.uniform(1, 10),
            balance=random.choice(['alto', 'medio', 'bajo'])  # Elige un balance aleatorio
        )
        pala.save()
