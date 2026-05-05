import sys
import os
ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_padre)


from ClasesPadre.Antibiotico import Antibiotico

class AntibioticoPorcino(Antibiotico):
    def __init__(self, nombre, dosis, precio):
        super().__init__(nombre, dosis, "porcino", precio)
