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
        
     


    
    
