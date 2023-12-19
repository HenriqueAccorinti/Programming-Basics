from os import system

def exibirTabela(L):
    """exibe a tabela de produtos de forma ordenada"""
    system("cls")
    L.sort()
    print("%15s\t%s" %("CATEGORIA", "PRODUTO"))
    for linha in L:
        print("%15s\t%s" %tuple(linha))     

N = int(input("Digite o numero de itens: "))
L=[]

for i in range(N):
    prod = input("Digite o nome do %i° produto: " %(i+1)).lower()
    categ = input("Digite sua categoria: ").lower()
    L.append([categ, prod])

exibirTabela(L)