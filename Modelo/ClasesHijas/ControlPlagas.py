import sys
import os
ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_padre)


from ClasesPadre.ProductoDeControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registroICA, nombre, frecuencia, precio, periodo_carencia):
        super().__init__(registroICA, nombre, frecuencia, precio)
        self.periodo_carencia = periodo_carencia
