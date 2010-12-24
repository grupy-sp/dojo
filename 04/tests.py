import unittest
import xmas

class XmasTest(unittest.TestCase):
    def test_SeparadorDeFamiliasUmNome(self):
        nomes = ["Rodolpho Eckhardt"]
        familias = xmas.separar_familias(nomes)
        self.assertEquals(familias, [set(["Rodolpho Eckhardt"])])

    def test_SeparadorDeFamiliasDoisNomesDif(self):
        nomes = ["Rodolpho Eckhardt", "Carlos Nascimento"]
        familias = xmas.separar_familias(nomes)
        self.assertEquals(familias, [set(["Rodolpho Eckhardt"]), set(["Carlos Nascimento"])])

    def test_SeparadorDeFamiliasDoisNomesMesma(self):
        nomes = ["Rodolpho Eckhardt", "Carlos Eckhardt"]
        familias = xmas.separar_familias(nomes)
        self.assertEquals(familias, [set(["Rodolpho Eckhardt","Carlos Eckhardt"])])

    def test_SeparadorDeFamiliasOrdenadoPorTamanho(self):
        nomes = ["Vanessa Sabino", "Rodolpho Eckhardt", "Carlos Eckhardt"]
        familias = xmas.separar_familias(nomes)
        self.assertEquals(familias, [set(["Rodolpho Eckhardt","Carlos Eckhardt"]), 
                                    set(["Vanessa Sabino"])])

    def test_sorteio_simples(self):
        nomes = ["Rodolpho Eckhardt", "Carlos Nascimento"]
        sorteio = xmas.sorteio(nomes)
        d = {"Rodolpho Eckhardt":"Carlos Nascimento", "Carlos Nascimento":"Rodolpho Eckhardt"}
        self.assertEquals(sorteio, d)
        
    def test_sorteio_simples2(self):
        nomes = ["Rodolpho Eckhardt", "Vanessa Sabino"]
        sorteio = xmas.sorteio(nomes)
        d = {"Rodolpho Eckhardt":"Vanessa Sabino", "Vanessa Sabino":"Rodolpho Eckhardt"}
        self.assertEquals(sorteio, d)
        
        
    def test_sorteio_simples3(self):
        nomes = ["Rodolpho Eckhardt", "Vanessa Sabino", "Guilherme Lara"]
        sorteio = xmas.sorteio(nomes)
        d = {"Rodolpho Eckhardt":"Vanessa Sabino", "Vanessa Sabino":"Guilherme Lara","Guilherme Lara":"Rodolpho Eckhardt"}
        self.assertEquals(sorteio, d)