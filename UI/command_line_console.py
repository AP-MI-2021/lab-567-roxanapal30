from Domain.obiect import toString, getid
from Logic.CRUD import adaugaobiect, stergeobiect, modificaobiect
from Logic.Concatenarestring import concatenare
from Logic.Mutare import mutare_locatie, verificarelocatieexistenta
from Logic.Celmaimare import celmaimare
from Logic.Ordonareaobiectelor import ordonarepret
from Logic.Sumepreturi import sumepreturi


def command(lista):
    printMenu()
    string = input("Dati comenzile despartite prin';' cu toate atributele necesare despartite prin ',':")
    comenzi = string.split(";")
    for s in comenzi:
        subcomenzi = s.split(",")
        if subcomenzi[0] == "add":
            id = int(subcomenzi[1])
            nume = subcomenzi[2]
            descriere = subcomenzi[3]
            pret = float(subcomenzi[4])
            locatie = subcomenzi[5]
            if descriere is None:
                print("Imposibil, descrierea nu poate fi null")
                break
            if pret<0:
                print("Imposibil,pretul trebuie sa fie pozitiv")
                break
            if len(locatie) != 4:
                print("Imposibil, locatia trebuie sa aiba 4 caractere")
                break
            lista = adaugaobiect(id, nume, descriere, pret, locatie, lista)
        elif subcomenzi[0] == "delete":
            id = int(subcomenzi[1])
            if id > getid(lista[len(lista) - 1]):
                print("Imposibil,id-ul trebuie sa existe in lista")
                break
            lista = stergeobiect(id, lista)
        elif subcomenzi[0] == "modify":
            id =int(subcomenzi[1])
            nume = subcomenzi[2]
            descriere = subcomenzi[3]
            pret = float(subcomenzi[4])
            locatie = subcomenzi[5]
            if descriere is None:
                print("Imposibil, descrierea nu poate fi null")
                break
            if pret<0:
                print("Imposibil,pretul trebuie sa fie pozitiv")
                break
            if len(locatie) != 4:
                print("Imposibil, locatia trebuie sa aiba 4 caractere")
                break
            lista = modificaobiect(id, nume, descriere, pret, locatie)
        elif subcomenzi[0] == "move":
            locatieinitiala = subcomenzi[1]
            locatiefinala = subcomenzi[2]
            if not verificarelocatieexistenta(locatieinitiala, lista):
                print("Imposibil, locatia trebuie sa existe in lista")
                break
            if len(locatiefinala) != 4:
                print("Imposibil, locatia trebuie sa aiba 4 caractere")
                break
            lista = mutare_locatie(locatieinitiala, locatiefinala, lista)
        elif subcomenzi[0] == "concat":
            sir = subcomenzi[1]
            suma = float(subcomenzi[2])
            lista = concatenare(sir, suma, lista)
        elif subcomenzi[0] == "biggest":
            dex={}
            dex=celmaimare(lista)
            if dex is None:
                print("Nu exista inca obiecte in lista")
            else:
                print(dex)
        elif subcomenzi[0]=="ordonare":
            lista=ordonarepret(lista)
        elif subcomenzi[0]=="show":
            dex = {}
            dex = sumepreturi(lista)
            if dex is None:
                print("Nu exista inca obiecte in lista")
            else:
                print(dex)
        elif subcomenzi[0] == "showall":
            for obiect in lista:
                print(toString(obiect))
        elif subcomenzi[0] !='':
            print("nu exista comanda aleasa")
    return lista



def printMenu():
    print("Lista cu comenzi: ")
    print("add,id,nume,descriere,pret,locatie;")
    print("delete,id;")
    print("modify,id,nume,descriere,pret,locatie;")
    print("move,locatieinitiala,locatiefinala;")
    print("biggest;")
    print("concat,sir,suma;")
    print("ordonare;")
    print("show all prices for every location")
    print("showall;")
