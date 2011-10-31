import unittest
import random

class Mock(object):
  def __init__(self, value, begin, end):
    self.verf = False
    self.value = value
    self.begin = begin
    self.end = end

  def __call__(self, begin, end):
    
    if end != self.end:
      raise Exception("Parametro end errado.")
    
    if begin != self.begin:
      raise Exception("Begin errado! Mane!")
    self.verf = True
    return self.value

def gera_solucao_arma(fr=random.randint):
  return fr(1,6)

def gera_solucao_local(fr = random.randint):
  return fr(1, 10)

def gera_soliu

class SimpleTest(unittest.TestCase):

  def test_gera_suspeito(self):
    self.assertTrue(0 < gera_solucao_suspeito() <= 6)

  def test_gera_local(self):
    self.assertTrue(0 < gera_solucao_local() < 11) 

  def test_gera_local_mockado(self):
    m = Mock(5, 1, 10)
    self.assertFalse(m.verf)
    self.assertEqual(5, gera_solucao_local(m))
    self.assertTrue(m.verf)

  def test_gera_arma(self):
    self.assertTrue(0 < gera_solucao_arma() < 7)
  
  def test_verificar_alteracao_verf(self):
    mock = Mock(4, 1, 6)
    self.assertFalse(mock.verf)
    self.assertEqual(gera_solucao_arma(mock), 4)	
    self.assertTrue(mock.verf)

  def test_random_mock_returning_3(self):
    mock = Mock(3, 2, 3)
    self.assertTrue(mock(2,3) == 3)
  
  def test_random_mock_returning_4(self):
    mock = Mock(4, 2, 4)
    self.assertTrue(mock(2,4) == 4)
    
  def test_random_with_right_params(self):
    mock = Mock(4, 1, 6)
    self.assertTrue(mock(1,6) == 4)
  
  def test_random_with_wrong_params(self):
    mock = Mock(4, 1, 6)
    self.assertRaises(Exception, mock, 1, 2)
    self.assertRaises(Exception, mock, 2, 6)
    
    self.assertFalse(mock.verf)




  
 


if __name__ == '__main__':
  unittest.main()
