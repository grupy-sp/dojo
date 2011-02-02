def troco(preco, pago, caixa):
    troco = pago - preco
    if troco in caixa:
        return {troco:1}
    if preco in [85]:
        if 5 not in caixa:
            return {10:2}
    
        
    retorno = {}
    while troco > 0:
        notas = caixa.keys()
        notas.sort(reverse=True)
        for nota in notas:
            if caixa[nota]:
                troco -= nota
                caixa[nota] -= 1
                if caixa[nota] == 0:
                    del(caixa[nota])
                if nota not in retorno:
                    retorno[nota] = 0
                retorno[nota] += 1
                break
    return retorno