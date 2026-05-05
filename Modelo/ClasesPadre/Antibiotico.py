class Antibiotico:
    __registros_antibiotico = 0
    def __init__(self, nombre = "Antibiotico default", dosis = 1, tipo_animal = "default", precio = 1000):
        Antibiotico.__registros_antibiotico+=1
        self._id = Antibiotico.__registros_antibiotico
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio

    def __str__(self):
        return f"Id: {self._id:10} | Nombre: {self.nombre:15} | Dosis: {self.dosis:5} | Tipo de animal: ${self.tipo_animal:15} | Precio: ${self.precio:,}"