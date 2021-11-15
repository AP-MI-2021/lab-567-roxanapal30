from Domain.obiect import creeazaobiect, getid

'''
Functia adauga un obiect in lista formata
param:id(int)
param:nume(string)
param:descriere(string)
param:pret(float)
param:locatie(string)
param:lista
param:listaundo
param:listaredo
returnare:listanoua
'''


def adaugaobiect(id, nume, descriere, pret, locatie, lista, listaundo, listaredo):
    for obiect in lista:
        if id== getid(obiect):
            raise ValueError(f"Exista deja un obiect cu id-ul {id}")
    obiect = creeazaobiect(id, nume, descriere, pret, locatie)
    listaundo.append(lista)
    listaredo.clear()
    if lista==None:
        lista=[]
    return lista + [obiect]


'''
Functia sterge un obiect din lista formata dupa id-ul dat de utilizator
param:id(int)
param:lista
param:listaundo
param:listaredo
returnare:listanoua
'''


def stergeobiect(id, lista, listaundo, listaredo):
    listaundo.append(lista)
    listaredo.clear()
    return [obiect for obiect in lista if getid(obiect) != id]


'''
Functia modifica un obiect dupa id-ul dat de utilizator din lista formata
param:id(int)
param:nume(string)
param:descriere(string)
param:pret(float)
param:locatie(string)
param:lista
param:listaundo
param:listaredo
returnare:listanoua
'''


def modificaobiect(id, nume, descriere, pret, locatie, lista, listaundo, listaredo):
    listanoua = []
    listaundo.append(lista)
    listaredo.clear()
    for obiect in lista:
        if getid(obiect) == id:
            obiectnou = creeazaobiect(id, nume, descriere, pret, locatie)
            listanoua.append(obiectnou)
        else:
            listanoua.append(obiect)
    return listanoua


'''
Functia gaseste obiectul din lista cu id-ul cerut si il returneaza
param:id(int)
param:lista
return:obiect
'''


def getbyid(id, lista):
    for obiect in lista:
        if getid(obiect) == id:
            return obiect
    return None
