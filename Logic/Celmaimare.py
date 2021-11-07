from Domain.obiect import getpret, getlocatie


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

