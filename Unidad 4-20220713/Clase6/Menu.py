from colorama import Fore
from ListaSimpleEnlazada import ListaSimpleEnlazada
from Actor import Actor
from Pelicula import Pelicula
import xml.etree.ElementTree as ET


def menu():
    opcion = ''
    listaActores = ListaSimpleEnlazada()
    while opcion != '8':
        print(Fore.CYAN + "----------------MENU----------------")
        print(Fore.CYAN + "1 -- CREAR ACTOR")
        print(Fore.CYAN + "2 -- IMPRIMIR ACTORES")
        print(Fore.CYAN + "3 -- BUSCAR ACTOR")
        print(Fore.CYAN + "4 -- AGREGAR PELICULA A ACTOR")
        print(Fore.CYAN + "5 -- IMPRIMIR PELICULAS POR ACTOR")
        print(Fore.CYAN + "6 -- CARGAR DESDE ARCHIVO")
        print(Fore.CYAN + "8 -- SALIR")


        opcion = input(Fore.YELLOW + "Seleccione una opcion del menu\n")

        if opcion == '1':
            c = input(Fore.BLUE + "Ingrese actor en el siguiente formato nombre-edad-nacionalidad\n")
            datos = c.split('-')
            nuevoActor = Actor(datos[0], datos[1], datos[2])
            listaActores.append(nuevoActor)
            print(Fore.GREEN + "Se registro el actor con exito!!\n")
        elif opcion == '2':
            listaActores.printListaSimpleEnlazada()
        elif opcion == '3':
            nombre = input(Fore.BLUE + "Ingrese el nombre del actor\n")
            actor = listaActores.buscarActor(nombre)
            if actor is None:
                print(Fore.RED + "El actor no esta registrado")
            else:
                print(Fore.GREEN +  "(" + actor.nombre + " " + actor.edad + " " + actor.nacionalidad + ")\n" )
        elif opcion == '4':
            nombre = input(Fore.BLUE + "Ingrese el nombre del actor\n")
            actor = listaActores.buscarActor(nombre)
            if actor is None:
                print(Fore.RED + "El actor no esta registrado")
            else:
                pelicula = input(Fore.BLUE + "Ingrese pelicula en el siguiente formato nombre-papel-anio-duracion\n")
                datos = pelicula.split('-')
                nuevaPelicula = Pelicula(datos[0],datos[1],datos[2],datos[3])
                actor.listaPeliculas.append(nuevaPelicula)
                print(Fore.GREEN + "Se registro pelicula con exito!!\n")
        elif opcion == '5':
            nombre = input(Fore.BLUE + "Ingrese el nombre del actor\n")
            actor = listaActores.buscarActor(nombre)
            if actor is None:
                print(Fore.RED + "El actor no esta registrado")
            else:
                actor.listaPeliculas.printDobleEnlazada()
        elif opcion == '6':
            nombre = input(Fore.BLUE + "Ingrese el nombre del archivo\n")
            ruta = './' + nombre
            listaActores = cargaArchivo(ruta)
            print(Fore.GREEN + "Se cargo archivo con exito!!\n")


def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    listaActores = ListaSimpleEnlazada()

    for actores in root:
        nuevoActor = Actor(actores.attrib['nombre'], actores.attrib['edad'], actores.attrib['nacionalidad'])
        listaActores.append(nuevoActor)
        for peliculas in actores.iter('pelicula'):
            nuevaPelicula = Pelicula(peliculas.attrib['nombre'],peliculas.attrib['papel'],peliculas.attrib['anio'],peliculas.text )
            nuevoActor.listaPeliculas.append(nuevaPelicula)
    
    return listaActores

menu()
        
