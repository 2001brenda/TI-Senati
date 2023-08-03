#-edad
#-color
#-tipo_pelaje
#-genero  
#-nombre 

#acciones
#-comer
#-correr 
#-dormir 
#-sonido 

#class Gato:
    #def __init__(self, nombre, genero, color, edad):
        #self._nombre = nombre 
        #self._genero = genero
        #self._color = color
        #self._edad = edad 

    #def correr(self, punto_llegada):
        #print(f"{self._nombre} tienes que ir a {punto_llegada}")
        #print("si llegaste detente ahi")

    #def dormir(self, tiempo_dormir):
        #print(f"{self._nombre} empieza a dormir {tiempo_dormir}")


#chimi = Gato("Chimi", "macho", "gris", 1)
#chimi.correr("a la mesa")

#kitty= Gato("Kitty", "hembra", "blanco", 1)
#kitty.dormir("15 minutos")


class Persona:
    def __init__(self, nombre, genero, dni, fecha_nacimiento, talla, peso):
        self._nombre = nombre 
        self._genero = genero
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento 
        self._talla = talla
        self._peso = peso
        

    #def caminar(self, punto_llegada):
        #print(f"{self._nombre} tienes que ir a {punto_llegada}")
        #print("si llegaste quedate ahi")

    #def comer(self, fruta_comer):
        #print(f"{self._nombre} empieza a comer {fruta_comer}")
        #print("si terminaste levanta la mano")


#diego = Persona("Diego", "varon", 23, 1.70, 60)
#diego.caminar("al parque")

#brenda= Persona("Brenda", "mujer", 22, 1.60, 55)
#brenda.comer("la manzana")

def edad(self):
    #self._fecha_nacimiento
    return 15

class Alumno(Persona):
    def __init__(self, nombre, genero, dni, fecha_nacimiento, talla, peso, id_estudiante, email):
        super().__init__(self, nombre, genero, dni, fecha_nacimiento, talla, peso)
        self._id_estudiante = id_estudiante
        self._email = email 

    def info(self):
        print(f"{self._nombre} {self._dni} {self._id_estudiante}")


juan = Alumno ("juan", "m", "72837459", "10/10/2001", "65", "1.75", "345678", "juan@senati.pe")
juan.info()


#persona = Persona("juan", "m", "72837459", "10/10/2001", "65", "1.75")
#print(persona.edad)
