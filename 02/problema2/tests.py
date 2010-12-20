import gol

mapa = [[False, False, False],
        [True,  True,  True],
        [False, True,  False]]

def testMapaPosUnica():
	mapa = [[False]]
	retorno = gol.CalculaProximo(mapa)
	assert retorno == mapa, retorno
	assert not retorno is mapa, retorno 
	mapa = [[True]]
	retorno = gol.CalculaProximo(mapa)
	assert retorno == [[False]], retorno

def testMap2Por2():
	mapa = [[False,False],[False,False]]
	retorno = gol.CalculaProximo(mapa)
	assert retorno == mapa, retorno

#	mapa = [[True,True],[True,True]]
#	retorno = gol.CalculaProximo(mapa)
#	assert retorno == mapa, retorno
	
def testQuantidadeVizinhosVivos():
	mapa = [[False]]
	retorno = gol.CalcularQuantidadeVizinhosVivos(mapa, 0, 0)
	assert retorno == 0, retorno
	mapa = [[False, False], [True, True]]
	retorno = gol.CalcularQuantidadeVizinhosVivos(mapa, 0, 0)
	assert retorno == 2, retorno