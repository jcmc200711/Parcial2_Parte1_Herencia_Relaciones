from Modelo.ClasesGenerales.Cliente import Cliente
from Modelo.ClasesGenerales.Factura import Factura
from Modelo.ClasesHijas.Fertilizantes import Fertilizante
from Modelo.ClasesHijas.ControlPlagas import ControlPlagas
from Modelo.ClasesHijas.AntibioticosBovinos import AntibioticoBovino
from Modelo.ClasesHijas.AntibioticosPorcinos import AntibioticoPorcino

from UI.menu_opciones import menu_opciones
from UI.verificar_cadenas import verificar_cadenas
from UI.verificar_valores_numericos import verificar_valores_numericos
from UI.verificar_fecha import verificar_fecha
from CRUD.buscar_por_cedula import buscar_por_cedula
from CRUD.guardar_cliente import guardar_o_actualizar_cliente
from CRUD.borrar_registros import resetear_archivo_datos

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

    def mostrar_facturas(self, facturas_dict):
        if not facturas_dict:
            print("\n[!] No hay facturas registradas.")
            return

        for id_f, datos in facturas_dict.items():
            # TODO lo de abajo debe estar indentado para que se repita por cada factura
            print("\n" + "="*40)
            print(f"FACTURA N°: {id_f}")
            print(f"FECHA: {datos.get('fecha')}")
            print("-" * 40)
        
            # Esta parte estaba "afuera" en tu código:
            productos = datos.get('lista_productos', [])
            if not productos:
                print("   (Factura sin productos registrados)")
            else:
                for p in productos:
                    print(f"• {p}") 

            print("-" * 40)
            print(f"TOTAL PAGADO: ${datos.get('valor_total')}")
            print("="*40)


    def ejecutar(self):
        while True:
            print("\n=== SISTEMA AGRÍCOLA ===\n")

            opcion_principal = menu_opciones(
                "Seleccione una opción:\n",
                ["1. Registrar un producto\n",
                 "2. Realizar una compra\n",
                 "3. Expedir factura\n",
                 "4. Buscar las facturas de un cliente por cedula\n",
                 "5. Borrar registros\n",
                 "6. Salir\n"]
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
                        precio = verificar_valores_numericos("Precio:")
                        fecha = verificar_fecha("Fecha:")
                        ica = verificar_valores_numericos("Ingrese el registro ICA:")

                        producto = Fertilizante(ica, nombre, frecuencia, precio, fecha)

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

                print(self.factura_actual) #Breakpoint para el debug

            # ================= BUSCAR CLIENTE POR CEDULA =================
            elif opcion_principal == 4:
                for cliente in self.clientes.values():
                    historial_limpio = {}
                    for id_factura, factura_obj in cliente.historial_compras.items():
                        historial_limpio[id_factura] = factura_obj.to_dict()

                    guardar_o_actualizar_cliente(cliente.cedula, cliente.nombre, historial_limpio)
                cedula_buscar = verificar_valores_numericos("Ingrese la cedula para buscar las facturas del cliente:\n")
                facturas, nombre_cliente = buscar_por_cedula(cedula_buscar)
                print(f"Nombre del cliente: {nombre_cliente}\n")
                print("Sus facturas:\n")
                self.mostrar_facturas(facturas)

            # ================= BORRAR LOS DATOS REGISTRADOS EN EL ARCHIVO clientes.txt =================
            elif opcion_principal == 5:
                resetear_archivo_datos()
                print("Los registros han sido borrados.\n")

            # ================= SALIDA =================
            elif opcion_principal == 6:
                for cliente in self.clientes:
                    guardar_o_actualizar_cliente(cliente.cedula, cliente.nombre, cliente.historial_compras)
                print("Saliendo...\n")
                break
                
                
