import datetime
class Factura:
    _contador_facturas = 0
    def __init__(self, fecha = datetime.date.today(), valor_total = 0):
        self._contador_facturas += 1
        self.id = Factura._contador_facturas
        self.fecha = fecha
        self.lista_productos = {}
        self.valor_total = 0


    def valor_total(self,dic_objetos):
        total = dic_objetos['precio'].sum()
        self.valor_total = total
    
    def agregar_producto(self,producto):
        self.lista_productos += producto

    import datetime

class Factura:
    _contador_facturas = 0

    def __init__(self, fecha=None, cliente=None):
        Factura._contador_facturas += 1
        self.id = Factura._contador_facturas
        self.fecha = fecha if fecha else datetime.date.today()
        self.cliente = cliente
        self.lista_productos = []  # Usaremos una lista para guardar los objetos vendidos
        self.valor_total = 0

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        self.valor_total += producto.precio

    def __str__(self):
        # 1. Cabecera de la factura
        encabezado = f"\n{'='*40}\n"
        encabezado += f"FACTURA N°: {self.id}\n"
        encabezado += f"FECHA: {self.fecha}\n"
        encabezado += f"{'-'*40}\n"
        encabezado += f"{'Prod.':<20} {'Precio':>18}\n"
        encabezado += f"{'-'*40}\n"

        # 2. Detalle de productos
        cuerpo = ""
        for p in self.lista_productos:
            # Asumiendo que el producto tiene atributo 'nombre' y 'precio'
            cuerpo += f"{p.nombre:<20} ${p.precio:>17,}\n"

        # 3. Pie de factura con el total
        pie = f"{'-'*40}\n"
        pie += f"{'TOTAL A PAGAR:':<20} ${self.valor_total:>17,}\n"
        pie += f"{'='*40}\n"

        return encabezado + cuerpo + pie