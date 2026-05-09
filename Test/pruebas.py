import sys
import os
ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_padre)

from Modelo.ClasesGenerales.Factura import Factura
from Modelo.ClasesHijas.AntibioticosBovinos import AntibioticoBovino
from Modelo.ClasesHijas.AntibioticosPorcinos import AntibioticoPorcino
from Modelo.ClasesHijas.ControlPlagas import ControlPlagas
from Modelo.ClasesHijas.Fertilizantes import Fertilizante

# ================= TEST 1 =================

def test_agregar_productos_factura():
    factura = Factura()

    a = AntibioticoBovino("Oxitetraciclina", 10, 20000)
    p = ControlPlagas(1234, "Glifosato", 15, 50000, 7)

    factura.agregar_producto(a)
    factura.agregar_producto(p)

    assert factura.valor_total == 70000

    print("\nTest 1: Factura suma productos correctamente\n")


# ================= TEST 2 =================

def test_herencia_antibioticos():
    bovino = AntibioticoBovino("Penicilina", 5, 30000)
    porcino = AntibioticoPorcino("Tilosina", 8, 25000)

    assert bovino.tipo_animal == "bovino"
    assert porcino.tipo_animal == "porcino"

    print("\nTest 2: Herencia de antibióticos correcta\n")


# ================= TEST 3 =================

def test_producto_control():
    plaga = ControlPlagas(5678, "Mancozeb", 10, 40000, 14)

    assert plaga._registroICA == 5678
    assert plaga.periodo_carencia == 14

    print("\nTest 3: Producto de control correcto\n")


# ================= TEST 4 =================

def test_fertilizante():
    fert = Fertilizante(9999, "Urea", 30, 80000, "10/05/2026")

    assert fert.nombre == "Urea"
    assert fert.frecuencia == 30

    print("\nTest 4: Fertilizante correcto\n")


# ================= TEST 5 =================

def test_factura_vacia():
    factura = Factura()
    assert factura.valor_total == 0
    assert len(factura.lista_productos) == 0

    print("\nTest 5: Factura vacía correcta\n")


# ================= TEST 6 =================

def test_multiples_productos():
    factura = Factura()

    a = AntibioticoBovino("A", 1, 10000)
    b = AntibioticoPorcino("B", 1, 20000)
    c = ControlPlagas(1111, "C", 10, 30000, 5)

    factura.agregar_producto(a)
    factura.agregar_producto(b)
    factura.agregar_producto(c)

    assert factura.valor_total == 60000

    print("\nTest 6: Múltiples productos correcto\n")


# ================= TEST 7 =================

from sistema import Sistema

def test_busqueda_producto():
    sistema = Sistema()

    p = ControlPlagas(1234, "Test", 10, 10000, 5)

    Sistema._Sistema__productos += 1
    sistema.productos['productos_control']['plagas'][Sistema._Sistema__productos] = p

    encontrado = sistema.buscar_producto_por_id(Sistema._Sistema__productos)

    assert encontrado is not None

    print("\nTest 7: Búsqueda correcta\n")
    

# ================= EJECUTAR =================

if __name__ == "__main__":
    test_agregar_productos_factura()
    test_herencia_antibioticos()
    test_producto_control()
    test_fertilizante()
    test_factura_vacia()
    test_multiples_productos()
    test_busqueda_producto()

    print("\n TODOS LOS TESTS PASARON")
