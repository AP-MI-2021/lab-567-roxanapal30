from Domain.Obiect import creazaobiect, getid


def adauga_obiect(lst_obiect,id, nume, descriere, pret_achizitie, locatie):
    '''
    adauga un obiect intr-o lista
    :param lst_obiect:lista de obiecte
    :param id:string
    :param nume:string
    :param descriere:string
    :param pret_achizitie:float
    :param locatie:string
    :return: returneaza o lista continand el vechi, cat si noul obiect
    '''
    obiect=creazaobiect(id, nume, descriere, pret_achizitie, locatie)
    return lst_obiect+[obiect]

def citeste_obiect(lst_obiect,id):
    '''
    returneaza obiectul cautat sau none
    :param lst_obiect:
    :param id:
    :return:
    '''
    obiect_cuid=None
    for obiect in lst_obiect:
        if getid(obiect)==id:
            obiect_cuid=obiect
    if obiect_cuid:
        return obiect_cuid
    return None

def modifica_obiect(lst_obiect,newobiect):
    '''

    :param lst_obiect:
    :param id:
    :return:
    '''
    newlistobiect=[]
    for obiect in lst_obiect:
        if getid(obiect)!=getid(newobiect):
            newlistobiect.append(obiect)
        else:
            newlistobiect.append(newobiect)

    return newlistobiect

def sterge_obiect(lst_obiect,id):
    '''

    :param lst_obiect:
    :param id:
    :return:
    '''
    newlistobiect=[]
    for obiect in lst_obiect:
        if getid(obiect)!=id:
            newlistobiect.append(obiect)
    return newlistobiect

