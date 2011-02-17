import unittest
import program

class ExemploTest(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(program.calcula('true'))
        
    def testFalse(self):
        self.assertFalse(program.calcula('false'))
        
    def testTrueAndTrue(self):
        self.assertTrue(program.calcula('true and true'))
        
    def testTrueAndFalse(self):
        self.assertFalse(program.calcula('true and false')) 
    
    def testTrueOrFalse(self):
        self.assertTrue(program.calcula('true or false'))
        self.assertTrue(program.calcula('false or true'))
        
    def testFalseAndFalse(self):
        self.assertFalse(program.calcula('false and false'))
        
    def testFalseOrFalse(self):
        self.assertFalse(program.calcula('false or false'))
    
    def testTrueOrTrue(self):
        self.assertTrue(program.calcula('true or true'))
        
    def testTrueXorFalse(self):
        self.assertTrue(program.calcula('true xor false'))    
        
    def testTrueXorFalse(self):
        self.assertTrue(program.calcula('false xor true'))    
    
    def testTrueAndTrueAndTrue(self):
        self.assertTrue(program.calcula('true and true and true'))
        
    def testTrueAndTrueAndFalse(self):
        self.assertFalse(program.calcula('true and true and false'))
    def testTrueAndFalseOrFalse(self):
        self.assertFalse(program.calcula('true and false or false'))
        
    def testTrueAndTrueOrFalse(self):
        self.assertTrue(program.calcula('true and true or false'))
        
    def testTrueOrTrueAndFalse(self):
        self.assertFalse(program.calcula('true or true and false'))
        
    def testTrueOrTrueOrFalse(self):
        self.assertTrue(program.calcula('true or true or false'))   
    def testTrueOrTrueXorFalse(self):
        self.assertTrue(program.calcula('true or true xor false')) 
        
             

class ExemploCalculaBinario(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(program.calculaBinario('true'))

    def testFalse(self):
        self.assertFalse(program.calculaBinario('false'))

    def testTrueAndTrue(self):
        self.assertTrue(program.calculaBinario('true and true'))

    def testTrueAndFalse(self):
        self.assertFalse(program.calculaBinario('true and false')) 

    def testTrueOrFalse(self):
        self.assertTrue(program.calculaBinario('true or false'))
        self.assertTrue(program.calculaBinario('false or true'))

    def testFalseAndFalse(self):
        self.assertFalse(program.calculaBinario('false and false'))

    def testFalseOrFalse(self):
        self.assertFalse(program.calculaBinario('false or false'))

    def testTrueOrTrue(self):
        self.assertTrue(program.calculaBinario('true or true'))

    def testTrueXorFalse(self):
        self.assertTrue(program.calculaBinario('true xor false'))    

    def testTrueXorFalse(self):
        self.assertTrue(program.calculaBinario('false xor true'))
        
        
           
           
           
           