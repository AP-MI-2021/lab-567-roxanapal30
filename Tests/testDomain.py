from Domain.Obiect import creazaobiect, getid, getnume, getdescriere, getpret_achizitie, getlocatie


def testobiect():
    obiect = creazaobiect("1", "calculator", "cautare", 1500, "Cluj")

    assert getid(obiect) == "1"
    assert getnume(obiect) == "calculator"
    assert getdescriere(obiect) == "vcautare"
    assert getpret_achizitie(obiect) == 1500
    assert getlocatie(obiect) == "Cluj"