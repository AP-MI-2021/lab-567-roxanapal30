from Tests.TestCRUD import testadaugaobiect, teststergereobiect, testmodificaobiect
from Tests.TestDomain import testobiect
from Tests.TestMutare import testmutare


def TestAll():
    testobiect()
    testadaugaobiect()
    teststergereobiect()
    testmodificaobiect()
    testmutare()