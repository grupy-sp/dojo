import copy

def CalculaProximo(mapa):
	novo_mapa = copy.deepcopy(mapa)
	
	novo_mapa[0][0] = False
	return novo_mapa
	
def CalcularQuantidadeVizinhosVivos(mapa, x, y):
	vizinhos = 0
	
	if mapa[x+1][y] :
		vizinhos += 1
	if mapa[x][y+1] :
		vizinhos += 1
	if mapa[x+1][y+1] :
		vizinhos += 1
	return vizinhos