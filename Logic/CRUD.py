from Domain.obiect import creeazaobiect, getid


def adaugaobiect(id, nume, descriere, pret, locatie, lista):
    obiect = creeazaobiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def stergeobiect(id, lista):
    return [obiect for obiect in lista if getid(obiect) != id]


def modificaobiect(id, nume, descriere, pret, locatie, lista):
    listanoua = []
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
