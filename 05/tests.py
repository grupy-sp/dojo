import mc
import unittest

class McTest(unittest.TestCase):
    def test_calcula_tempo_espera(self):
        tempo = mc.BalcaoFila(5, 10)
        espera = tempo.calcula_tempo_espera()
        self.assertEquals(espera, 55)

    def test_calcula_tempo_filas(self):
        filas = [mc.BalcaoFila(1, 5), mc.BalcaoFila(2, 4), mc.BalcaoFila(3, 3), mc.BalcaoFila(4, 2), mc.DriveThruFila(5, 1)]
        tempos_espera = mc.calcula_tempo_filas(filas)
        self.assertEquals(tempos_espera, [10, 13, 14, 13, 5])


    def test_calcula_fila_rapida_empate(self):
        filas = [mc.BalcaoFila(1, 5), mc.BalcaoFila(2, 4), mc.BalcaoFila(3, 3), mc.BalcaoFila(4, 2), mc.DriveThruFila(5, 2)]
        fila_rapida = mc.calcula_fila_rapida(filas)
        self.assertEquals(fila_rapida, 4)

    def test_calcula_fila_rapida_balcao(self):
        filas = [mc.BalcaoFila(1, 5), mc.BalcaoFila(2, 4), mc.BalcaoFila(3, 3), mc.BalcaoFila(4, 2), mc.DriveThruFila(9, 3)]
        fila_rapida = mc.calcula_fila_rapida(filas)
        self.assertEquals(fila_rapida, 0)

    def test_calcula_fila_rapida_drive(self):
        filas = [mc.BalcaoFila(1, 5), mc.BalcaoFila(2, 4), mc.BalcaoFila(3, 3), mc.BalcaoFila(4, 2), mc.DriveThruFila(1, 1)]
        fila_rapida = mc.calcula_fila_rapida(filas)
        self.assertEquals(fila_rapida, 4)

    def test_calcula_fila_rapida_empate_fora_de_ordem(self):
        filas = [mc.BalcaoFila(1, 5), mc.BalcaoFila(2, 4), mc.DriveThruFila(5, 2), mc.BalcaoFila(3, 3), mc.BalcaoFila(4, 2)]
        fila_rapida = mc.calcula_fila_rapida(filas)
        self.assertEquals(fila_rapida, 2)
