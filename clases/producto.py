class Producto:
    def __init__(self, nombre, categoria, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - {self.categoria}: {self.stock} en stock"