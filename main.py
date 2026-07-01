print("Bienvenido al Sistema de Inventario de la Tienda Laika_Games")

print("<<<<<<------------------------------------------------->>>>>>>")

from producto import Producto

producto1 = Producto("Colección Completa Olocoons O2 Bimbo 2023-2025 21 Piezas Color", 1200, 32)

producto2 = Producto("Colección Completa Olocoons O2 Bimbo 2025 21 Piezas Translúcidos", 1200, 30)

producto1.mostrar_producto()

print("------------------------------------------------------------")

producto2.mostrar_producto()


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