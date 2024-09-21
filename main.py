# Importa modulo de tiempo
import time

#Importa clases
from clases import Producto, Inventario

#Importa modulos
from modulos import agregar_producto, buscar_producto, actualizar_stock, reportar_productos_agotados
from modulos import cargar_inventario, guardar_inventario

inventario = cargar_inventario()

#Inicia menú inventario
while True:
    print("1. Ingresar nuevo producto")
    print("2. Actualizar stock de producto")
    print("3. Buscar producto")
    print("4. Generar reporte de productos agotados")
    print("5. Salir")
    opcion = input("Seleccione opción: ")
    
    # Evalúa las opciones
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            while True:
                try:
                    stock = int(input("Ingrese la cantidad en stock: "))
                    break
                except ValueError:
                    # Imprime error
                    print("El número de stock no es válido. ")
            
            nuevo_producto = Producto(nombre, categoria, stock)
            agregar_producto(inventario,nuevo_producto)
            guardar_inventario(inventario)
            print(f"Producto '{nombre}' ingresado correctamente.")     
        case "2":
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            while True:
                try:
                    cantidad = int(input("Ingrese la nueva cantidad en stock: "))
                    break
                except ValueError:
                    # Imprime error
                    print("El número de stock no es válido. ") 
                    
            resultado = actualizar_stock(inventario, nombre, cantidad)
            guardar_inventario(inventario)
            if resultado:
                print(f"Stock actualizado para '{nombre}'.") 
            else:
                print(f"Producto '{nombre}' no encontrado.")
        case "3":
            busqueda = input("Ingrese el nombre o categoría del producto: ")
            resultados = buscar_producto(inventario, busqueda)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos para la búsqueda.") 
        case "4":
            productos_agotados = reportar_productos_agotados(inventario)
            if productos_agotados:
                print("Productos agotados:")
                for producto in productos_agotados:
                    print(producto)
            else:
                print("No hay productos agotados.") 
        case "5":
            print("Muchas gracias por usar mi sistema de reserva.")
            break
        case _:
            print("No existe la opción ingresada")
    
    # Espera unos segundos para desplegar el menú
    time.sleep(2)    
