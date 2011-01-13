import unittest
import program

class Test(unittest.TestCase):
	def test_zero_itens(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, []), 0)

	def test_um_item(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite"]), 1)

	def test_dois_itens_iguais(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite", "leite"]), 1)

	def test_dois_itens_diferentes(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite", "ovo"]), 2)
		
	def test_tres_itens_dois_iguais_um_diferentes(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite", "leite", "ovo"]), 2)
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite", "ovo", "leite"]), 2)
		
	def test_tres_itens_iguais(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite", "leite", "leite"]), 2)
	
	def test_cinco_leites_tres_ovos(self):
		self.assertEquals(program.calcular_qtd_sacolas(2, ["leite", "leite", "leite", "leite",
														   "leite", "ovo", "ovo", "ovo"]), 5)
														   
	def test_cinco_leites_tres_ovos_tres_itens(self):
		self.assertEquals(program.calcular_qtd_sacolas(3, ["leite", "leite", "leite", "leite",
														   "leite", "ovo", "ovo", "ovo"]), 3)
														   
	def test_cinco_leites_tres_ovos_um_item(self):
		self.assertEquals(program.calcular_qtd_sacolas(1, ["leite", "leite", "leite", "leite",
														   "leite", "ovo", "ovo", "ovo"]), 8)

  
    	