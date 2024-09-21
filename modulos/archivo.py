import json
from clases import Inventario, Producto
from .inventario import agregar_producto

def cargar_inventario():
    try:
        with open('inventario.json', 'r') as file:
            data = json.load(file)
            inventario = Inventario()
            for item in data:
                producto = Producto(item['nombre'], item['categoria'], item['stock'])
                agregar_producto(inventario, producto)
            return inventario
    except FileNotFoundError:
        return Inventario()
    except json.JSONDecodeError:
        print("Error al leer el archivo de inventario. Creando uno nuevo.")
        return Inventario()

def guardar_inventario(inventario):
    data = [{'nombre': p.nombre, 'categoria': p.categoria, 'stock': p.stock} for p in inventario.productos.values()]
    with open('inventario.json', 'w') as file:
        json.dump(data, file)
