lista_productos.append(prueba)
def comparar_producto(np, mp, list_product):
    existe = False
    for p in list_product:
        if np.upper() == p.get_nombre().upper() and mp.apper() == p.get_marca().upper():
            print("el producto ya existe")
            existe = True
        else:
            print("agregando producto")
    return existe 
#comparar_producto("laptop", "asus", lista_productos)

def crar_producto(list_product):
    nombre_p = input("Nombre del producto: ")
    marca_p = input("Marca del prodcuto: ")
    precio_p = input_int("Precio del producto: ", "no ingresaste bien el precio ")
    cantidad_p = input_int("Cantidad del prodcuto: ", "no ingresaste bien la cantidad")

    existencia = comparar_producto(nombre_p, marca_p, lista_productos)
    if not existencia:
        nuevo_producto =Productos(nombre_p, marca_p, precio_p, cantidad_p)
        list_product.append(nuevo_producto)

#crar_producto(lista_productos)
#print(lista_productos)
def lista_productos(list_product):
    c = 0
    for p in list_product:
        c += 1
        print(f"{c}. {p.get_info_completa()} ")
lista_productos(lista_productos)
