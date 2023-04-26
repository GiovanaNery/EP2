#TODOS OS CODIGOS DO EP2
def define_posicoes(linha, coluna, orientacao, tamanho): 
    posicoes = []
    if orientacao == 'vertical': 
        for i in range(tamanho): 
            posicoes.append([linha+i, coluna])
    elif orientacao == 'horizontal': 
        for i in range(tamanho): 
            posicoes.append([linha, coluna+i])
    return posicoes



def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota: 
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else: #se o nome do navio nao esta no dicio
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota 
    
    
    
def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna]==1: 
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
        


def posiciona_frota(frota): 

    tabuleiro = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio in frota: 
        posicoes = frota[navio]
        for posicao in posicoes: 
            for i, j in posicao: #i = linha, j = coluna  
                tabuleiro[i][j] = 1 
    return tabuleiro
            

         
def afundados(frota, tabuleiro):
    navio_afundado = 0 
    for navio in frota: 
        posicoes = frota[navio]
        for posicao in posicoes:
            algum_afundou = True 
            for i, j in posicao:
                if tabuleiro[i][j] != 'X': 
                    algum_afundou = False 
                    break 
            else: 
                    navio_afundado +=1 
    return navio_afundado



          

    
    
