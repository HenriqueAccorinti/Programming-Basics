# Definição das funções
def menorMaior(L):
    """retorna uma lista com o menor e o maior valor da lista"""
    return [min(L), max(L)]

# Programa principal
N = int(input("Digite o número de itens: "))
L = []
for i in range(N):
    x = float(input("Digite o elemento %i da lista: " %(i+1)))
    L.append(x)

dados = menorMaior(L)    
print("O menor valor da lista é %.1f e o maior é %.1f" %(dados[0], dados[1]))
print("O menor valor da lista é %.1f e o maior é %.1f" %tuple(dados))