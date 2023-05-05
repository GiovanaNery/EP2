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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

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
            
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(preenche_frota(frota, navio, linha, coluna, orientacao, tamanho_frota[navio]))
jogando = True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

ataque_passado = []

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna]==1: 
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = '-'
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

while jogando: 
    grid = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print (grid) 
    repete = True
    while repete: 
        linha_ataque = int(input('Jogador, qual linha deseja atacar? ')) 
        while linha_ataque < 0 and linha_ataque > 9: 
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna_ataque < 0 or coluna_ataque > 9: 
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        novo_ataque = [linha_ataque, coluna_ataque]
        if novo_ataque not in ataque_passado: 
            ataque_passado.append(novo_ataque)
            repete = False
        else: 
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!' )
    jogada=faz_jogada(tabuleiro_oponente,linha,coluna)
    afundado = afundados(frota_oponente, tabuleiro_oponente)
    if afundado == 10: 
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False 
