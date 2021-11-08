

from Domain.obiect import toString, getid
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
    while True:
        id = input("Dati id-ul: ")
        if len(id)>0:
            if int(id)>0:
                break
    id=int(id)
    nume = input("Dati numele: ")
    while True:
        descriere = input("Dati descriere,ea nu poate fi nula: ")
        if len(descriere) > 0:
            break
    while True:
        pret = input("Dati pretul,acesta trebuie sa fie pozitiv: ")
        if len(pret) > 0:
            if float(pret) >= 0:
                break
    pret=float(pret)
    locatie = input("Dati locatia: ")
    if len(locatie) != 4:
        while True:
            locatie = input("Dati locatia, locatia trebuie sa aiba 4 caractere: ")
            if len(locatie) == 4:
                break
    return adaugaobiect(id, nume, descriere, pret, locatie, lista,listaundo,listaredo)


def UIstregereobiect(lista,listaundo,listaredo):
    id = int(input("Dati id-ul pentru obiectul pe care vreti sa il stergeti: "))
    if id> getid(lista[len(lista)-1]):
        while True:
            id = int(input("Dati id-ul pentru obiectul pe care vreti sa il stergeti,acesta trebuie sa existe in lista: "))
            if id <= getid(lista[len(lista)-1]):
                break
    return stergeobiect(id, lista,listaundo,listaredo)


def UImodificaobiect(lista,listaundo,listaredo):
    id = int(input("Dati id-ul pentru obiectul pe care vreti sa il modificati: "))
    if id> getid(lista[len(lista)-1]):
        while True:
            id = int(input("Dati id-ul pentru obiectul pe care vreti sa il stergeti,acesta trebuie sa existe in lista: "))
            if id <= getid(lista[len(lista)-1]):
                break
    nume = input("Dati noul nume: ")
    while True:
        descriere = input("Dati noua descriere,ea nu poate fi nenula: ")
        if len(descriere) > 0:
            break
    while True:
        pret = input("Dati pretul,acesta trebuie sa fie pozitiv: ")
        if len(pret) > 0:
            if float(pret) >= 0:
                break
    pret=float(pret)
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
        while True:
            locatieinitiala=input("Dati locatia din care mutati obiectele, locatia trebuie sa fie una deja existenta in "
                              "lista: ")
            if verificarelocatieexistenta(locatieinitiala,lista):
                break
    locatiefinala=input("Dati locatia in care mutati obiectele: ")
    if len(locatiefinala) != 4:
        while True:
            locatiefinala = input("Dati noua locatie, locatia trebuie sa aiba 4 caractere: ")
            if len(locatiefinala) == 4:
                break
    return mutare_locatie(locatieinitiala,locatiefinala,lista,listaundo,listaredo)

def UIconcatenare(lista,listaundo,listaredo):
    sir=input("Dati sir pentru concatenare: ")
    suma=int(input("Dati suma de la care vreti sa concatenati,nu si inclusiv: "))
    return concatenare(sir,suma,lista,listaundo,listaredo)

def UIcelmaimare(lista):
    return celmaimare(lista)

def UIOrdonareaobiectelor(lista,listaundo,listaredo):
    return ordonarepret(lista,listaundo,listaredo)

def UISumepreturi(lista):
    return sumepreturi(lista)

def showAll(lista):
    if len(lista)==0:
        print("Nu exista obiecte in lista")
    else:
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
