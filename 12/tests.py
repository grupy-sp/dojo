import unittest

def mata_escravos(n, k, i):
    qual_esta_vivo = n
    if n == 3:
        if k == 3:
            qual_esta_vivo = (i % n) + 1
        else:
            qual_esta_vivo = ((i + 1) % n) + 1
    elif n == 2:
        if k == 1:
            qual_esta_vivo = i % n + 1
        else:
            qual_esta_vivo = ((i + 1) % n) + 1
    elif n == 4:
        if i == 2 or k == 2 or k == 3:
            qual_esta_vivo = 1
            
    return qual_esta_vivo


class SimpleTest(unittest.TestCase):
    
    def test_n_4_k_4_i_1(self):
        self.assertEquals
    
    def test_n_4_k_3_i_1(self):
        self.assertEquals(mata_escravos(4, 3, 1), 1)
    def test_n_4_k_2_i_1(self):
        self.assertEquals(mata_escravos(4, 2, 1), 1)
    
    def test_n_4_k_1_i_2(self):
        self.assertEquals(mata_escravos(4, 1, 2), 1)
        
    def test_n_4_k_1_i_1(self):
        self.assertEquals(mata_escravos(4, 1, 1), 4)
        
    def test_n_3_k_2_i_3(self):
        self.assertEquals(mata_escravos(3, 2, 3), 2)

    def test_n_3_k_1_i_3(self):
        self.assertEquals(mata_escravos(3, 1, 3), 2)
    
    def test_n_3_k_2_i_2(self):
        self.assertEquals(mata_escravos(3, 2, 2), 1)
    
    def test_n_3_k_3_i_2(self):
        self.assertEquals(mata_escravos(3, 3, 2), 3)
        
    def test_n_3_k_3_i_3(self):
        self.assertEquals(mata_escravos(3, 3, 3), 1)

    def test_n_1_k_1_i_1(self):
        self.assertEquals(mata_escravos(1, 1, 1), 1)
    
    def test_n_2_k_1_i_1(self):
        self.assertEquals(mata_escravos(2, 1, 1), 2)

    def test_n_2_k_1_i_2(self):
        self.assertEquals(mata_escravos(2, 1, 2), 1)

    def test_n_2_k_2_i_1(self):
        self.assertEquals(mata_escravos(2, 2, 1), 1)
        
    def test_n_2_k_2_i_2(self):
        self.assertEquals(mata_escravos(2, 2, 2), 2)
        
    def test_n_3_k_1_i_1(self):
        self.assertEquals(mata_escravos(3, 1, 1), 3)

    def test_n_3_k_2_i_1(self):
        self.assertEquals(mata_escravos(3, 2, 1), 3)
    
    def test_n_3_k_3_i_1(self):
        self.assertEquals(mata_escravos(3, 3, 1), 2)
    
    def test_n_3_k_1_i_2(self):
        self.assertEquals(mata_escravos(3, 1, 2), 1)
if __name__ == '__main__':
    unittest.main()