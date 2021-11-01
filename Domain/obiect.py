def creeazaobiect(id,nume,descriere,pret,locatie):
    '''

    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :return:
    '''

    return{
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret":pret,
        "locatie":locatie,
    }

def getid(obiect):
    '''

    :param obiect:
    :return:
    '''
    return obiect["id"]

def getnume(obiect):
    return obiect["nume"]

def getdescriere(obiect):
    return obiect["descriere"]

def getpret(obiect):
    return obiect["pret"]

def getlocatie(obiect):
    return obiect["locatie"]

def toString(obiect):
    return "Id:{}, Nume:{},Descriere:{},Pret:{},Locatie:{}".format(
        getid(obiect),
        getnume(obiect),
        getdescriere(obiect),
        getpret(obiect),
        getlocatie(obiect),
    )


