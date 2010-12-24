def separar_familias(nomes):
    familias = {}
    for nome in nomes:
        sobrenome = nome.split(" ")[1]
        if sobrenome not in familias:
            familias[sobrenome] = set()
        familias[sobrenome].add(nome)
    lista_de_familias_ordenada = familias.values()
    lista_de_familias_ordenada.sort(key=len, reverse=True)
    return lista_de_familias_ordenada

def sorteio(nomes):     
    
    return {nomes[0]:nomes[1],nomes[1]:nomes[0]}
    i = 0
    for nome in nomes:
        nome
    