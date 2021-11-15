from Domain.obiect import creeazaobiect, getlocatie, getdescriere
from Logic.CRUD import adaugaobiect, stergeobiect, modificaobiect
from Logic.Concatenarestring import concatenare
from Logic.Mutare import mutare_locatie
from Logic.Ordonareaobiectelor import ordonarepret
from Logic.undosiredo import undo, redo


def testundosiredo():
    lista = []
    listaundo = []
    listaredo = []
    assert len(lista) == 0
    ob1 = creeazaobiect(1, "mouse", "negru", 30, "casa")
    ob2 = creeazaobiect(2, "masa", "alba", 50, "casa")
    ob3 = creeazaobiect(3, "scaun", "maro", 70, "casa")
    lista = adaugaobiect(1, "mouse", "negru", 30, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert ob2 in lista
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    lista = undo(listaundo, listaredo, lista)
    assert not lista
    lista = undo(listaundo, listaredo, lista)
    assert not lista
    lista = adaugaobiect(1, "mouse", "negru", 30, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista = redo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert ob2 in lista
    assert ob3 in lista
    lista = undo(listaundo, listaredo, lista)
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    lista = redo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert ob2 in lista
    lista = redo(listaundo, listaredo, lista)
    assert ob3 in lista
    lista = undo(listaundo, listaredo, lista)
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    ob4 = creeazaobiect(4, "perna", "alba", 40, "casa")
    lista = adaugaobiect(4, "perna", "alba", 40, "casa", lista, listaundo, listaredo)
    lista = redo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert ob4 in lista
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    lista = undo(listaundo, listaredo, lista)
    assert not lista
    lista = redo(listaundo, listaredo, lista)
    lista = redo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert ob4 in lista
    lista = redo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert ob4 in lista
    # stergere
    lista = []
    listaundo = []
    listaredo = []
    ob1 = creeazaobiect(1, "mouse", "negru", 30, "casa")
    ob2 = creeazaobiect(2, "masa", "alba", 50, "casa")
    ob3 = creeazaobiect(3, "scaun", "maro", 70, "casa")
    lista = adaugaobiect(1, "mouse", "negru", 30, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista = stergeobiect(1, lista, listaundo, listaredo)
    assert ob1 not in lista
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    # modificare
    lista = []
    listaundo = []
    listaredo = []
    ob1 = creeazaobiect(1, "mouse", "negru", 30, "casa")
    ob2 = creeazaobiect(2, "masa", "alba", 50, "casa")
    ob3 = creeazaobiect(3, "scaun", "maro", 70, "casa")
    obmodificat = creeazaobiect(1, "patura", "alba", 40, "casa")
    lista = adaugaobiect(1, "mouse", "negru", 30, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista = modificaobiect(1, "patura", "alba", 40, "casa", lista, listaundo, listaredo)
    assert obmodificat in lista
    assert ob1 not in lista
    lista = undo(listaundo, listaredo, lista)
    assert ob1 in lista
    assert obmodificat not in lista
    lista = redo(listaundo, listaredo, lista)
    assert obmodificat in lista
    assert ob1 not in lista
    # ordonare
    lista = []
    listaundo = []
    listaredo = []
    ob1 = creeazaobiect(1, "mouse", "negru", 60, "casa")
    ob2 = creeazaobiect(2, "masa", "alba", 50, "casa")
    ob3 = creeazaobiect(3, "scaun", "maro", 70, "casa")
    lista = adaugaobiect(1, "mouse", "negru", 60, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista = ordonarepret(lista, listaundo, listaredo)
    assert lista[0] == ob2
    assert lista[1] == ob1
    assert lista[2] == ob3
    lista = undo(listaundo, listaredo, lista)
    assert lista[0] == ob1
    assert lista[1] == ob2
    assert lista[2] == ob3
    lista = redo(listaundo, listaredo, lista)
    assert lista[0] == ob2
    assert lista[1] == ob1
    assert lista[2] == ob3
    # mutare
    lista = []
    listaundo = []
    listaredo = []
    ob1 = creeazaobiect(1, "mouse", "negru", 60, "casa")
    ob2 = creeazaobiect(2, "masa", "alba", 50, "casa")
    ob3 = creeazaobiect(3, "scaun", "maro", 70, "casa")
    lista = adaugaobiect(1, "mouse", "negru", 60, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista = mutare_locatie("casa", "cana", lista, listaundo, listaredo)
    assert getlocatie(lista[0]) == "cana"
    assert getlocatie(lista[1]) == "cana"
    assert getlocatie(lista[2]) == "cana"
    lista = undo(listaundo, listaredo, lista)
    assert getlocatie(lista[0]) == "casa"
    assert getlocatie(lista[1]) == "casa"
    assert getlocatie(lista[2]) == "casa"
    lista = redo(listaundo, listaredo, lista)
    assert getlocatie(lista[0]) == "cana"
    assert getlocatie(lista[1]) == "cana"
    assert getlocatie(lista[2]) == "cana"
    # concatenare
    lista = []
    listaundo = []
    listaredo = []
    ob1 = creeazaobiect(1, "mouse", "negru", 60, "casa")
    ob2 = creeazaobiect(2, "masa", "alba", 50, "casa")
    ob3 = creeazaobiect(3, "scaun", "maro", 70, "casa")
    lista = adaugaobiect(1, "mouse", "negru", 60, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(2, "masa", "alba", 50, "casa", lista, listaundo, listaredo)
    lista = adaugaobiect(3, "scaun", "maro", 70, "casa", lista, listaundo, listaredo)
    lista=concatenare("ana",60,lista,listaundo,listaredo)
    assert getdescriere(lista[2])=="maro ana"
    lista=undo(listaundo,listaredo,lista)
    assert getdescriere(lista[2])=="maro"
    lista=redo(listaundo,listaredo, lista)
    assert getdescriere(lista[2]) == "maro ana"
