def calcular_qtd_sacolas(qtd_max_por_sacola, itens):
	tipos_produto = {}
	num_sacolas = 0
	for item in itens:
		if item in tipos_produto:
			tipos_produto[item] += 1
		else:
			tipos_produto[item] = 1
		if tipos_produto[item] == qtd_max_por_sacola:
			num_sacolas += 1
			del tipos_produto[item]
	num_sacolas += len(tipos_produto)
	return num_sacolas