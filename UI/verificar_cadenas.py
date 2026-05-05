from UI.limpiarPantalla import limpiar_pantalla

def verificar_cadenas(mensaje):
    while(True):
        cadena = input(mensaje)
        if(isinstance(cadena,str) and len(cadena) > 0):
            break
        else:
            print("Ingrese una opción válida...\n")
            limpiar_pantalla()
    return cadena
