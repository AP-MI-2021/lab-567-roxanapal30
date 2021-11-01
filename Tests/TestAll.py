from Tests.TestCRUD import testadaugaobiect, teststergereobiect, testmodificaobiect
from Tests.TestConcatenare import testconcatenare
from Tests.TestDomain import testobiect
from Tests.TestMutare import testmutare


def TestAll():
    testobiect()
    testadaugaobiect()
    teststergereobiect()
    testmodificaobiect()
    testmutare()
    testconcatenare()
