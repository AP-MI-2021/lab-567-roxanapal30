

from Domain.obiect import toString
from Logic.CRUD import stergeobiect, modificaobiect, adaugaobiect
from Logic.Concatenarestring import concatenare
from Logic.Mutare import verificarelocatieexistenta, mutare_locatie
from Logic.Celmaimare import celmaimare
from Logic.Ordonareaobiectelor import ordonarepret
from Logic.Sumepreturi import sumepreturi
from Logic.undosiredo import undo, redo


def printMenu():
    print("1.Adaugare obiect")
    print("2.Stergere obiect")
    print("3.Modificare obiect")
    print("4.Mutare dintr-o locatie in alta")
    print("5.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("6.Determinarea celui mai mare preț pentru fiecare locație")
    print("7.Ordonarea obiectelor crescător după prețul de achiziție")
    print("8.Afișarea sumelor prețurilor pentru fiecare locație")
    print("u. Undo")
    print("r. Redo")
    print("a.Arata obiectele")
    print("x.Iesire")


def UIadaugareobiect(lista,listaundo,listaredo):
    id = int(input("Dati id-ul: "))
    nume = input("Dati numele: ")
    while True:
        descriere = input("Dati descriere: ")
        if len(descriere) > 0:
            break
    pret = float(input("Dati pretul: "))
    locatie = input("Dati locatia: ")
    if len(locatie) != 4:
        while True:
            locatie = input("Dati locatia, locatia trebuie sa aiba 4 caractere: ")
            if len(locatie) == 4:
                break
    return adaugaobiect(id, nume, descriere, pret, locatie, lista,listaundo,listaredo)


def UIstregereobiect(lista,listaundo,listaredo):
    id = int(input("Dati id-ul pentru obiectul pe care vreti sa il stergeti: "))
    return stergeobiect(id, lista,listaundo,listaredo)


def UImodificaobiect(lista,listaundo,listaredo):
    id = int(input("Dati id-ul pentru obiectul pe care vreti sa il modificati: "))
    nume = input("Dati noul nume: ")
    while True:
        descriere = input("Dati noua descriere: ")
        if len(descriere) > 0:
            break
    pret = float(input("Dati noul pret: "))
    locatie = input("Dati noua locatie: ")
    if len(locatie) != 4:
        while True:
            locatie = input("Dati noua locatie, locatia trebuie sa aiba 4 caractere: ")
            if len(locatie) == 4:
                break
    return modificaobiect(id, nume, descriere, pret, locatie,lista,listaundo,listaredo)

def UImutarelocatie(lista,listaundo,listaredo):
    locatieinitiala=input("Dati locatia din care mutati obiectele: ")
    if not verificarelocatieexistenta(locatieinitiala,lista):
        locatieinitiala=input("Dati locatia din care mutati obiectele, locatia trebuie sa fie una deja existenta in "
                              "lista: ")
    locatiefinala=input("Dati locatia in care mutati obiectele: ")
    if len(locatiefinala) != 4:
        while True:
            locatiefinala = input("Dati noua locatie, locatia trebuie sa aiba 4 caractere: ")
            if len(locatiefinala) == 4:
                break
    return mutare_locatie(locatieinitiala,locatiefinala,lista,listaundo,listaredo)

def UIconcatenare(lista,listaundo,listaredo):
    sir=input("Dati sir pentru concatenare: ")
    suma=int(input("Dati suma de la care vreti sa concatenati: "))
    return concatenare(sir,suma,lista,listaundo,listaredo)

def UIcelmaimare(lista):
    return celmaimare(lista)

def UIOrdonareaobiectelor(lista,listaundo,listaredo):
    return ordonarepret(lista,listaundo,listaredo)

def UISumepreturi(lista):
    return sumepreturi(lista)

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def runMenu(lista,listaundo,listaredo):
    while True:
        printMenu()
        op = input("Dati optiunea: ")
        if op == '1':
            lista = UIadaugareobiect(lista,listaundo,listaredo)
        elif op == '2':
            lista = UIstregereobiect(lista,listaundo,listaredo)
        elif op == '3':
            lista = UImodificaobiect(lista,listaundo,listaredo)
        elif op=='4':
            lista=UImutarelocatie(lista,listaundo,listaredo)
        elif op=='5':
            lista=UIconcatenare(lista,listaundo,listaredo)
        elif op=='6':
            dex={}
            dex=UIcelmaimare(lista)
            print(dex)
        elif op=='7':
            lista=UIOrdonareaobiectelor(lista,listaundo,listaredo)
        elif op=='8':
            dex={}
            dex=UISumepreturi(lista)
            print(dex)
        elif op=='u':
            undo_result=undo(listaundo,listaredo,lista)
            if undo_result is not None:
                lista= undo_result
        elif op=='r':
            redo_result=redo(listaundo,listaredo,lista)
            if redo_result is not None:
                lista=redo_result
        elif op == 'a':
            showAll(lista)
        elif op == 'x':
            break
        else:
            print("Optiune inexistenta, reincercati")
    return lista
