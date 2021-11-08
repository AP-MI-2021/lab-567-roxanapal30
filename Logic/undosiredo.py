def undo(listaundo, listaredo, lista):
    if listaundo:
        listaredo.append(lista)
        return listaundo.pop()
    return None


def redo(listaundo, listaredo, lista):
    if listaredo:
        listaundo.append(lista)
        return listaredo.pop()
    return None
