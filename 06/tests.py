import unittest
import program

class Test(unittest.TestCase):
	def test_nenhum_livro(self):
		self.assertEquals(program.calcula_preco({}), 0)

	def test_um_livro(self):
		self.assertEquals(program.calcula_preco({2:1}), 8)

	def test_dois_livros_iguais(self):
		self.assertEquals(program.calcula_preco({2:2}), 16)
		
	def test_dois_livros_diferentes(self):
		self.assertEquals(program.calcula_preco({2:1,1:1}), 15.2)
		
	def test_tres_livros_diferentes(self):
		self.assertEquals(program.calcula_preco({2:1,1:1,3:1}), 21.6)
		
	def test_quatro_livros_diferentes(self):
		self.assertEquals(program.calcula_preco({2:1,1:1,3:1,4:1}), 25.6)
		
	def test_cinco_livros_diferentes(self):
		self.assertEquals(program.calcula_preco({2:1,1:1,3:1,4:1,5:1}), 30)
		
	def test_dois_livros_iguais_um_diferente(self):
		self.assertEquals(program.calcula_preco({2:2,1:1}), 23.2)
	
	def test_tres_livros_iguais_dois_diferente(self):
		self.assertEquals(program.calcula_preco({2:2,1:1, 3:3}), 44.8)
	
	def test_quatro_livros_n_unidades(self):
		self.assertEquals(program.calcula_preco({1:1, 2:2, 3:3, 4:4}), 70.4)
	


