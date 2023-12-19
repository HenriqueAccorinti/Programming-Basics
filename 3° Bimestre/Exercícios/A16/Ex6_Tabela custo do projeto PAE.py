from os import *

# Definição das funções
def exibirTabela(L):
    """exibe a tabela de produtos de forma ordenada"""
    system("cls")
    L.sort()
    s = 0
    print("%15s\t%5s\t%s" %("Produto", "Qtd", "Preço"))
    for linha in L:
        print("%15s\t%5.1f\t%.2f" %tuple(linha))
        s = s + linha[2]*linha[1] #preço*qtd
    print("Total = R$ %.2f" %s)

# Programa principal
print("Cadastro de produtos")
N = int(input("Digite a quantidade de produtos: "))
L = []
for i in range(N):
    produto = input("Nome do produto %i: " %(i + 1)).lower()
    qtd = float(input("Quantidade do produto %i: " %(i + 1)))
    L.append([produto, qtd, 0])

exibirTabela(L)

print("Cadastro de preços")
for i in range(N):
    produto = input("Qual produto deseja cadastrar o preço: ").lower()
    preço = float(input("Digite o preço do %s: " %produto))
    for item in L:
        if item[0] == produto:
            item[2] = preço
    exibirTabela(L)