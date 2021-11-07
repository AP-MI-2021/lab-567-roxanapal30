from Domain.obiect import getpret

def gasestepret(obiect):
    return getpret(obiect)

def ordonarepret(lista):
    return sorted(lista,key=gasestepret)