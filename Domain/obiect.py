def creeazaobiect(id,nume,descriere,pret,locatie):
    '''

    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :return:
    '''

    return[
        id,
        nume,
        descriere,
        pret,
        locatie,
    ]

def getid(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect[0]

def getnume(obiect):
    return obiect[1]

def getdescriere(obiect):
    return obiect[2]

def getpret(obiect):
    return obiect[3]

def getlocatie(obiect):
    return obiect[4]

def toString(obiect):
    return "Id:{}, Nume:{},Descriere:{},Pret:{},Locatie:{}".format(
        getid(obiect),
        getnume(obiect),
        getdescriere(obiect),
        getpret(obiect),
        getlocatie(obiect),
    )


