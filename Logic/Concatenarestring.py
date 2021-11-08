from Domain.obiect import getpret, creeazaobiect, getid, getnume, getlocatie, getdescriere


def concatenare(sir,pret,lista,listaundo,listaredo):
    listanoua=[]
    listaundo.append(lista)
    listaredo.clear()
    for obiect in lista:
        if getpret(obiect) <= pret:
            listanoua.append(obiect)
        else:

            obiectnou=creeazaobiect(getid(obiect),getnume(obiect),getdescriere(obiect)+' '+ sir,getpret(obiect),getlocatie(obiect))
            listanoua.append(obiectnou)
    return listanoua


