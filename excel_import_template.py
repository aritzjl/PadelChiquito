import pandas as pd

# Define the columns
columns = [
    'nombre', 'marca', 'precio', 'temporada', 'material_marco', 'material_plano',
    'material_goma', 'tacto', 'forma', 'peso', 'potencia', 'control', 'salida_bola',
    'punto_dulce', 'fondo_de_pista', 'volea', 'bajada_de_pared', 'bandeja',
    'remate', 'defensa', 'ataque', 'puntuacion_total', 'balance', 'nivel'
]

# Create an empty DataFrame with the defined columns
df = pd.DataFrame(columns=columns)

# Save the DataFrame to an Excel file
df.to_excel('import_template.xlsx', index=False)
