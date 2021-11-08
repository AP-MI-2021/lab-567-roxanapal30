from Domain.obiect import getlocatie, creeazaobiect, getid, getnume, getdescriere, getpret


def mutare_locatie(locatiainitiala,locatiafinala,lista,listaundo,listaredo):
    listanoua=[]
    listaundo.append(lista)
    listaredo.clear()
    for obiect in lista:
        if getlocatie(obiect)!=locatiainitiala:
            listanoua.append(obiect)
        else:
            obiectnou= creeazaobiect(getid(obiect),getnume(obiect),getdescriere(obiect),getpret(obiect),locatiafinala)
            listanoua.append(obiectnou)
    return listanoua

def verificarelocatieexistenta(locatie,lista):
    for obiect in lista:
        if getlocatie(obiect)==locatie:
            return True
    return False

