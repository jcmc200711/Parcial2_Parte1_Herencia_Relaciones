class Antibiotico:
    __registros_antibiotico = 0

    def __init__(self, nombre, dosis, tipo_animal, precio):
        Antibiotico.__registros_antibiotico += 1
        self._id = Antibiotico.__registros_antibiotico
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio

    def __str__(self):
        return f"ID: {self._id} | {self.nombre} | {self.tipo_animal} | Dosis: {self.dosis} | Precio: ${self.precio}"
