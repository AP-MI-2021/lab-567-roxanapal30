from Domain.obiect import getpret, creeazaobiect, getid, getnume, getlocatie, getdescriere


def concatenare(sir,pret,lista):
    listanoua=[]
    for obiect in lista:
        if getpret(obiect) <= pret:
            listanoua.append(obiect)
        else:

            obiectnou=creeazaobiect(getid(obiect),getnume(obiect),getdescriere(obiect)+' '+ sir,getpret(obiect),getlocatie(obiect))
            listanoua.append(obiectnou)
    return listanoua

