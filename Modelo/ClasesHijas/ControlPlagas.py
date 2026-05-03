import sys
import os
ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_padre)


from ClasesPadre.ProductoDeControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, _registroICA, nombre, frecuencia, valor, periodo_carencia = 1):
        super().__init__(_registroICA, nombre, frecuencia, valor)
        self.periodo_carencia = periodo_carencia
