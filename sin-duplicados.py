import pandas as pd

def eliminar_duplicados_por_nombre(csv_path):
    
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv_path)

    # Obtener los nombres duplicados
    nombres_duplicados = df[df.duplicated(subset=['nombre'], keep=False)]['nombre'].unique()

    # Eliminar duplicados basados en la columna 'nombre'
    df.drop_duplicates(subset=['nombre'], inplace=True)

    # Guardar el DataFrame sin duplicados en el mismo archivo CSV
    df.to_csv(csv_path, index=False)
    print(f"Duplicados eliminados del archivo {csv_path}")

    # Mostrar los nombres duplicados por consola
    if len(nombres_duplicados) > 0:
        print("\nNombres eliminados:")
        for nombre in nombres_duplicados:
            print(nombre)
    else:
        print("\nNo se encontraron nombres duplicados.")

# Ejemplo de uso
csv_path = 'Dia\productos-dia.csv'  # Ruta del archivo CSV
eliminar_duplicados_por_nombre(csv_path)