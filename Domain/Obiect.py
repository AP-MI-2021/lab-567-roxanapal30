def creazaobiect(id, nume, descriere, pret_achizitie, locatie):
    '''
    creeaza o lista ce reprezinta un obiect
    :param id:
    :param nume:
    :param descriere:
    :param pret_achizitie:
    :param locatie:
    :return:
    '''
    return [id, nume, descriere, pret_achizitie, locatie]



def getid(lst):
    '''

    :param obiect:
    :return:
    '''
    return lst[0]


def getnume(lst):
    '''

    :param obiect:
    :return:
    '''
    return lst[1]


def getdescriere(lst):
    '''

    :param obiect:
    :return:
    '''
    return lst[2]


def getpret_achizitie(lst):
    '''

    :param obiect:
    :return:
    '''
    return lst[3]


def getlocatie(lst):
    '''

    :param obiect:
    :return:
    '''
    return lst[4]