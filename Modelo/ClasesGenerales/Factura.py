import datetime
class Factura:
    _contador_facturas = 0
    def __init__(self, fecha = datetime.date.today(), valor_total = 0):
        self._contador_facturas += 1
        self.id = Factura._contador_facturas
        self.fecha = fecha
        self.valor_total = 0


    def valor_total(self,dic_objetos):
        total = dic_objetos['precio'].sum()
        self.valor_total = total