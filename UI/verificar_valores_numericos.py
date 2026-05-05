from UI.limpiarPantalla import limpiar_pantalla

def verificar_valores_numericos(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            return int(numero)
        else:
            print("Ingrese un número válido\n")
            limpiar_pantalla()
