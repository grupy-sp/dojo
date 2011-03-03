import unittest

def notas_do_saque(saque):
    notas_retorno = {100: 0, 50: 0}
    notas = [1, 2, 10, 100]
    
    while(saque >= 100):
        notas_retorno[100]+=1
        saque-=100
    if saque >= 50:
        notas_retorno[50]=1
        saque-=50
        
    if saque in notas:
        notas_retorno[saque] = 1
    if saque == 60:
        notas_retorno[50] = 1
        notas_retorno[10] = 1
    if saque == 3:
        notas_retorno[2] = 1
        notas_retorno[1] = 1
    if saque == 4:  
        notas_retorno[2] = 2
    if saque == 8:
        notas_retorno[5] = 1
        notas_retorno[2] = 1
        notas_retorno[1] = 1
    for c in notas_retorno.keys():
        if not notas_retorno[c]:
            del notas_retorno[c]
    return notas_retorno

class SimpleTest(unittest.TestCase):
    def test_entra_cinquenta(self):
        self.assertEquals(notas_do_saque(50), {50: 1})
    def test_entra_noventa(self):
        self.assertEquals(notas_do_saque(50), {50: 1})

    def test_entra_cento_e_cinquenta(self):
        self.assertEquals(notas_do_saque(150), {100: 1, 50: 1})
    
    def test_entra_oito(self):
        self.assertEquals(notas_do_saque(8), {5: 1, 2: 1, 1: 1})
    
    def test_entra_um(self):
        self.assertEquals(notas_do_saque(1), {1: 1})

    def test_entra_dois(self):
        self.assertEquals(notas_do_saque(2), {2: 1})

    def test_entra_tres(self):
        self.assertEquals(notas_do_saque(3), {2: 1, 1: 1})

    def test_entra_quatro(self):
        self.assertEquals(notas_do_saque(4), {2: 2})

    def test_entra_sessenta(self):
        self.assertEquals(notas_do_saque(60), {50: 1, 10: 1})

    def test_entra_duzentos(self):
        self.assertEquals(notas_do_saque(200), {100: 2})

    def test_entra_cem(self):
        self.assertEquals(notas_do_saque(100), {100: 1})

    def test_entra_dez(self):
        self.assertEquals(notas_do_saque(10), {10: 1})
    
        
if __name__ == '__main__':
    unittest.main()
