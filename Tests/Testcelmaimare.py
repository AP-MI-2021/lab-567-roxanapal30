from Domain.obiect import creeazaobiect
from Logic.Celmaimare import celmaimare


def testcelmaimare():
    obiect=creeazaobiect(1,"mouse","negru",30,"casa")
    lista=[]
    lista.append(obiect)
    obiect=creeazaobiect(2,"masa","alba",50,"casa")
    lista.append(obiect)
    obiect = creeazaobiect(3, "scaun", "maro", 70, "cana")
    lista.append(obiect)
    obiect = creeazaobiect(4, "casti", "alba", 40, "casa")
    lista.append(obiect)
    dex={}
    dex=celmaimare(lista)
    assert dex["casa"]==50
    assert dex["cana"]==70