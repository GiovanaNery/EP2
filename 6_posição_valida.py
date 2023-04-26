def define_posicoes(linha, coluna, orientacao, tamanho): 
    posicoes = []
    if orientacao == 'vertical': 
        for i in range(tamanho): 
            posicoes.append([linha+i, coluna])
    elif orientacao == 'horizontal': 
        for i in range(tamanho): 
            posicoes.append([linha, coluna+i])
    return posicoes

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0]<0 or posicao[1]<0 or posicao[0]>=10 or posicao[1]>=10:
            return False
        for coordenadas in frota.values():
            for j in range (len(coordenadas)):
                if posicao in coordenadas[j]:
                    return False
    if frota == {}:
        return True 
    return True   
    

