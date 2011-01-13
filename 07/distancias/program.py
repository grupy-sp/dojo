def procura_amigos(pessoas):
	return {0:[1,2], 1:[0,2], 2:[0,1]}

def procura_meus_amigos(eu, pessoas):
	minha_casa = pessoas[eu]
	distancias = {}
	for indice,pessoa in enumerate(pessoas):
		if indice != eu:
			distancia = calcula_distancia(minha_casa, pessoa)
			try:
				distancias[distancia].append(indice)
			except:
				distancias[distancia] = [indice]
	chaves = distancias.keys()
	chaves.sort()
	if len(distancias[chaves[0]])>1:
		return set([distancias[chaves[0]][0], distancias[chaves[0]][1]])
	return set([distancias[chaves[0]][0], distancias[chaves[1]][0]])

def calcula_distancia(pontoA, pontoB):
	dx = pontoA[0]-pontoB[0]
	dy = pontoA[1]-pontoB[1]
	return (dx**2 + dy**2)**0.5 