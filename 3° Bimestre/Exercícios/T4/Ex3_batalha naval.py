
# Definição das funções
def restam_casas(Tabela):
    """retorna a quantidade de casas (posições) que ainda possuem navios"""
    soma = 0
 # inicializa a variável da soma
    for linha in Tabela:
        soma += sum(linha) # identifica a quantidade de navios na linha
    return soma

def realiza_jogada(Tabela, linha, coluna):
    """testa a jogada definida por linha e coluna, caso a jogada acerte
    um navio, a função deve atualizar o tabuleiro (adicionando zero à 
    posição da jogada) e retornar True. Caso contrário a função deverá
    apenas retornar False"""
    if Tabela[linha][coluna] == 1:
        # navio
        Tabela[linha][coluna] = 0
        return True
    else:
        # água
        return False

# Definição do tabuleiro
tabuleiro = [[0,0,0,0,0,0,0,0,0,0],
             [0,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,0,0,0,0,0],
             [0,1,0,0,1,0,0,1,0,0],
             [0,1,0,0,1,0,0,1,0,0],
             [0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0]]
 
# Inicialização das variáveis
total_jogadas = 0
jogadas_certas = []

while restam_casas(tabuleiro) > 0:
    # validação da linha
    linha = 10
    while not(0<=linha<=9):
        linha = int(input("Escolha a linha (0 à 9): ")) 
    # validação da coluna
    coluna = 10
    while not(0<=coluna<=9):
        coluna = int(input("Escolha a coluna (0 à 9): "))
    
    if realiza_jogada(tabuleiro, linha, coluna): 
        print("\nAcertou")
        # adiciona uma tupla com a jogada certa ao final da lista
        jogadas_certas.append((linha, coluna))
    else:
        print("\nErrou")
    
    total_jogadas += 1  
print("Fim de jogo, foram realizadas: %i tentativas" %total_jogadas)
print("Jogadas certas:", jogadas_certas)

