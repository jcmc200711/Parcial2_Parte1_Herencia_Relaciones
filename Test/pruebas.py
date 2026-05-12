import sys
import os

ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_proyecto)

from Modelo.ClasesGenerales.Cliente import Cliente
from Modelo.ClasesGenerales.Factura import Factura

from Modelo.ClasesHijas.Fertilizantes import Fertilizante
from Modelo.ClasesHijas.ControlPlagas import ControlPlagas

from Modelo.ClasesPadre.Antibiotico import Antibiotico

print("\n========== PRUEBAS UNITARIAS ==========\n")


# PRUEBA 1 - CREACIÓN DE OBJETOS


cliente = Cliente("Nata", 12345)

assert cliente.nombre == "Nata"
assert cliente.cedula == 12345

print("PRUEBA 1 EXITOSA - Creacion de cliente")


# ======================================================
# PRUEBA 2 -> HERENCIA Y ATRIBUTOS


antibiotico = Antibiotico(
    "Oxitetraciclina",
    20,
    "bovino",
    50000
)

assert antibiotico.nombre == "Oxitetraciclina"
assert antibiotico.dosis == 20
assert antibiotico.tipo_animal == "bovino"
assert antibiotico.precio == 50000

print("PRUEBA 2 EXITOSA - Antibiótico creado correctamente")


# ======================================================
# PRUEBA 3 -> HERENCIA Y ATRIBUTOS

fertilizante = Fertilizante(
    1001,
    "Triple15",
    30,
    70000,
    "10/05/2025"
)

assert fertilizante.nombre == "Triple15"
assert fertilizante.precio == 70000

print("PRUEBA 3 EXITOSA - Fertilizante creado correctamente")


# ======================================================
# PRUEBA 4 -> HERENCIA Y ATRIBUTOS

control = ControlPlagas(
    2001,
    "MataPlagas",
    15,
    45000,
    7
)

assert control.nombre == "MataPlagas"
assert control.precio == 45000
assert control.periodo_carencia == 7

print("PRUEBA 4 EXITOSA - Control de plagas creado correctamente")


# ======================================================
# PRUEBA 5 -> COMPOSICION Y LOGICA DE FACTURA

factura = Factura()

factura.agregar_producto(antibiotico)
factura.agregar_producto(fertilizante)

assert len(factura.lista_productos) == 2

print("PRUEBA 5 EXITOSA - Productos agregados a factura")


# ======================================================
# PRUEBA 6 -> ASOCIACION CLIENTE-FACTURA

cliente._cant_comprar += 1
cliente.historial_compras[cliente._cant_comprar] = factura

assert len(cliente.historial_compras) == 1

print("PRUEBA 6 EXITOSA - Factura asociada al cliente")


# ======================================================
# PRUEBA 7 -> HERENCIA

assert isinstance(fertilizante, Fertilizante)
assert isinstance(control, ControlPlagas)
assert isinstance(antibiotico, Antibiotico)

print("PRUEBA 7 EXITOSA - Herencia verificada")


# ======================================================
# PRUEBA 8 -> CRUD

datos = factura.to_dict()

assert "fecha" in datos
assert "valor_total" in datos
assert "lista_productos" in datos

print("PRUEBA 8 EXITOSA - Conversión a diccionario correcta")


print("\n========== TODAS LAS PRUEBAS PASARON ==========\n")
