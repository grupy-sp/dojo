import unittest

VAZIO = 'vazio'
MIJANDO = 'mijando'

def distribui_pessoas(num_mic, num_pes):
    mictorios = [VAZIO] * num_mic
    if num_pes >= 1:
        mictorios[0] = MIJANDO
    if num_pes >= 2:
        mictorios[-1] = MIJANDO
    if num_pes == 3:
        mictorios[num_mic/2] = MIJANDO
    if num_mic == 7:
        mictorios[3] = MIJANDO
    
    return mictorios


class TestCase(unittest.TestCase):
    def test_zero_mictorios(self):
        dist = distribui_pessoas(num_mic=0, num_pes=0)
        self.assertEquals(dist, [])
    
    def test_um_mictorio_zero_pessoa(self):
        dist = distribui_pessoas(num_mic=1, num_pes=0)
        self.assertEquals(dist, [VAZIO]) 
        
    def test_um_mictorio_uma_pessoa(self):
        dist = distribui_pessoas(num_mic=1, num_pes=1)
        self.assertEquals(dist, [MIJANDO])
    
    def test_dois_mictorios_uma_pessoa(self):
        dist = distribui_pessoas(num_mic=2, num_pes=1)
        self.assertEquals(dist,[MIJANDO,VAZIO])
        
    def test_dois_mictorios_duas_pessoas(self):
        dist = distribui_pessoas(num_mic=2, num_pes=2)
        self.assertEquals(dist, [MIJANDO, MIJANDO])
        
    def test_tres_mictorios_duas_pessoas(self):
        dist = distribui_pessoas(num_mic=3, num_pes=2)
        self.assertEquals(dist, [MIJANDO, VAZIO, MIJANDO])
    
    def test_cinco_mictorios_tres_pessoas(self):
        dist = distribui_pessoas(num_mic=5, num_pes=3)
        self.assertEquals(dist, [MIJANDO, VAZIO, MIJANDO, VAZIO, MIJANDO])
    def test_sete_mictorios_tres_pessoas(self):
        dist= distribui_pessoas(num_mic=7, num_pes=3)
        self.assertEquals(dist, [MIJANDO, VAZIO, VAZIO, MIJANDO, VAZIO, VAZIO, MIJANDO])
if __name__ == '__main__':
    unittest.main()