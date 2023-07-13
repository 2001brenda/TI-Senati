producto = {
    "nombre": "", 
    "marca":"",
    "costo": 0,
    "cantidad": 0,
}

lista_productos = []

flag=True
while flag:
    try:
        nombreproducto = input("Nombre del producto: ")
        marcaproducto = input("Marca del producto: ")
        costoproducto = input("costo del p´roducto: ")
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

        print(lista_productos)

#menu
print("""
      supermercado
      elija la opcion
1. listar los productos
2. agregar mas productos 
3. hacer la venta    
""")

opcion = input("elija la opcion del menu: ")
