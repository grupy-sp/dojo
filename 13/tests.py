from __future__ import division
import unittest


VAZIO = 0
OCUPADO = 1

def distribuirMijoes(mijoes, mictorios):
	variavel = [VAZIO] * mictorios
	if mijoes:
		if mijoes == mictorios:
			return [OCUPADO]*mictorios
		passo = mictorios/mijoes
		
		#for i in xrange(0,mijoes,passo):
		#	variavel[i] = OCUPADO
		#variavel[-1] = OCUPADO
			
		if mijoes >= 1:
			variavel[0] = OCUPADO
		if mijoes >= 2:
			variavel[-1] = OCUPADO	
		if mijoes >= 3:
			variavel[(mictorios-1)//2] = OCUPADO
		if mijoes >= 4:
			variavel[(mictorios-1)//4] = OCUPADO
		if mijoes >= 5:
			variavel[(mictorios//2)] = OCUPADO
	return variavel
	
class SimpleTest(unittest.TestCase):
	def test_zero_pessoa_um_mictorio(self):
		self.assertEqual(distribuirMijoes(0, 1), [VAZIO])
	
	def test_uma_pessoa_um_mictorio(self):
		self.assertEqual(distribuirMijoes(1, 1), [OCUPADO])
	
	def test_zero_pessoa_dois_mictorios(self):
		self.assertEqual(distribuirMijoes(0,2), [VAZIO,VAZIO])
		
	def test_uma_pessoa_dois_mictorios(self):
		self.assertEqual(distribuirMijoes(1, 2), [OCUPADO,VAZIO])
		
	def test_duas_pessoas_dois_mictorios(self):
		self.assertEqual(distribuirMijoes(2, 2), [OCUPADO,OCUPADO])
	
	def test_zero_pessoa_tres_mictorios(self):
		self.assertEqual(distribuirMijoes(0, 3), [VAZIO, VAZIO, VAZIO])
		
	def test_uma_pessoa_tres_mictorios(self):
		self.assertEqual(distribuirMijoes(1, 3), [OCUPADO, VAZIO, VAZIO])

	def test_duas_pessoas_tres_mictorios(self):
		self.assertEqual(distribuirMijoes(2, 3), [OCUPADO, VAZIO, OCUPADO])

	def test_tres_pessoas_tres_mictorios(self):
		self.assertEqual(distribuirMijoes(3, 3), [OCUPADO]*3)
	
	def test_zero_pessoa_quatro_mictorios(self):	
		self.assertEqual(distribuirMijoes(0,4),[VAZIO]*4)
	
	def test_tres_pessoas_quatro_mictorios(self):
		self.assertEqual(distribuirMijoes(3,4), [OCUPADO,OCUPADO,VAZIO, OCUPADO])	
	
	def test_quatro_pessoas_quatro_mictorios(self):
		self.assertEqual(distribuirMijoes(4,4),[OCUPADO]*4)
	
	def test_tres_pessoas_cinco_mictorios(self):
		self.assertEqual(distribuirMijoes(3,5),[OCUPADO,VAZIO,OCUPADO,VAZIO,OCUPADO])

	def test_quatro_pessoas_cinco_mictorios(self):
		self.assertEqual(distribuirMijoes(4,5),[OCUPADO,OCUPADO,OCUPADO,VAZIO,OCUPADO])

	def test_cinco_pessoas_cinco_mictorios(self):
		self.assertEqual(distribuirMijoes(5,5),[OCUPADO]*5)	

	def test_cinco_pessoas_seis_mictorios(self):
		self.assertEqual(distribuirMijoes(5,6),[OCUPADO,OCUPADO,OCUPADO,OCUPADO,VAZIO,OCUPADO])


if __name__ == '__main__':
	unittest.main()
