
#RAMA DEVELOP
class SerVivo():
    def __init__(self, nombre = None, altura = None, peso = None):
        self.__nombre = nombre
        self.__altura = altura
        self.__peso = peso
    
    @property   
    def get_nombre(self):
        return self.__nombre
    
    def get_altura(self):
        return self.__altura
    
    def get_peso(self):
        return self.__peso
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_altura(self, altura):
        self.__altura = altura
        
    def set_peso(self, peso):
        self.__peso = peso
    
    def moverse(self):
        print("El ser vivo se puede mover")




ser1 = SerVivo("Juan", 1.8, 90)
ser2 = SerVivo()
ser2.set_altura(1.7)
ser2.set_nombre("Daniel")
ser2.set_peso(78)


class Persona(SerVivo):
    def __init__(self,nombre = None, altura = None, peso = None, dpi = None):
        super().__init__(nombre, altura, peso)
        self.__dpi = dpi
    
    def get_dpi(self):
        return self.__dpi
    
    def set_dpi(self, dpi):
        self.__dpi = dpi
        
    def moverse(self):
        super().moverse()
        print("La persona se mueve caminando") 
    
class Animal(SerVivo):
    def __init__(self,nombre = None, altura = None, peso = None, tipo = None):
        super().__init__(nombre, altura, peso)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    def moverse(self):
        super().moverse()
        print("El animal puede arrastrarse, nadar, caminar en dos patas o en cuatro")   

pedro = Persona("Pedro", 1.88, 87, "12345")

perro = Animal("Stinky", 1.76, 67, "Mamifero")
perro.moverse()

        