from Domain.Obiect import getid, getnume, getdescriere, getpret_achizitie, getlocatie


def testadauga_obiect():
    lista = testadauga_obiect("1", "telefon", "vorbire", 1500, "Cluj", [])

    assert len(lista) == 1
    assert getid(lista[0]) == "1"
    assert getnume(lista[0]) == "calculator"
    assert getdescriere(lista[0]) == "cautare"
    assert getpret_achizitie(lista[0]) == 1500
    assert getlocatie(lista[0]) == "Cluj"

