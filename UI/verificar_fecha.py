from datetime import datetime
from UI.limpiarPantalla import limpiar_pantalla

def verificar_fecha(mensaje):
    while True:
        fecha_str = input(mensaje + " (formato DD/MM/AAAA): ")
        try:
            fecha_objeto = datetime.strptime(fecha_str, "%d/%m/%Y")
            
            
            return fecha_objeto.strftime("%d/%m/%Y")
            
        except ValueError:
            print("\nError: Fecha inválida o formato incorrecto.")
            print("Asegúrese de usar el formato día/mes/año (ej: 15/05/2024)\n")
            
            input("Presione Enter para intentar de nuevo...")
            limpiar_pantalla()
