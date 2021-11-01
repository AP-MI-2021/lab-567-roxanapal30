from Tests.TestCRUD import testadaugaobiect, teststergereobiect, testmodificaobiect
from Tests.TestDomain import testobiect


def TestAll():
    testobiect()
    testadaugaobiect()
    teststergereobiect()
    testmodificaobiect()
