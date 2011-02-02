import unittest
import program

class Test(unittest.TestCase):
    def test_sem_troco(self):
        self.assertEquals({}, program.troco(preco=10,pago=10,caixa={}))
        self.assertEquals({}, program.troco(preco=10,pago=10,caixa={5:1,10:2}))

    def test_nota_50_troco_10(self):
        self.assertEquals({10:1}, program.troco(preco=40,pago=50,caixa={5:1,10:2}))

    def test_nota_50_troco_5(self): 
        self.assertEquals({5:1}, program.troco(preco=45,pago=50,caixa={5:1,10:2}))
    
    def test_nota_100_troco_10(self):
        self.assertEquals({10:1}, program.troco(preco=90,pago=100,caixa={5:1,10:2}))
        
    def test_nota_100_troco_15(self):
        self.assertEquals({10:1, 5:1}, program.troco(preco=85,pago=100,caixa={5:1,10:2}))

    def test_nota_100_troco_20(self):
        self.assertEquals({10:2}, program.troco(preco=85,pago=100,caixa={10:2}))
        
    def test_nota_100_troco_25(self):
        self.assertEquals({10:2, 5:1}, program.troco(preco=75,pago=100,caixa={10:2, 5:1}))
        