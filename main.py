print("Bienvenido al Sistema de Inventario de la Tienda Laika_Games")

from producto import Producto

producto1 = Producto("Colección Completa Olocoons O2 Bimbo 2023-2025 21 Piezas Color", 999, 32)




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