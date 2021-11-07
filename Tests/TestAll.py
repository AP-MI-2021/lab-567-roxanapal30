from Tests.TestCRUD import testadaugaobiect, teststergereobiect, testmodificaobiect
from Tests.TestConcatenare import testconcatenare
from Tests.TestDomain import testobiect
from Tests.TestMutare import testmutare
from Tests.Testcelmaimare import testcelmaimare
from Tests.Testordonareaobiectelor import testordonareobiecte
from Tests.Testsumepreturi import testsumepreturi


def TestAll():
    testobiect()
    testadaugaobiect()
    teststergereobiect()
    testmodificaobiect()
    testmutare()
    testconcatenare()
    testcelmaimare()
    testordonareobiecte()
    testsumepreturi()
