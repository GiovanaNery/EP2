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



frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

tamanho_frota = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1
    }

for navio in frota.keys():

    n=0
    if navio == "porta-aviões":
        vezes=1
    if navio == "navio-tanque":
        vezes=2
    if navio == "contratorpedeiro":
        vezes=3
    if navio == "submarino": 
        vezes=4

    while n < vezes:
        print(n)

        print (f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho_frota[navio]}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if navio != "submarino":
            direção = int(input("[1] Vertical [2] Horizintal: "))
        if navio == "submarino": 
            orientacao = "vertical"
        
        elif direção == 1: 
            orientacao = "vertical"
        elif direção == 2:
            orientacao = "horizontal"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho_frota[navio]) == False:
            print ("Esta posição não está válida!")
        else: 
            preenche_frota(frota, navio, linha, coluna, orientacao, tamanho_frota[navio])
            n+=1
print(frota)





          

    
    
