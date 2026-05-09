import ast
import os

def buscar_por_cedula(cedula):
    ruta = os.path.join("Data", "clientes.txt")
    
    try:
        if not os.path.exists(ruta):
            return [], "Archivo no encontrado"

        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().strip()
            if not contenido or contenido == "":
                return [], "Archivo vacío"
            
            # Intentamos leer el diccionario
            mi_diccionario = ast.literal_eval(contenido)
            
            # Buscamos al cliente (asegurando que cedula sea string o int según guardaste)
            cliente = mi_diccionario.get(str(cedula)) or mi_diccionario.get(int(cedula))
            
            if cliente:
                # Retornamos los dos valores que espera el sistema
                return cliente.get('facturas', {}), cliente.get('nombre', "Sin nombre")
            
            return [], "Cliente no registrado"

    except Exception as e:
        # Si algo falla (como el SyntaxError o malformed node), avisamos y devolvemos 2 cosas
        print(f"Ocurrió un error al buscar: {e}")
        return [], "Error en base de datos" # <--- ESTO EVITA EL VALUEERROR