import json

def guardar_datos(productos):
    with open("inventario.json", "w", encoding="utf-8") as file:
        json.dump([p.__dict__ for p in productos], file, indent=4)

#Nota: jason.dump guarda la lista en el archivo json
      #p.__dict__ convierte cada objeto producto en un json con tres atributos/propiedades


from producto import Producto

def cargar_datos():
    try:
        with open("inventario.json", "r", encoding="utf-8") as file:
            datos = json.load(file)
            return [Producto(**p) for p in datos]
    except FileNotFoundError:
        return []
    
#Nota 2: Lee el JSON
#Convierte cada diccionario en un objeto Producto
#Si no existe el archivo → devuelve lista vacía