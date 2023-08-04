#productos  = []
#append agrema mas datos a la coleccion
#productos.append("laptop")
#productos.append("mouse")
#print(productos[1])

#diciconario {} y valor 
#productos = {}

#productos["nombre"] = "laptop"
#productos["precio"] = 1200

#get para acceder solo a un indicador 
#print(productos.get("nombre"))

#productos = [
    #{"productos":
     #[]
     #}
#]

#productos = [1,2,3,4,5,6,7,8]
#print(productos[0] + 1)
#suma_elementos = []

#for para listas  de una secuencia definida 
#for producto in productos:
    #print(producto +1)
    #suma_elementos.append(producto + 1)
#print(productos)
#print(suma_elementos)

#print(len(productos))
#contador = 0
#while proceso infinito hasta q se cumpla la condicion 
#while True:
    #print(productos[contador])
    #if (len(productos)-1) == contador:
        #break #para detener el siglo
    #else:
       # contador += 1

#para realizar una funcion
#def multiplicacion(numero1, numero2):
    #resultado = numero1 * numero2
    #return resultado 

#valor1 = 12
#valor2 = 2
#print (multiplicacion(valor1, valor2)) #es una funcion dinamica

#import math
#area_circunferencia = 2*pi*r 

#def area_circunferencia(radio):
    #resultado = 2 * math.pi * (radio*radio)
    #print(resultado)

def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def division(a, b):
    return a/b

def input_int(mensaje, mensaje_error):
    while True:
        try:
            v = int(input(mensaje))
        except ValueError:
            print(mensaje_error)
        else:
            return v
        #break 
#input_int("ingrese un valor: ")

menu = """
    calculadora
opciones:
1. sumar
2. restar
3. multiplicar
4. dividir 
5. salir
"""

while True:
    print(menu)
    opcion = input_int("elije la opcion: ", "es la opcion incorrecta") 

    if opcion in [1,2,3,4]:
        a = input_int("ingrese el primer valor: ", "no es un numero")
        b = input_int("ingrese el segundo valor: ", "no es un numero")
        if opcion == 1:
            print(f"el resultado es {suma(a,b)}")
        elif opcion  == 2:
            print(f"el resultado es {resta(a,b)}")
        elif opcion == 3:
            print(f"el resultado es {multiplicacion(a,b)}")
        elif opcion == 4:
            print(f"el resultado es {division(a,b)}")
            
    elif opcion == 5:
        print("saliendo")
        break

    else:
        print("no existe esa opcion")
