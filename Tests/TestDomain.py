from Domain.obiect import creeazaobiect, getid, getnume, getdescriere, getpret, getlocatie


def testobiect():
    obiect=creeazaobiect(1,"perna","alba",20,"casa")
    assert getid(obiect) == 1
    assert getnume(obiect)=="perna"
    assert getdescriere(obiect)=="alba"
    assert getpret(obiect)==20
    assert getlocatie(obiect)=="casa"

    obiect=creeazaobiect(2,"casa","mare",500,"aici")
    assert getid(obiect)==2
    assert getnume(obiect)=="casa"
    assert getdescriere(obiect)=="mare"
    assert getpret(obiect)==500
    assert getlocatie(obiect)=="aici"
