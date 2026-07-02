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
