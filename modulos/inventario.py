

def agregar_producto(inventario, producto):
    inventario.productos[producto.nombre] = producto

def actualizar_stock(inventario, nombre, cantidad):
    if nombre in inventario.productos:
        inventario.productos[nombre].stock = cantidad
        return True
    else:
        return False

def buscar_producto(inventario, busqueda):
    return [p for p in inventario.productos.values() if busqueda.lower() in p.nombre.lower() or busqueda.lower() in p.categoria.lower()]

def reportar_productos_agotados(inventario):
    return [p for p in inventario.productos.values() if p.stock == 0]
    
    