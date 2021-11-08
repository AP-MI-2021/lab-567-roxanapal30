from Domain.obiect import getpret, creeazaobiect, getid, getnume, getlocatie, getdescriere

'''
Functia concateneaza un sir dat la fiecare descriere a obiectelor ce au suma egala cu cea data de utilizator
param:sir(string)
param:pret(float)
param:lista
param:listaundo
param:listaredo
returnare:listanoua
'''

def concatenare(sir,pret,lista,listaundo,listaredo):
    listanoua=[]
    listaundo.append(lista)
    listaredo.clear()
    for obiect in lista:
        if getpret(obiect) <= pret:
            listanoua.append(obiect)
        else:

            obiectnou=creeazaobiect(getid(obiect),getnume(obiect),getdescriere(obiect)+' '+ sir,getpret(obiect),getlocatie(obiect))
            listanoua.append(obiectnou)
    return listanoua

'''
Functia verifica daca suma data de utilizator exista in lista 
param:lista
param:suma(float)
'''
def sumaexistenta(lista,suma):
    for obiect in lista:
        if getpret(obiect)==suma:
            return True
    return False



