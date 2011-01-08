def fator_desconto(numero):
	descontos = {0:0, 1:0, 2:5, 3:10, 4:20, 5:25}
	return (1 - (descontos[numero] / 100.0))

def calcula_preco(livros):
	total = 0
	while livros:
		total += 8 * len(livros) * fator_desconto(len(livros))
		for livro in livros.keys():
			livros[livro]-=1 
			if not livros[livro]:
				del livros[livro]
	return total