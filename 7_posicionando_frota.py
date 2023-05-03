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
