from Domain.obiect import toString
from Logic.CRUD import adaugaobiect, stergeobiect, modificaobiect
from Logic.Concatenarestring import concatenare
from Logic.Mutare import mutare_locatie, verificarelocatieexistenta


def command(lista):
    printMenu()
    string=input("Dati comenzile despartite prin';' cu toate atributele necesare despartite prin ',':")
    comenzi=string.split(";")
    for s in comenzi:
        subcomenzi = s.split(",")
        if subcomenzi[0]=="add":
            id = subcomenzi[1]
            nume = subcomenzi[2]
            descriere=subcomenzi[3]
            pret = subcomenzi[4]
            locatie = subcomenzi[5]
            if descriere is None:
                print("Imposibil")
                break
            if len(locatie)!=4:
                print("Imposibil")
                break
            lista=adaugaobiect(id, nume, descriere, pret, locatie, lista)
        elif subcomenzi[0]=="delete":
            id=subcomenzi[1]
            lista= stergeobiect(id, lista)
        elif subcomenzi[0]=="modify":
            id = subcomenzi[1]
            nume = subcomenzi[2]
            descriere = subcomenzi[3]
            pret = subcomenzi[4]
            locatie = subcomenzi[5]
            if descriere is None:
                print("Imposibil")
                break
            if len(locatie) != 4:
                print("Imposibil")
                break
            lista=modificaobiect(id, nume, descriere, pret, locatie)
        elif subcomenzi[0]=="move":
            locatieinitiala =subcomenzi[1]
            locatiefinala = subcomenzi[2]
            if not verificarelocatieexistenta(locatieinitiala, lista):
                print("Imposibil")
                break
            if len(locatiefinala) != 4:
                print("Imposibil")
                break
            lista=mutare_locatie(locatieinitiala, locatiefinala, lista)
        elif subcomenzi[0]=="concat":
            sir = subcomenzi[1]
            suma = subcomenzi[2]
            lista=concatenare(sir, suma, lista)
        elif subcomenzi[0]=="showall":
            for obiect in lista:
                print(toString(obiect))
    return lista


def printMenu():
    print("1.add,id,nume,descriere,pret,locatie; :")
    print("2.delete,id; :")
    print("3.modify,id,nume,descriere,pret,locatie; :")
    print("4.move,locatieinitiala,locatiefinala; :")
    print("5.concat,sir,suma; :")
    print("6.showall")