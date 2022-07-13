from NodoEncabezado import NodoEncabezado

class ListaEncabezado():
    def __init__(self, tipo = None):
        self.tipo = tipo
        self.primero: NodoEncabezado = None
        self.ultimo: NodoEncabezado = None
        self.size = 0

    def insertarEncabezado(self, nuevo):
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:

            #INSERTAR EN ORDEN (IMPORTANTE)
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                aux = self.primero

                while aux != None:
                    if nuevo.id < aux.id:
                        nuevo.siguiente = aux
                        nuevo.anterior = aux.anterior
                        aux.anterior.siguiente = nuevo
                        aux.anterior = nuevo
                        break
                    elif nuevo.id > aux.id:
                        aux = aux.siguiente
                    else:
                        break

    
    def mostrarEncabezado(self):
        aux = self.primero
        while aux != None:
            print("Encabezado ", self.tipo, aux.id)
            aux = aux.siguiente
        
    def getEncabezado(self, id) -> NodoEncabezado:
        aux = self.primero
        while aux != None:
            if id == aux.id:
                return aux
            aux = aux.siguiente
        return None

# fila = ListaEncabezado("FILA")
# n1 = NodoEncabezado(2)
# n2 = NodoEncabezado(4)
# n3 = NodoEncabezado(3)

# fila.insertarEncabezado(n1)
# fila.insertarEncabezado(n2)
# fila.insertarEncabezado(n3)

# fila.mostrarEncabezado()
