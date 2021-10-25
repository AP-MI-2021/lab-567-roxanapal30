from Logic.crud import adauga_obiect, sterge_obiect


def menu_crud(lst_obiect):
    while True:
        print("1. Adaugare in inventar.")
        print("2. Citeste din inventar")
        print("3. Modificare obiect")
        print("4. Stergere in inventar.")
        print("x. Iesire")
        op=input("alegeti optiunea:")
        if op =='1':
            id = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            descriere = input("Dati descrierea: ")
            pret = float(input("Dati pretul: "))
            locatie = input("Dati locatia: ")
            return adauga_obiect(lst_obiect,id, nume, descriere, pret, locatie)
        elif op =='4':
            id = input("Dati id-ul obiectul din inventar ce trebuie sters: ")
            return sterge_obiect(lst_obiect,id)
        elif op == 'x':
            break
