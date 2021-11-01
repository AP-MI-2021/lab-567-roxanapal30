from Domain.obiect import toString
from Logic.CRUD import stergeobiect, modificaobiect, adaugaobiect


def printMenu():
    print("1.Adaugare obiect")
    print("2.Stergere obiect")
    print("3.Modificare obiect")
    print("4.Arata obiectele")
    print("5.Iesire")


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
    return modificaobiect(id, nume, descriere, pret, locatie)


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
        elif op == 4:
            showAll(lista)
        elif op == 5:
            break
        else:
            print("Optiune gresita, reincercati")
