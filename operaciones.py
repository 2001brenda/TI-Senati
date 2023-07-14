from productos import crearproductos, listarproductos

def menu():
    lista_de_productos = []
    omenu = ("""
    MINIMARKET
    _________________________
    1. listar los productos
    2. agregar producto_costo
    3. salir
    """)
    flag = True
    while flag:
        try:
            print(omenu)
            opcion = int(input("Elije la opcion: "))
        except ValueError:
            print('Has elegido una opcion que no esta en el menu')
            listarproductos(lista_de_productos)
        else:
            if opcion == 1:
                print("Listando productos")
                print(lista_de_productos)
            elif opcion == 2:
                print("Agegando productos")
                crearproductos(lista_de_productos)
            elif opcion == 3:
                print("saliendo")
                flag = False

menu()
