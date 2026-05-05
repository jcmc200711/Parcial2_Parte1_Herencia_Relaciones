from UI.limpiarPantalla import limpiar_pantalla

def menu_opciones(mensaje, alternativas):
     print(mensaje)   

     for alternativa in alternativas:
        print(alternativa)

     while True:
        opcion = input("Seleccione una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(alternativas):
                return opcion

        print("Ingrese una opción válida...\n")
        limpiar_pantalla()
