class ProductoControl:
    _registros_ICA = 0
    def __init__(self, nombre = "Producto default", frecuencia = 1, valor = 1000):
        ProductoControl._registros_ICA+=1
        self.registroICA = ProductoControl._registros_ICA
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.valor = valor
        
