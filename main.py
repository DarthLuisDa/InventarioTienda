print("<<<<<<------------------------------------------------->>>>>>>")
print("Bienvenido al Sistema de Inventario de la Tienda Laika_Games")
#Dos espacios
#Dos esapcios
print("<<<<<<------------------------------------------------->>>>>>>")
#Espacio para que se vea mas bonito
from inventario import Inventario
from persistencia import cargar_datos

inventario = Inventario()

inventario.productos = cargar_datos()

while True:
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Eliminar Producto")
    print("4. Buscar Producto")
    print("5. Productos con bajo stock")
    print("6. Editar Producto")
    print("7. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        inventario.agregar_producto(nombre, precio, stock)

    elif opcion == "2":
        print("\n===== INVENTARIO =====\n")
        inventario.mostrar_inventario()

    elif opcion == "3":
        nombre = input("Nombre del producto a eliminar: ")
        inventario.eliminar_producto(nombre)
        #print("3. Eliminar producto")

#Para buscar el nombre del producto, se necesita poner el nombre completo sino es dificil que lo encuentre
    elif opcion == "4":
        nombre = input("Nombre del producto a buscar: ")
        inventario.buscar_producto(nombre)

    elif opcion == "5":
        inventario.productos_bajo_stock()

    elif opcion == "6":
        nombre = input("Nombre del producto a editar: ")
        inventario.editar_producto(nombre)

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, intenta de nuevo.")




#Esta parte se dejara de utilizar ya que crearemos un menu interactivo
"""
from inventario import Inventario

# Crear el inventario
inventario = Inventario()

# Agregar productos (pruebas)
inventario.agregar_producto("Colección Completa Olocoons O2 Bimbo 2023-2025 21 Piezas Color", 1200, 32)
inventario.agregar_producto("Colección Completa Olocoons O2 Bimbo 2025 21 Piezas Translúcidos", 1200, 30)
inventario.agregar_producto("Colección Completa Cartoon Network Little Bites Bimbo 25 Piezas", 1100, 11)

# Mostrar inventario
print("\n===== INVENTARIO =====\n")
inventario.mostrar_inventario()
"""




#Esta parte solo muestra un producto

"""
from producto import Producto

producto1 = Producto("Colección Completa Olocoons O2 Bimbo 2023-2025 21 Piezas Color", 1200, 32)

producto2 = Producto("Colección Completa Olocoons O2 Bimbo 2025 21 Piezas Translúcidos", 1200, 30)

producto1.mostrar_producto()

print("------------------------------------------------------------")

producto2.mostrar_producto()

"""

















#Vamos a quitar esta parta para usar un método, simplificando todo
"""
print(f"Nombre: {producto1.nombre}")
print(f"Precio: ${producto1.precio:.2f}")
print(f"Stock: {producto1.stock} uds.")
"""

#Prueba ya que no me imprimia acentos
"""
import sys

print(sys.stdout.encoding)
print("Colección") 
"""