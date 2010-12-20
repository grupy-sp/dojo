from roman import decimal2roman


def test1():
    assert decimal2roman(1) == ['I']
    assert decimal2roman(2) == ['I','I'], decimal2roman(2)
    assert decimal2roman(3) == ['I','I','I']

def testQuatro():
    assert decimal2roman(4) == ['I','V'], decimal2roman(4)
    
def testCinco():
    assert decimal2roman(5) == ['V']
    
def testSeisAOito():
    assert decimal2roman(6) == ['V','I']
    assert decimal2roman(7) == ['V','I','I']
    assert decimal2roman(8) == ['V','I','I','I']

def testeQuatorzeEDezesseis():
    assert decimal2roman(14) == ['X','I','V']
    assert decimal2roman(16) == ['X','V','I']
    
def test949():
    assert decimal2roman(949) == ['C','M','X','L','I','X']
    
def test4999():
    assert decimal2roman(4999) == ['M','~V','C','M','X','C','I','X']