from Domain.obiect import creeazaobiect, getpret
from Logic.Ordonareaobiectelor import ordonarepret


def testordonareobiecte():
    lista=[]
    obiect=creeazaobiect(1,"caine","maro",20,"casa")
    lista.append(obiect)
    obiect = creeazaobiect(2, "scaun", "maro", 40, "casa")
    lista.append(obiect)
    obiect = creeazaobiect(3, "paine", "maro", 30, "cana")
    lista.append(obiect)
    listanoua=ordonarepret(lista,[],[])
    assert getpret(listanoua[0])==20
    assert getpret(listanoua[1]) == 30
    assert getpret(listanoua[2]) == 40