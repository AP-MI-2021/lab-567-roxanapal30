from Domain.obiect import getlocatie, creeazaobiect, getid, getnume, getdescriere, getpret


'''
Functia schimba locatiile tuturor obiectelor care locatie egala cu cea introdusa de utilizator cu alta introdusa tot de utilizator
param:locatieinitiata(string)
param:locatiefinala(string)
param:lista
param:listaundo
param:listaredo
returnare:listanoua
'''
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

'''
Functia verifica daca locatie introdusa de utilizator exista in lista
param:locatie(string)
param:lista
'''
def verificarelocatieexistenta(locatie,lista):
    for obiect in lista:
        if getlocatie(obiect)==locatie:
            return True
    return False

