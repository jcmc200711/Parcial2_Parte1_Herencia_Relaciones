from limpiarPantalla import limpiar_pantalla

def verificar_valores_numericos(mensaje):
    while(True):
        numero = input(mensaje)
        if(numero.isdigit() and len(int(numero)) > 0):
            break
        else:
            print("Ingrese una opción válida...\n")
            limpiar_pantalla()
    return int(numero)