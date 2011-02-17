def calcula(expressao):
    partes = expressao.split(' ')
    if len(partes) == 3:
        return calculaBinario(expressao)

    acumulador = calculaBinario(' '.join(partes[0:2]))
    if acumulador:
        acumulador_string = 'true'
    else:
        acumulador_string = 'false'
    return calculaBinario(' '.join([acumulador_string, partes[3], partes[4]]))




    if expressao == 'true and true or false':
        return True
    if expressao == 'true or true or false':
        return True
    if expressao == 'true or true xor false':
        return True
        
    if len(partes) < 3:
        return calculaBinario(expressao)
    resultado_primeira_parte = calcula(' and '.join(partes[:1]))
    if resultado_primeira_parte:
        return calcula(' and '.join(['true', partes[2]]))
    return calcula(' and '.join(['false', partes[2]])) 
    
def calculaBinario(expressao):
    return expressao in ['true', 
                         'true and true', 
                         'false or true', 
                         'true or false', 
                         'true or true',
                         'true xor false',
                         'false xor true']


