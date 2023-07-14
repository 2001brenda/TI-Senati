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
    print('N Producto | Marca | Precio | Cantidad')
    for producto in lista_productos:
        print(f"{producto.get('nombre')} | {producto.get('marca')} | {producto.get('costo')} | {producto.get('cantidad')}")
