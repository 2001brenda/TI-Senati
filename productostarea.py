def crearproductos(lista_productos):
    producto = {}
    flag=True
    while flag:
        try:
            nombreproducto = input("Nombre del producto: ")
            marcaproducto = input("Marca del producto: ")
            costoproducto = int(input("costo del producto: "))
            cantidadproducto = int(input("cantidad del producto: "))

        except ValueError:
            print("ALGO SALIO MAL INTENTELO OTRA VEZ")
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]= costoproducto
            producto["cantidad"]= cantidadproducto
            lista_productos.append(producto)
            producto = {}
            pregunta = input("desea agregar mas productos? si/no")
            if str(pregunta) != "SI":
                flag = False

    return lista_productos

def listarproductos(lista_productos):
    print('N° | Producto | Cantidad | Precio')
    counter = 0
    for producto in lista_productos:
        counter += 1
        print(f"{counter} | {producto.get('nombre')} | {producto.get('marca')} | {producto.get('costo')} | {producto.get('cantidad')}")

def coincidenciaproducto(nombreproducto, cantidadproducto, lista_productos): 
    #agrega la cantidad de producto registrada
    flag = False
    for producto in lista_productos:
        if producto.get("nombre") == nombreproducto:
            print("este producto ya esta registrado")
            producto["cantidad"] = producto.get('cantidad') + cantidadproducto
            flag = True
    return flag

def ventaproductos(lista_de_productos):
    lista_venta = []
    producto_venta = {}
    listarproductos(lista_de_productos)
    while True:
        try:
            seleccionproducto = int(input('elija el numero del producto: '))
            producto = lista_de_productos[seleccionproducto-1]
            producto_cantidad = int(input(f'escriba cantidad de {producto.get("nombre")}: '))
           
        except ValueError:
            print("algo salio mal")
        else:
        
            producto["cantidad"] = producto.get("cantidad") - producto_cantidad
            producto_venta["producto"] = producto.get("nombre")
            producto_venta["cantidad"] = producto_cantidad
            producto_venta["subtotal"] = producto_cantidad * producto.get("costo")
            lista_venta.append(producto_venta)
            listarproductos(lista_de_productos)
            flag_repeticion = duplicadoproducto(producto_venta, lista_de_productos)
            if not flag_repeticion:
                lista_de_productos.append(producto)
            producto_venta = {}
            pregunta=input("desea a comprar mas productos? si/no")
            if str(pregunta) != "SI":
                break
            print(lista_venta)

def duplicadoproducto(producto_venta, lista_de_productos): 
    flag = False
    for producto in lista_de_productos:
        if producto.get("nombre") == producto_venta:
            print("ya compró este producto")
            flag = True
    return flag
