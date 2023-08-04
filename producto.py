def input_int(mensaje, mensaje_error):
    while True:
        try:
            v = int(input(mensaje))
        except ValueError:
            print(mensaje_error)
        else:
            return v

class Productos:
    def __init__(self, nombre, marca, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad
    
    def info(self):
        return f"{self.nombre} {self.marca} {self.cantidad}"
    
    def actualizar_cantidad(self, cantidad_vendida):
        self.cantidad = self.cantidad - cantidad_vendida
    
    def get_nombre(self):
        return self.nombre 
    
    def get_marca(self):
        return self.marca
    
    def get_info_completa(self):
        return f"{self.nombre} {self.marca} {self.cantidad}"

    def actualizar_nombre(self, nuevo_nombre):
        return 
    
p = Productos("Teclado", "HP", 50, 300)
l = Productos("Laptop", "HP", 200, 300)
#print(p.info())
#p.actualizar_cantidad(5)
#print(p.info())
