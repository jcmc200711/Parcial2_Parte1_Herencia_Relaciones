import os
import ast

def guardar_o_actualizar_cliente(cedula, nombre, facturas_nuevas):
    """
    Guarda o actualiza un cliente. Si ya existe, anexa la nueva factura
    calculando automáticamente el siguiente ID disponible.
    """
    cedula = str(cedula)
    # Ajusta las rutas según tu estructura de carpetas
    ruta_data = os.path.join(os.path.dirname(__file__), '..', 'Data')
    ruta_archivo = os.path.join(ruta_data, 'clientes.txt')

    datos_clientes = {}

    # 1. INTENTAR LEER EL ARCHIVO EXISTENTE
    if os.path.exists(ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read().strip()
                if contenido:
                    datos_clientes = ast.literal_eval(contenido)
        except Exception as e:
            print(f"Aviso: No se pudo leer el historial previo ({e}). Se creará uno nuevo.")

    # 2. PROCESAR LA FACTURA NUEVA
    # Extraemos el contenido real (por si viene como {id: {datos}})
    if isinstance(facturas_nuevas, dict) and len(facturas_nuevas) > 0:
        # Tomamos el primer valor del diccionario que nos envían
        contenido_factura_real = list(facturas_nuevas.values())[0]
    else:
        # Si ya enviaron solo los datos, los usamos directamente
        contenido_factura_real = facturas_nuevas

    # 3. LÓGICA DE ACTUALIZACIÓN O CREACIÓN
    if cedula in datos_clientes:
        # El cliente ya existe, buscamos el siguiente número de factura
        facturas_historial = datos_clientes[cedula]['facturas']
        
        # Obtenemos todos los IDs actuales como números para hallar el mayor
        ids_existentes = [int(k) for k in facturas_historial.keys() if str(k).isdigit()]
        
        proximo_id = max(ids_existentes) + 1 if ids_existentes else 1
        nuevo_id_str = str(proximo_id)
        
        # Anexamos la factura con el nuevo ID correlativo
        datos_clientes[cedula]['facturas'][nuevo_id_str] = contenido_factura_real
        datos_clientes[cedula]['nombre'] = nombre # Actualizamos nombre por si acaso
    else:
        # El cliente es nuevo, empezamos con la factura "1"
        datos_clientes[cedula] = {
            'nombre': nombre,
            'facturas': {"1": contenido_factura_real}
        }

    # 4. GUARDAR EN EL ARCHIVO
    try:
        # Aseguramos que la carpeta Data existe
        if not os.path.exists(ruta_data):
            os.makedirs(ruta_data)
            
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            # repr() convierte el diccionario a string de forma segura para ast.literal_eval
            archivo.write(repr(datos_clientes))
        print(f"\n[OK] Compra registrada exitosamente para {nombre}.")
    except Exception as e:
        print(f"\n[ERROR] No se pudo escribir en el archivo: {e}")