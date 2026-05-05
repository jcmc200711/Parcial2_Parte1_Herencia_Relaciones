from limpiarPantalla import limpiar_pantalla
def menu_opciones(mensaje,alternativas):
    for alternativa in alternativas : print(alternativa)
    while(True):
        opcion = input(mensaje)
        if(opcion.isdigit() and (opcion >= 1 and opcion <= len(alternativas))):
            opcion = int(opcion)
            break
        else:
            print("Ingrese una opción válida...\n")
            limpiar_pantalla()
    return opcion