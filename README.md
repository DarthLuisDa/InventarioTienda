# Sistema de Inventario para Tienda

## Descripción

Este proyecto consiste en un sistema de gestión de inventario desarrollado en **Python** aplicando los principios de **Programación Orientada a Objetos (POO)** y persistencia de datos mediante archivos **JSON**.

El sistema permite administrar los productos de una tienda desde una interfaz de consola, facilitando operaciones como agregar, eliminar, editar y buscar productos, además de mantener la información almacenada para futuras ejecuciones.

---

## Objetivos del Proyecto

* Aplicar Programación Orientada a Objetos.
* Utilizar clases, objetos y métodos.
* Implementar validaciones para evitar productos duplicados.
* Guardar y recuperar información utilizando archivos JSON.
* Simular el funcionamiento básico de un sistema de inventario.

---

## Funcionalidades

### Gestión de Productos

* Agregar nuevos productos.
* Mostrar el inventario completo.
* Buscar productos por nombre.
* Editar la información de un producto.
* Eliminar productos existentes.

### Control de Inventario

* Evita registrar productos con nombres duplicados.
* Muestra los productos con bajo stock (por defecto, menor o igual a 5 unidades).

### Persistencia de Datos

* Guarda automáticamente los cambios en un archivo `inventario.json`.
* Carga el inventario automáticamente al iniciar el programa.

---

## Estructura del Proyecto

```text
Proyecto/
│
├── main.py              # Menú principal
├── inventario.py        # Clase Inventario
├── producto.py          # Clase Producto
├── persistencia.py      # Guardar y cargar datos JSON
├── inventario.json      # Base de datos del inventario
└── README.md
```

---

## Tecnologías Utilizadas

* Python 3
* Programación Orientada a Objetos (POO)
* Módulo `json`
* Archivos JSON para persistencia de datos

---

## Menú del Sistema

```text
===== SISTEMA DE INVENTARIO =====

1. Agregar producto
2. Mostrar inventario
3. Eliminar producto
4. Buscar producto
5. Productos con bajo stock
6. Editar producto
7. Salir
```

---

## Características Implementadas

* ✔ Creación de productos.
* ✔ Visualización del inventario.
* ✔ Eliminación de productos.
* ✔ Búsqueda por nombre.
* ✔ Edición de productos.
* ✔ Validación para evitar productos duplicados.
* ✔ Persistencia automática de datos.
* ✔ Carga automática del inventario al iniciar.

---

## Autor

Luis Daniel Vargas Rodríguez
