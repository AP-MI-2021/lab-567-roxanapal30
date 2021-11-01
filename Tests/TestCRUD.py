from Domain.obiect import getid, getnume, getdescriere, getpret, getlocatie
from Logic.CRUD import adaugaobiect, stergeobiect, getbyid, modificaobiect


def testadaugaobiect():
    lista = []
    lista = adaugaobiect(1, "perna", "alba", 20, "casa", lista)

    assert len(lista) == 1
    assert getid(getbyid(1, lista)) == 1
    assert getnume(getbyid(1, lista)) == "perna"
    assert getdescriere(getbyid(1, lista)) == "alba"
    assert getpret(getbyid(1, lista)) == 20
    assert getlocatie(getbyid(1, lista)) == "casa"


def teststergereobiect():
    lista = []
    lista = adaugaobiect(1, "perna", "alba", 20, "casa", lista)
    lista = adaugaobiect(2, "casa", "mare", 500, "aici", lista)
    lista = stergeobiect(1, lista)
    assert len(lista) == 1
    assert getbyid(1, lista) is None
    assert getbyid(2, lista) is not None


def testmodificaobiect():
    lista = []
    lista = adaugaobiect(1, "perna", "alba", 20, "casa", lista)
    lista = adaugaobiect(2, "casa", "mare", 500, "aici", lista)

    lista = modificaobiect(1, "lampa", "mare", 30, "masa", lista)
    obiectnou = getbyid(1, lista)
    assert getid(obiectnou) == 1
    assert getnume(obiectnou) == "lampa"
    assert getdescriere(obiectnou) == "mare"
    assert getpret(obiectnou) == 30
    assert getlocatie(obiectnou) == "masa"

    obiectvechi = getbyid(2, lista)
    assert getid(obiectvechi) == 2
    assert getnume(obiectvechi) == "casa"
    assert getdescriere(obiectvechi) == "mare"
    assert getpret(obiectvechi) == 500
    assert getlocatie(obiectvechi) == "aici"
