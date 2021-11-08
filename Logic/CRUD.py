from Domain.obiect import creeazaobiect, getid


def adaugaobiect(id, nume, descriere, pret, locatie, lista,listaundo,listaredo):
    obiect = creeazaobiect(id, nume, descriere, pret, locatie)
    listaundo.append(lista)
    listaredo.clear()
    return lista + [obiect]


def stergeobiect(id, lista,listaundo,listaredo):
    listaundo.append(lista)
    listaredo.clear()
    return [obiect for obiect in lista if getid(obiect) != id]


def modificaobiect(id, nume, descriere, pret, locatie, lista,listaundo,listaredo):
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


def getbyid(id, lista):
    for obiect in lista:
        if getid(obiect) == id:
            return obiect
    return None
