from Domain.obiect import creeazaobiect, getlocatie
from Logic.Mutare import mutare_locatie


def testmutare():
    obiect=creeazaobiect(1,"casa","mare",20,"raft")
    lista=[]
    lista.append(obiect)
    obiect=creeazaobiect(2,"paine","alba",5,"raft")
    lista.append(obiect)
    obiect=creeazaobiect(3,"patura","grea",200,"casa")
    lista.append(obiect)
    lista= mutare_locatie("raft","care",lista,[],[])
    assert getlocatie(lista[0])=="care"
    assert getlocatie(lista[1])=="care"
    assert getlocatie(lista[2])=="casa"
