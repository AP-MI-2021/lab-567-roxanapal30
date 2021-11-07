

from Domain.obiect import toString
from Logic.CRUD import stergeobiect, modificaobiect, adaugaobiect
from Logic.Concatenarestring import concatenare
from Logic.Mutare import verificarelocatieexistenta, mutare_locatie
from Logic.Celmaimare import celmaimare
from Logic.Ordonareaobiectelor import ordonarepret
from Logic.Sumepreturi import sumepreturi


def printMenu():
    print("1.Adaugare obiect")
    print("2.Stergere obiect")
    print("3.Modificare obiect")
    print("4.Mutare dintr-o locatie in alta")
    print("5.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("6.Determinarea celui mai mare preț pentru fiecare locație")
    print("7.Ordonarea obiectelor crescător după prețul de achiziție")
    print("8.Afișarea sumelor prețurilor pentru fiecare locație")
    print("9.Arata obiectele")
    print("10.Iesire")


def UIadaugareobiect(lista):
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
    return adaugaobiect(id, nume, descriere, pret, locatie, lista)


def UIstregereobiect(lista):
    id = input("Dati id-ul pentru obiectul pe care vreti sa il stergeti: ")
    return stergeobiect(id, lista)


def UImodificaobiect(lista):
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
    return modificaobiect(id, nume, descriere, pret, locatie,lista)

def UImutarelocatie(lista):
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
    return mutare_locatie(locatieinitiala,locatiefinala,lista)

def UIconcatenare(lista):
    sir=input("Dati sir pentru concatenare: ")
    suma=int(input("Dati suma de la care vreti sa concatenati: "))
    return concatenare(sir,suma,lista)

def UIcelmaimare(lista):
    return celmaimare(lista)

def UIOrdonareaobiectelor(lista):
    return ordonarepret(lista)

def UISumepreturi(lista):
    return sumepreturi(lista)

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def runMenu(lista):
    while True:
        printMenu()
        op = int(input("Dati optiunea: "))
        if op == 1:
            lista = UIadaugareobiect(lista)
        elif op == 2:
            lista = UIstregereobiect(lista)
        elif op == 3:
            lista = UImodificaobiect(lista)
        elif op==4:
            lista=UImutarelocatie(lista)
        elif op==5:
            lista=UIconcatenare(lista)
        elif op==6:
            dex={}
            dex=UIcelmaimare(lista)
            print(dex)
        elif op==7:
            lista=UIOrdonareaobiectelor(lista)
        elif op==8:
            dex={}
            dex=UISumepreturi(lista)
            print(dex)
        elif op == 9:
            showAll(lista)
        elif op == 10:
            break
        else:
            print("Optiune inexistenta, reincercati")
    return lista
