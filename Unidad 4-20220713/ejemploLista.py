#LISTA ENLAZADA DE USUARIOS Y PASSWORD

from urllib.request import AbstractDigestAuthHandler


class Nodo:
    def __init__(self, username = None, password = None, siguiente = None):
        self.username = username
        self.password = password
        self.siguiente = siguiente
        

class ListaSimpleEnlazada:
    def __init__(self):
        self.raiz = Nodo()
        self.ultimo = Nodo()
        
    
    def append(self, nuevoNodo):
        if self.raiz.username is None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def pop(self, username = None):
        if username is None:
            if self.raiz.siguiente is None:
                self.raiz = Nodo()
            else:
                nodoaux = self.raiz
                nodoPenultimo = nodoaux
                
                while nodoaux.siguiente is not None:
                    nodoPenultimo = nodoaux
                    nodoaux = nodoaux.siguiente
                
                nodoPenultimo.siguiente = None
        else:
            if self.raiz.username is username:
                if self.raiz.siguiente is not None:
                    self.raiz = self.raiz.siguiente
                else:
                    self.raiz = Nodo()
            else:
                nodoaux = self.raiz
                nodoAnterior = nodoaux
                
                while nodoaux.username is not username:
                    nodoAnterior = nodoaux
                    nodoaux = nodoaux.siguiente
                    
                nodoAnterior.siguiente = nodoaux.siguiente
                    
    def findByUsername(self, username):
        nodoaux = self.raiz
        
        while nodoaux.username is not username:
            if nodoaux.siguiente is not None:
                nodoaux = nodoaux.siguiente
            else:
                return None
        return nodoaux
                  
                
    
    def printListaSimpleEnlazada(self):
        nodoAux = self.raiz
        
        cadena = ''
        while True:
            if nodoAux.username is not None:
                cadena += '(' + nodoAux.username + '-' + nodoAux.password + ') -> '
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        print(cadena)
            

nodo1 = Nodo("Pedro", "1234")
nodo2 = Nodo("Juan", "1020")


nuevaListaSimple = ListaSimpleEnlazada()
nuevaListaSimple.append(nodo1)
nuevaListaSimple.append(nodo2)
nuevaListaSimple.append(Nodo("Maria", "2222"))
nuevaListaSimple.printListaSimpleEnlazada()
nuevaListaSimple.pop("Juan")
print("\n ELIMINAR POR USERNAME")
nuevaListaSimple.printListaSimpleEnlazada()
print("\n ELIMINAR ULTIMO")
nuevaListaSimple.pop()
nuevaListaSimple.printListaSimpleEnlazada()

print("\n AGREGANDO")
nuevaListaSimple.append(Nodo("Daniel","11111"))
nuevaListaSimple.append(Nodo("Diego","34433"))
nuevaListaSimple.printListaSimpleEnlazada()

nodoBuscar = nuevaListaSimple.findByUsername("Daniel1")
print("\n BUSQUEDA")
if nodoBuscar is not None:
    print('(' + nodoBuscar.username + '-' + nodoBuscar.password + ')')
else:
    print("No existe usuario dentro de la lista")
    
    

