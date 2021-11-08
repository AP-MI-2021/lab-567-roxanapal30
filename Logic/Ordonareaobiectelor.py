from Domain.obiect import getpret

def gasestepret(obiect):
    return getpret(obiect)

'''
Functia ordoneaza lista noastra crescator dupa preturile din ea
param:lista
param:listaundo
param:listaredo
returnare:listanoua
'''
def ordonarepret(lista,listaundo,listaredo):
    listaundo.append(lista)
    listaredo.clear()
    return sorted(lista,key=gasestepret)