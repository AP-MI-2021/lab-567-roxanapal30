from Domain.obiect import creeazaobiect, getdescriere
from Logic.Concatenarestring import concatenare


def testconcatenare():
    lista = []
    obiect = creeazaobiect(1, "mara", "draguta", 50, "casa")
    lista.append(obiect)
    obiect = creeazaobiect(2, "caine", "maro", 30, "casa")
    lista.append(obiect)
    lista = concatenare("ana", 30, lista,[],[])
    assert getdescriere(lista[0]) == "draguta ana"
    assert getdescriere(lista[1]) == "maro"
