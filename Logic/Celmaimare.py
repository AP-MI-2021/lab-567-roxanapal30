from Domain.obiect import getpret, getlocatie
'''
Functia gaseste cea mai mare suma pentru fiecare locatie existenta in lista de obiecte
param:lista
returnare:dex
'''

def celmaimare(lista):
    dex={}
    for obiect in lista:
        pret=getpret(obiect)
        locatie=getlocatie(obiect)
        if locatie not in dex:
            dex[locatie]=pret
        elif pret>dex[locatie]:
            dex[locatie]=pret
    return dex

