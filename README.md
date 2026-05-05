# 🌱 Sistema de Facturación para Tienda Agrícola

Este proyecto consiste en el desarrollo de un sistema de facturación orientado a una tienda agrícola, el cual permite gestionar productos como fertilizantes, plaguicidas y antibióticos para animales (bovinos y porcinos).

El sistema fue desarrollado aplicando principios de Programación Orientada a Objetos (POO), destacando el uso de **herencia, composición y encapsulamiento**.

---

## 📌 Funcionalidades

- ✅ Registro de productos:
  - Fertilizantes
  - Control de plagas
  - Antibióticos (bovinos y porcinos)

- ✅ Gestión de compras:
  - Selección de productos por ID
  - Agregado de múltiples productos a una factura

- ✅ Generación de facturas:
  - Cálculo automático del total
  - Visualización estructurada

- ✅ Validación de datos:
  - Entradas numéricas
  - Cadenas de texto
  - Fechas

---

## 🧠 Conceptos aplicados

### 🔹 Herencia
Se implementó en:
- `Antibiotico` → `AntibioticoBovino`, `AntibioticoPorcino`
- `ProductoControl` → `ControlPlagas`, `Fertilizante`

Esto permitió reutilizar atributos comunes y especializar comportamientos.

---

### 🔹 Composición
La clase `Factura` contiene múltiples productos:

```python
lista_productos = []
