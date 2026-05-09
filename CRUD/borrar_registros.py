import os

def resetear_archivo_datos():
    ruta_data = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data'))
    ruta_archivo = os.path.join(ruta_data, 'clientes.txt')
    
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("{}") 
        print("✔ Base de datos reseteada con éxito.")
    except Exception as e:
        print(f"❌ Error al intentar resetear: {e}")