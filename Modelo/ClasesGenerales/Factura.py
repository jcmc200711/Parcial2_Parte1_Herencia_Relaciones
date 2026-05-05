import datetime

class Factura:
    _contador_facturas = 0

    def __init__(self, fecha=None, cliente=None):
        Factura._contador_facturas += 1
        self.id = Factura._contador_facturas
        self.fecha = fecha if fecha else datetime.date.today()
        self.cliente = cliente
        self.lista_productos = []
        self.valor_total = 0

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        
        # 👇 soporte para ambos tipos
        if hasattr(producto, 'precio'):
            self.valor_total += producto.precio
        elif hasattr(producto, 'valor'):
            self.valor_total += producto.valor

    def __str__(self):
        encabezado = f"\n{'='*40}\n"
        encabezado += f"FACTURA N°: {self.id}\n"
        encabezado += f"FECHA: {self.fecha}\n"
        encabezado += f"{'-'*40}\n"
        encabezado += f"{'Prod.':<20} {'Precio':>18}\n"
        encabezado += f"{'-'*40}\n"

        cuerpo = ""
        for p in self.lista_productos:
            precio = p.precio if hasattr(p, 'precio') else p.valor
            cuerpo += f"{p.nombre:<20} ${precio:>17,}\n"

        pie = f"{'-'*40}\n"
        pie += f"{'TOTAL A PAGAR:':<20} ${self.valor_total:>17,}\n"
        pie += f"{'='*40}\n"

        return encabezado + cuerpo + pie
