import sys
import os
import datetime
ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_padre)


from ClasesPadre.ProductoDeControl import ProductoControl

class Fertilizante(ProductoControl):
    def __init__(self, registroICA, nombre, frecuencia, valor, ultima_fecha):
        super().__init__(registroICA, nombre, frecuencia, valor)
        self.ultima_fecha = ultima_fecha
