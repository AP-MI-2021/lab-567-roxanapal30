from Tests.TestAll import TestAll
from UI.command_line_console import command
from UI.console import runMenu


def main():
    TestAll()
    lista=[]
    while True:
        print("1.Consola clasica")
        print("2.command_line_console")
        print("3.Exit")
        op=int(input("Alegeti consola: "))
        if op==1:
            lista=runMenu(lista)
        elif op==2:
            lista=command(lista)
        elif op==3:
            break
        else:
            print("Optiune invalida")


main()
