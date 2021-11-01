from Domain.obiect import creeazaobiect
from Logic.Mutare import mutare_locatie


def testmutare():
    obiect=creeazaobiect(1,"casa","mare",20,"aici")
    lista=[]
    lista.append(obiect)
    obiect=creeazaobiect(2,"paine","alba",5,"raft")
    lista.append(obiect)
    obiect=creeazaobiect(2,"patura","grea",200,"casa")
    lista.append(obiect)
    lista= mutare_locatie("raft","aici",lista)
