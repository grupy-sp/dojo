import unittest
import program

class Test(unittest.TestCase):
	def test_um(self):
		self.assertEquals(program.procura_amigos([[1,1],[1,1],[1,1]]),
												{0:[1,2], 1:[0,2], 
												2:[0,1]})
	
	def test_distancias(self):
		self.assertEquals(program.calcula_distancia([1,1],[1,1]), 0)
		self.assertEquals(program.calcula_distancia([0,0],[3,4]), 5)
		self.assertEquals(program.calcula_distancia([3,4],[0,0]), 5)
		self.assertEquals(program.calcula_distancia([2,3],[-1,-1]), 5)
		self.assertEquals(program.calcula_distancia([1,0],[5,0]), 4)
		self.assertEquals(program.calcula_distancia([0,1],[0,5]), 4)
	
	def test_procura_amigos_de_uma_pessoa(self):
		self.assertEquals(program.procura_meus_amigos(0, [[0,1], [0,5], [2,3]]), set([1, 2]))
		self.assertEquals(program.procura_meus_amigos(1, [[0,1], [0,5], [2,3]]), set([0, 2]))
		self.assertEquals(program.procura_meus_amigos(1, [[0,1], [0,0], [2,3], [1,0]]), set([0, 3]))