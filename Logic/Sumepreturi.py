
from Domain.obiect import getpret, getlocatie

'''
Functia aduna toate sumele din lista de la fiecare locatie existenta
param:lista
returnare:dex
'''
def sumepreturi(lista):
    dex={}
    for obiect in lista:
        locatie=getlocatie(obiect)
        pret=getpret(obiect)
        if locatie not in dex :
            dex[locatie]=pret
        else:
            dex[locatie]=dex[locatie]+pret
    return dex






