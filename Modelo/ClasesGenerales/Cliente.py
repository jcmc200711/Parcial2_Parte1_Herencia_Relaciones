class Cliente:
    _cantidad_clientes = 0
    def __init__(self, nombre = "Cliente default", cedula = "00000"):
        _cantidad_clientes += 1
        self.nombre = nombre
        self.cedula = cedula
        self._cant_comprar = 0
        self.historial_compras = {}

        