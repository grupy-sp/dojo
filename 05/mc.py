
def calcula_tempo_filas(filas):
    tempo_filas = []
    for fila in filas:
        tempo_filas.append(fila.calcula_tempo_espera())
    return tempo_filas

def calcula_fila_rapida(filas):
    menor_tempo = filas[0].calcula_tempo_espera()
    fila_rapida = 0
    for i, fila in enumerate(filas):
        tempo_espera = fila.calcula_tempo_espera()
        drive_thru_e_empate = (tempo_espera == menor_tempo and type(fila) == DriveThruFila)
        if tempo_espera < menor_tempo or drive_thru_e_empate:
            menor_tempo = tempo_espera
            fila_rapida = i

    return fila_rapida

class Fila(object):
    def __init__(self, tempo, tamanho):
        self.tempo = tempo
        self.tamanho = tamanho

    def calcula_tempo_espera(self):
        return self.tempo * self.tamanho


class DriveThruFila(Fila):
    pass


class BalcaoFila(Fila):
    def __init__(self, tempo, tamanho, tempo_deslocamento=5):
        super(BalcaoFila, self).__init__(tempo, tamanho)
        self.tempo_deslocamento = tempo_deslocamento

    def calcula_tempo_espera(self):
        return super(BalcaoFila, self).calcula_tempo_espera() + self.tempo_deslocamento
