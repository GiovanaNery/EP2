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
        for posicao in posicoes: #cada posicao
            for i, j in posicao: #i = linha, j = coluna  
                tabuleiro[i][j] = 1 
            # o ultimo for serve para pegar os dois valores da posicao, sendo o pirmeiro a linha(i) e o segundo a coluna(j) e colocar no tabuleiro 
    return tabuleiro
            
            
        