from Domain.obiect import creeazaobiect, getid
from Logic.CRUD import adaugaobiect
from Logic.undosiredo import undo, redo


def testundosiredo():
    lista=[]
    listaundo=[]
    listaredo=[]
    obiect = creeazaobiect(1, "mouse", "negru", 30, "casa")
    lista.append(obiect)
    lista=adaugaobiect(2, "masa", "alba", 50, "casa",lista,listaundo,listaredo)
    lista=undo(listaundo,listaredo, lista)
    assert len(lista)==1
    lista=redo(listaundo,listaredo,lista)
    assert len(lista)==2
    assert getid(lista[1])==2
    