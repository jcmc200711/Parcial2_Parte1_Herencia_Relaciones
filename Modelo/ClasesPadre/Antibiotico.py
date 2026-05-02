class Antibiotico:
    _registros_antibiotico = 0
    def __init__(self, nombre = "Antibiotico default", dosis = 1, tipo_animal = "bovino", precio = 1000):
        Antibiotico._registros_antibiotico+=1
        self.id = Antibiotico._registros_antibiotico
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio