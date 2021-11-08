from Domain.obiect import getpret

def gasestepret(obiect):
    return getpret(obiect)

def ordonarepret(lista,listaundo,listaredo):
    listaundo.append(lista)
    listaredo.clear()
    return sorted(lista,key=gasestepret)