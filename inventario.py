from producto import Producto
from persistencia import guardar_datos

class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        self.productos.append(nuevo_producto)
        guardar_datos(self.productos)
        print("Producto agregado correctamente.")

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