# Definição das funções
def procura_valor(D, N):
    """retorna uma lista em ordem das chaves que contenham o valor"""
    L = []
    for chave in D :
        if N in D[chave]:
            L.append(chave)
    L.sort()
    return L

# Programa principal
D = {"sala":[1, 2, 3], "quarto":[2, 2, 6], "cozinha":[6, 3, 1]}
N = int(input("Digite um número: "))

print(procura_valor(D, N))