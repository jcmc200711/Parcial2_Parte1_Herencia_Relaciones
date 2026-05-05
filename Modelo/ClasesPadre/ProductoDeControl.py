class ProductoControl:
    def __init__(self, registroICA, nombre, frecuencia, valor):
        self._registroICA = registroICA
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.valor = valor
        
    def __str__(self):
        return f"ICA: {self._registroICA:10} | Nombre: {self.nombre:15} | Frecuencia: {self.frecuencia:5} | Precio: ${self.valor:,}"
