from producto import Productos, input_int

lista_productos = []
p = Productos("latop", "ASUS", 2000, 5)
#lista_productos.append(p)
#print(lista_productos)
#producto = lista_productos[0]
#print(producto.info())

nombre_p = input("Nombre del producto: ")
marca_p = input("Marca del prodcuto: ")
precio_p = input_int("Precio del producto: ", "no ingresaste bien el precio ")
cantidad_p = input_int("Cantidad del prodcuto: ", "no ingresaste bien la cantidad")

while
t = Productos(nombre_p, marca_p, precio_p, cantidad_p)
print(t.info())
lista_productos.append(t)
