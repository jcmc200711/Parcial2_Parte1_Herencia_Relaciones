class Antibiotico:
    __registros_antibiotico = 0
    def __init__(self, nombre = "Antibiotico default", dosis = 1, tipo_animal = "default", precio = 1000):
        Antibiotico.__registros_antibiotico+=1
        self._id = Antibiotico.__registros_antibiotico
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio