def afundados(frota, tabuleiro):
    navio_afundado = 0 
    for navio in frota: 
        posicoes = frota[navio]
        for posicao in posicoes:
            algum_afundou = True #vai ser verdadeiro se algum navio afundar, ou seja, as posicoes forem X
            for i, j in posicao:
                if tabuleiro[i][j] != 'X': #e o navio esta em alguma posicao que nao esta com X, logo ele nao afunda 
                    algum_afundou = False #nenhum navio na posicao onde tem X, ent nao afundou 
                    break #o loop para, pois a embarcacao nao afundou, uma vez que pelo menos uma das suas posicoes nao esta no X
            else:         
                navio_afundado +=1 # se o navio estiver na posicao com X, logo o navio afundou 
    return navio_afundado
    