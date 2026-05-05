from Modelo.ClasesGenerales.Cliente import Cliente
from Modelo.ClasesGenerales.Factura import Factura
from Modelo.ClasesHijas.Fertilizantes import Fertilizante
from Modelo.ClasesHijas.ControlPlagas import ControlPlagas
from Modelo.ClasesHijas.AntibioticosBovinos import AntibioticoBovino
from Modelo.ClasesHijas.AntibioticosPorcinos import AntibioticoPorcino
from UI.limpiarPantalla import limpiar_pantalla
from UI.menu_opciones import menu_opciones
from UI.verificar_cadenas import verificar_cadenas
from UI.verificar_valores_numericos import verificar_valores_numericos
from UI.verificar_fecha import verificar_fecha

class Sistema:
    __productos = 0
    def __init__(self):
        self.productos = {'productos_control':{'plagas': {},'fertilizantes':{}},'antibioticos':{'porcinos': {},'bovinos':{}}}
        self.clientes = {}

    def agregar_cliente(self, cliente):
        self.clientes[cliente.cedula] = cliente

    
    def _imprimir_subcategorias(self, nombre_cat, subcats):
        print(f"Categoría: {nombre_cat}")
        for nombre_sub, productos in subcats.items():
            print(f"  [{nombre_sub}]: {len(productos)} artículos registrados.")
    
    def mostrar_productos(self):
        for nombre_cat, subcats in self.productos.items():
            self._imprimir_subcategorias(nombre_cat, subcats)
    
    def buscar_producto_por_id(self,id):
        # Recorremos el primer nivel: productos_control, antibioticos...
        for subcategorias in self.productos.items():
            # Recorremos el segundo nivel: Plagas, Fertilizantes, Porcinos...
            for  inventario in subcategorias.items():
            
            # El operador 'in' en un diccionario busca directamente en las LLAVES
                if id in inventario:
                    producto = inventario[id]
                    return producto
        print("\n[!] El id no coincide con ningún producto.")
        return None
    
    def ejecutar(self):    
        while(True):
            print("Bienvenido a nuestro sistema de registro de productos de agricultura\n")
            mensaje_opciones_principales = "Cuál de las siguientes opciones desea elegir:\n"
            opciones_principales = ["1. Registrar un producto\n",
            "2. Realizar una compra\n",
            "3. Expedir su factura\n", "4. Salir\n"]

            ##En esta funcion primero va el mensaje a mostrar, las opciones
            opcion_principal = menu_opciones(mensaje_opciones_principales,opciones_principales)

            if opcion_principal == 1:    
                mensaje_producto = "¿Qué tipo de producto desea registrar?:\n"
                tipos_productos = ["1. Producto de Control.\n",
                "2. Antibiotico\n"]

                opcion_tipos_producto = menu_opciones(mensaje_producto, tipos_productos)
        

                match opcion_tipos_producto:
                    case 1:
                        mensaje_productos_control = "¿Desea Control de plagas o Fertilizante?:\n"
                        tipos_productos_control = ["1. Producto de Control de plagas.\n",
                        "2. Fertilizante\n"]
                        opcion_productos_control = menu_opciones(mensaje_productos_control, tipos_productos_control)

                        match opcion_productos_control:
                            case 1:
                                nombre = verificar_cadenas("Ingrese el nombre del producto de control de plagas:\n")
                                frecuencia = verificar_valores_numericos("Ingrese la frecuencia de aplicacion en dias del producto:\n")
                                precio = verificar_valores_numericos("Ingrese el valor de su producto:\n")
                                periodo = verificar_valores_numericos("Ingrese su periodo de carencia del producto:\n")
                                producto = ControlPlagas(nombre, frecuencia, precio, periodo)
                                Sistema.__productos+=1
                                self.productos['productos_control']['flagas'][Sistema.__productos] = producto
                            case 2:
                                nombre = verificar_cadenas("Ingrese el nombre del fertilizante:\n")
                                frecuencia = verificar_valores_numericos("Ingrese la frecuencia de aplicacion en dias del producto:\n")
                                valor = verificar_valores_numericos("Ingrese el valor de su producto:\n")
                                ultima_fecha = verificar_fecha("Ingrese la fecha de expiracion de su fertilizante:\n")
                                producto = Fertilizante(nombre, frecuencia, valor, ultima_fecha)
                                Sistema.__productos+=1
                                self.productos['productos_control']['fertilizantes'][Sistema.__productos] = producto
                            case _:
                                print("Opción inválida...\n")
                    case 2:
                        mensaje_productos_antibiotico = "¿Desea antibiotico de Bovinos o Porcinos?:\n"
                        tipos_productos_antibiotico = ["1. Antibiotico de Bovinos.\n",
                        "2. Antibiotico de Porcinos\n"]
                        opcion_productos_antibiotico = menu_opciones(mensaje_productos_antibiotico, tipos_productos_antibiotico)
                        match opcion_productos_antibiotico:
                            case 1:
                                nombre = verificar_cadenas("Ingrese el nombre del antibiotico para bovinos:\n")
                                dosis = verificar_valores_numericos("Ingrese la dosis:\n")
                                precio = verificar_valores_numericos("Ingrese el valor del antibiotico:\n")
                                producto = AntibioticoBovino(nombre, dosis, precio)
                                Sistema.__productos+=1
                                self.productos['antibioticos']['bovinos'][Sistema.__productos] = producto
                            case 2:
                                nombre = verificar_cadenas("Ingrese el nombre del antibiotico para porcinos:\n")
                                dosis = verificar_valores_numericos("Ingrese la dosis:\n")
                                precio = verificar_valores_numericos("Ingrese el precio del antibiotico:\n")
                                producto = AntibioticoPorcino(nombre, dosis, precio)
                                Sistema.__productos+=1
                                self.productos['antibioticos']['porcinos'][Sistema.__productos] = producto
                            case _:
                                print("Opción inválida...\n")
                    case _:
                        print("Opción inválida...\n")
            if opcion_principal == 2:
                factura = Factura()
                try: 
                    while(True):
                        print("Qué producto desea comprar?:\n")
                        self.mostrar_productos()
                        try:
                            opcion_producto = verificar_valores_numericos("")
                            if opcion_producto > 0 and (opcion_producto <= len(self.productos)):
                                producto = self.buscar_producto_por_id(opcion_producto)
                                factura.agregar_producto(producto)
                                opcion_otro = verificar_valores_numericos("Desea agregar otro producto?:\n 1. Si\n 2.No\n")
                                if opcion_otro == 1:
                                    limpiar_pantalla()
                                else:
                                    break
                        except:
                            print("Ingrese un producto válido\n")
                            limpiar_pantalla()

                except:
                    print("Ingrese una cedula válida...\n")
            if opcion_principal == 3:
                nombre_cliente = verificar_cadenas("Ingrese su nombre:\n")
                cedula_cliente = verificar_valores_numericos("Ingrese su cedula:\n")
                cliente = Cliente(nombre_cliente, cedula_cliente)
                cliente._cant_comprar+=1
                print(factura)
                cliente.historial_compras[cliente._cant_comprar] = factura
            if opcion_principal == 4:
                print("Saliendo...\n")
                break
            else:
                print("Ingrese una opción válida...\n")


            
            

    
    





