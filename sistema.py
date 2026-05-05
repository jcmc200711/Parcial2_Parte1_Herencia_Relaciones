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
        self.productos = {
            'productos_control': {'plagas': {}, 'fertilizantes': {}},
            'antibioticos': {'porcinos': {}, 'bovinos': {}}
        }
        self.clientes = {}
        self.factura_actual = None  

    def agregar_cliente(self, cliente):
        self.clientes[cliente.cedula] = cliente

    def _imprimir_subcategorias(self, nombre_cat, subcats):
        print(f"\nCategoría: {nombre_cat}")
        for nombre_sub, productos in subcats.items():
            print(f"  [{nombre_sub}]: {len(productos)} artículos registrados.")

    def mostrar_productos(self):
        print("\n===== PRODUCTOS DISPONIBLES =====")

        for nombre_cat, subcats in self.productos.items():
            print(f"\n🔹 {nombre_cat.upper()}")

            for nombre_sub, productos in subcats.items():
                print(f"\n  ▸ {nombre_sub.capitalize()}")

                if not productos:
                    print("     (Sin productos)")
                else:
                    for id_prod, prod in productos.items():

                  
                        precio = prod.precio if hasattr(prod, 'precio') else prod.valor

                        ica = prod._registroICA if hasattr(prod, '_registroICA') else "N/A"

                        print(f"     ID: {id_prod}")
                        print(f"        Nombre: {prod.nombre}")
                        print(f"        Precio: ${precio}")
                    
                        if ica != "N/A":
                           print(f"        ICA: {ica}")
 
                        if hasattr(prod, 'frecuencia'):
                           print(f"        Frecuencia: {prod.frecuencia}")

                        if hasattr(prod, 'periodo_carencia'):
                           print(f"        Carencia: {prod.periodo_carencia} días")

                        if hasattr(prod, 'tipo_animal'):
                           print(f"        Tipo: {prod.tipo_animal}")

                        print()

    def buscar_producto_por_id(self, id):
        for categoria in self.productos.values():
            for subcat in categoria.values():
                if id in subcat:
                    return subcat[id]
        return None

    def ejecutar(self):
        while True:
            print("\n=== SISTEMA AGRÍCOLA ===\n")

            opcion_principal = menu_opciones(
                "Seleccione una opción:\n",
                ["1. Registrar un producto\n",
                 "2. Realizar una compra\n",
                 "3. Expedir factura\n",
                 "4. Salir\n"]
            )

            # ================= REGISTRAR =================
            if opcion_principal == 1:

                opcion_tipos_producto = menu_opciones(
                    "\n¿Qué tipo de producto desea registrar?\n",
                    ["1. Producto de Control\n", "2. Antibiótico\n"]
                )

                if opcion_tipos_producto == 1:

                    opcion_control = menu_opciones(
                        "\n¿Tipo de producto de control?\n",
                        ["1. Control de plagas\n", "2. Fertilizante\n"]
                    )

                    if opcion_control == 1:
                        nombre = verificar_cadenas("\nNombre:")
                        frecuencia = verificar_valores_numericos("Frecuencia (días):")
                        precio = verificar_valores_numericos("Precio:")
                        periodo = verificar_valores_numericos("Periodo de carencia:")
                        ica = verificar_valores_numericos("Ingrese el registro ICA:")

                        producto = ControlPlagas(ica, nombre, frecuencia, precio, periodo)

                        Sistema.__productos += 1
                        self.productos['productos_control']['plagas'][Sistema.__productos] = producto

                    elif opcion_control == 2:
                        nombre = verificar_cadenas("\nNombre:")
                        frecuencia = verificar_valores_numericos("Frecuencia:")
                        valor = verificar_valores_numericos("Precio:")
                        fecha = verificar_fecha("Fecha:")
                        ica = verificar_valores_numericos("Ingrese el registro ICA:")

                        producto = Fertilizante(ica, nombre, frecuencia, valor, fecha)

                        Sistema.__productos += 1
                        self.productos['productos_control']['fertilizantes'][Sistema.__productos] = producto

                elif opcion_tipos_producto == 2:

                    opcion_antibiotico = menu_opciones(
                        "¿Tipo de antibiotico?\n",
                        ["1. Bovino\n", "2. Porcino\n"]
                    )

                    nombre = verificar_cadenas("\nNombre:")
                    dosis = verificar_valores_numericos("Dosis:")
                    precio = verificar_valores_numericos("Precio:")

                    if opcion_antibiotico == 1:
                        producto = AntibioticoBovino(nombre, dosis, precio)
                        Sistema.__productos += 1
                        self.productos['antibioticos']['bovinos'][Sistema.__productos] = producto

                    else:
                        producto = AntibioticoPorcino(nombre, dosis, precio)
                        Sistema.__productos += 1
                        self.productos['antibioticos']['porcinos'][Sistema.__productos] = producto

                print("\n✔ Producto registrado correctamente\n")

            # ================= COMPRA =================
            elif opcion_principal == 2:

                self.factura_actual = Factura()

                while True:
                    print("\n--- PRODUCTOS DISPONIBLES ---")
                    self.mostrar_productos()

                    idp = verificar_valores_numericos("Ingrese ID del producto:\n")
                    producto = self.buscar_producto_por_id(idp)

                    if producto:
                        self.factura_actual.agregar_producto(producto)
                        print("✔ Producto agregado\n")
                    else:
                        print("❌ Producto no encontrado\n")

                    op = verificar_valores_numericos("1. Agregar otro\n2. Terminar\n")
                    if op == 2:
                        break

            # ================= FACTURA =================
            elif opcion_principal == 3:

                if not self.factura_actual:
                    print("❌ No hay compra realizada\n")
                    continue

                nombre = verificar_cadenas("\nNombre cliente:")
                cedula = verificar_valores_numericos("Cédula:")

                cliente = Cliente(nombre, cedula)
                cliente._cant_comprar += 1
                cliente.historial_compras[cliente._cant_comprar] = self.factura_actual

                self.agregar_cliente(cliente)

                print(self.factura_actual)

            # ================= SALIR =================
            elif opcion_principal == 4:
                print("Saliendo...")
                break
