
def CalcularPlacar(jogo):
	total = 0
	jogada = 0
	flag = False
	is_primeira_it = True
	proximaJogada = 0
	proxProxJogada = 0
	jogadas = list(jogo)
	jogadas.reverse()
	
	for jogada in jogadas:
		if flag:
			flag = False
			continue
		if jogada == "/":
			if not is_primeira_it:
				total += 10 + proximaJogada
			flag = True 
		elif jogada == "X":
			total += 10 + proxProxJogada + proximaJogada
			proxProxJogada = proximaJogada
			proximaJogada = 10
		elif jogada != "-":
			total += int(jogada)
			proxProxJogada = proximaJogada
			proximaJogada = int(jogada)
		is_primeira_it = False
	return total
	