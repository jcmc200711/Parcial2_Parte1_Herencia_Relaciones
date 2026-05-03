from Modelo.ClasesGenerales.Cliente import Cliente
from Modelo.ClasesGenerales.Factura import Factura
from Modelo.ClasesHijas.Fertilizantes import Fertilizante
from Modelo.ClasesHijas.ControlPlagas import ControlPlagas
from Modelo.ClasesHijas.AntibioticosBovinos import AntibioticoBovino
from Modelo.ClasesHijas.AntibioticosPorcinos import AntibioticoPorcino
from UI.limpiarPantalla import limpiar_pantalla
from UI.menu_opciones import menu_opciones
from UI.verificar_cadenas import verificar_cadenas

def ejecutar():
    print("Bienvenido a nuestro sistema de registro de productos de agricultura\n")

    mensaje_opciones_principales = "Cuál de las siguientes opciones desea elegir:\n"
    opciones_principales = ["1. Registrar un producto\n",
    "2. Realizar una compra\n",
    "3. Expedir su factura\n"]
    ##En esta funcion primero va el mensaje a mostrar, las opciones
    opcion_principal = menu_opciones(mensaje_opciones_principales,opciones_principales)
    
    if(opcion_principal == 1):    
        mensaje_producto = "¿Qué tipo de producto desea registrar?:\n"
        tipos_productos = ["1. Producto de Control.\n",
        "2. Antibiotico\n"]

        opcion_tipos_producto = menu_opciones(mensaje_producto, tipos_productos)
        
        if(opcion_tipos_producto == 1):
            nombre = verificar_cadenas("Ingrese el nombre del producto:\n")
            

    
    





