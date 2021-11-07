from os import remove

from Domain.obiect import getpret, getlocatie

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






