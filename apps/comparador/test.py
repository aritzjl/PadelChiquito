import pandas as pd
from comparador.models import Pala

def cargar_palas_desde_excel(ruta_excel):
    # Cargar el archivo Excel en un DataFrame
    df = pd.read_excel(ruta_excel)

    # Iterar sobre las filas del DataFrame y crear instancias de Pala
    for _, fila in df.iterrows():
        Pala.objects.create(
            nombre=fila['Nombre'],
            imagen=fila['Imagen URL'],
            marca=fila['Marca'],
            precio=fila['Precio PVP'],
            precio_rebaja=fila['Precio Rebajado'],
            temporada=fila['Temporada'],
            material_marco=fila['Material Marco'],
            material_plano=fila['Material Plano'],
            material_goma=fila['Material Goma'],
            tacto=fila['Tacto'],
            forma=fila['Forma'],
            peso=fila['Peso'],
            total_padelzoom=fila['Total PadelZoom'],
            potencia=fila['Potencia'],
            control=fila['Control'],
            salida_bola=fila['Salida Bola'],
            manejabilidad=fila['Manejabilidad'],
            punto_dulce=fila['Punto Dulce'],
            fondo_de_pista=fila['Fondo de Pista'],
            volea=fila['Volea'],
            bajada_de_pared=fila['Bajada de Pared'],
            bandeja=fila['Bandeja'],
            remate=fila['Remate'],
            defensa=fila['Defensa'],
            ataque=fila['Ataque'],
            puntuacion_total=fila['Puntuación Total'],
            balance=fila['Balance']
        )

# Llamada a la función con la ruta de tu archivo Excel
ruta_excel = './palas_data_actualizado.xlsx'
cargar_palas_desde_excel(ruta_excel)
