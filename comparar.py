import json
import pandas as pd

def productos_no_en_csv(json_path, csv_path, output_path):
    # Cargar los datos del JSON con codificación utf-8
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Crear un conjunto de nombres de productos en el JSON
    productos_json = {producto['nombre'] for producto in json_data}
    
    # Cargar el CSV y crear un conjunto de nombres de productos
    csv_data = pd.read_csv(csv_path)
    productos_csv = set(csv_data['nombre'])
    
    # Encontrar productos que están en el JSON pero no en el CSV
    productos_faltantes = productos_json - productos_csv
    
    # Guardar los productos faltantes en un nuevo archivo CSV
    faltantes_df = pd.DataFrame(list(productos_faltantes), columns=['nombre'])
    faltantes_df.to_csv(output_path, index=False)
    print(f"Productos faltantes guardados en {output_path}")

# Ejemplo de uso
json_path = 'productos_dia.json'
csv_path = 'productos-dia.csv'
output_path = 'faltantes.csv'  # Nombre del nuevo archivo CSV
productos_no_en_csv(json_path, csv_path, output_path)
