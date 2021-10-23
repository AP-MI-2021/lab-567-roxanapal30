def creazaobiect(id, nume, descriere, pret_achizitie, locatie):
    '''

    :param id:
    :param nume:
    :param descriere:
    :param pret_achizitie:
    :param locatie:
    :return:
    '''
    return {
        'id':id,
        'nume':nume,
        'descriere':descriere,
        'pret_achizitie':pret_achizitie,
        'locatie':locatie,
    }


def getid(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect['id']


def getnume(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect['nume']


def getdescriere(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect['descriere']


def getpret_achizitie(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect['pret_achizitie']


def getlocatie(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect['locatie']