from producto import Producto
from persistencia import guardar_datos

class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, stock):
    # Verificar si el producto ya existe
     for producto in self.productos:
        if producto.nombre.lower() == nombre.lower():
            print("Error: El producto ya existe en el inventario.")
            return

    # Crear el nuevo producto
     nuevo_producto = Producto(nombre, precio, stock)

    # Agregarlo a la lista
     self.productos.append(nuevo_producto)

    # Guardar cambios
     guardar_datos(self.productos)

     print("Producto agregado correctamente.")
    #Esto se modifica
    """
    def agregar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        self.productos.append(nuevo_producto)
        guardar_datos(self.productos)
        print("Producto agregado correctamente.")
    """
    #Esto se modifica
    """
    def agregar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        self.productos.append(nuevo_producto)
        print("Producto agregado correctamente.")
    """
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            producto.mostrar_producto()
            print("--------------------")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
          if producto.nombre.lower() == nombre.lower():
            self.productos.remove(producto)
            guardar_datos(self.productos)
            print("Producto eliminado correctamente.")
            return

        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
         if producto.nombre.lower() == nombre.lower():
            print("\nProducto encontrado:\n")
            producto.mostrar_producto()
            return

        print("Producto no encontrado.")

    def productos_bajo_stock(self, limite=5):
        encontrados = False

        print(f"\nProductos con stock menor o igual a {limite}:\n")

        for producto in self.productos:
         if producto.stock <= limite:
            producto.mostrar_producto()
            print("--------------------")
            encontrados = True

        if not encontrados:
            print("No hay productos con bajo stock.")

    def editar_producto(self, nombre):
        for producto in self.productos:
          if producto.nombre.lower() == nombre.lower():

            print("\nProducto encontrado. Deja vacío si no quieres cambiar algo.\n")

            nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ")
            nuevo_precio = input(f"Nuevo precio ({producto.precio}): ")
            nuevo_stock = input(f"Nuevo stock ({producto.stock}): ")

            if nuevo_nombre:
                producto.nombre = nuevo_nombre

            if nuevo_precio:
                producto.precio = float(nuevo_precio)

            if nuevo_stock:
                producto.stock = int(nuevo_stock)
            
            guardar_datos(self.productos)
            print("Producto actualizado correctamente.")
            return

        print("Producto no encontrado.")