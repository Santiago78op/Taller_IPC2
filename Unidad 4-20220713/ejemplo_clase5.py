#LISTA ENLAZADA DE USUARIOS Y PASSWORD

import os;

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
    
    
    def ordenar(self):
        aux2 = self.raiz
        
        while (aux2 is not None):
            aux1 = aux2.siguiente
            while (aux1 is not None):
                if (aux1.username < aux2.username):
                    auxT = Nodo(aux2.username, aux2.password)
                    aux2.username = aux1.username
                    aux2.password = aux1.password
                    aux1.username = auxT.username
                    aux1.password = auxT.password
                aux1 = aux1.siguiente
            aux2 = aux2.siguiente
            
    def graficar(self):
        nodoAux = self.raiz
        
        cadena = 'digraph { '
        while True:
            if nodoAux.username is not None:
                cadena += nodoAux.username
                if nodoAux.siguiente is not None:
                    cadena += ' -> '
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        cadena += "}"
        file = open("./nodo.dot", "w+")
        file.write(cadena)
        file.close()
        os.system('dot -Tpng nodo.dot -o nodo.png')
        
        
            

nodo1 = Nodo("Juan", "1234")
nodo2 = Nodo("Daniel", "1020")
nodo3 = Nodo("Pedro", "1020")
nodo4 = Nodo("Maria", "1020")
nodo5 = Nodo("Karla", "1020")


nuevaListaSimple = ListaSimpleEnlazada()
nuevaListaSimple.append(nodo1)
nuevaListaSimple.append(nodo2)
nuevaListaSimple.append(nodo3)
nuevaListaSimple.append(nodo4)
nuevaListaSimple.append(nodo5)
nuevaListaSimple.graficar()

# nuevaListaSimple.printListaSimpleEnlazada()
# nuevaListaSimple.ordenar()
# nuevaListaSimple.printListaSimpleEnlazada()

# nuevaListaSimple.append(Nodo("Maria", "2222"))
# nuevaListaSimple.printListaSimpleEnlazada()
# nuevaListaSimple.pop("Juan")
# print("\n ELIMINAR POR USERNAME")
# nuevaListaSimple.printListaSimpleEnlazada()
# print("\n ELIMINAR ULTIMO")
# nuevaListaSimple.pop()
# nuevaListaSimple.printListaSimpleEnlazada()

# print("\n AGREGANDO")
# nuevaListaSimple.append(Nodo("Daniel","11111"))
# nuevaListaSimple.append(Nodo("Diego","34433"))
# nuevaListaSimple.printListaSimpleEnlazada()

# nodoBuscar = nuevaListaSimple.findByUsername("Daniel1")
# print("\n BUSQUEDA")
# if nodoBuscar is not None:
#     print('(' + nodoBuscar.username + '-' + nodoBuscar.password + ')')
# else:
#     print("No existe usuario dentro de la lista")


class NodoDobleEnlazado:
    def __init__(self, username = None, password = None, siguiente = None, anterior = None):
        self.username = username
        self.password = password
        self.siguiente = siguiente
        self.anterior = anterior
        

class ListaDoblementeEnlazada:
    def __init__(self):
        self.raiz = NodoDobleEnlazado()
        self.ultimo = self.raiz
    
    def append(self, nuevoNodo):
        if self.raiz.username is None:
            self.raiz = nuevoNodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoNodo
            nuevoNodo.anterior = self.raiz
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            nuevoNodo.anterior = self.ultimo
            self.ultimo = nuevoNodo
            
    def printDobleEnlazada(self):
        nodoaux = self.raiz
        
        cadena = ''
        while True:
            if nodoaux.username is not None:
                cadena += "( " + nodoaux.username + " " + nodoaux.password + " )"
                if nodoaux.siguiente is not None:
                    cadena += " -> "
                    nodoaux = nodoaux.siguiente
                else:
                    break
            else:
                break
        
        print(cadena)
    
    def printDobleEnlazadaReversa(self):
        nodoaux = self.ultimo
        
        cadena = ''
        while True:
            if nodoaux.username is not None:
                cadena += "( " + nodoaux.username + " " + nodoaux.password + " )"
                if nodoaux.anterior is not None:
                    cadena += " -> "
                    nodoaux = nodoaux.anterior
                else:
                    break
            else:
                break
        
        print(cadena)
        
        
        
# nodoDoble1 = NodoDobleEnlazado("Daniel", "1020")
# nodoDoble2 = NodoDobleEnlazado("Carlos", "2020")
# nodoDoble3 = NodoDobleEnlazado("Maria", "3030")

# listaDobleEnlazada = ListaDoblementeEnlazada()
# listaDobleEnlazada.append(nodoDoble1)
# listaDobleEnlazada.append(nodoDoble2)
# listaDobleEnlazada.append(nodoDoble3)

# listaDobleEnlazada.printDobleEnlazada()
# listaDobleEnlazada.printDobleEnlazadaReversa()

        
        
    
        
    
    
    

