from Logic.crud import adauga_obiect, sterge_obiect
from Tests.all_tests import all_tests


def main():
    all_tests()
    while True:
        print("1. Adaugare inventar.")
        print("2. Stergere inventar.")
        print("3. Iesire")
        op=input(int("Alege optiunea"))
        if op==1:
            id = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            descriere = input("Dati descrierea: ")
            pret = float(input("Dati pretul: "))
            locatie = input("Dati locatia: ")
            return adauga_obiect(id, nume, descriere, pret, locatie)
        elif op==2:
            id = input("Dati id-ul obiectul din inventar ce trebuie sters: ")
            return sterge_obiect(id)
        else:
            break

