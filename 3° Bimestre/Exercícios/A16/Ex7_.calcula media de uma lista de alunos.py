# Importação dos módulos
from operator import itemgetter

# Definição das funções
def exibir_tabela(T):
    """exibe na forma de tabela"""
    T.sort(key = itemgetter(1), reverse = True)
    print("%15s\t%7s" %("Nome", "Média"))
    for linha in T:
        print("%15s\t%7.2f" %tuple(linha))

# Programa principal
dados = "Sarah Vaz\t8.5,4.5,7,6\nFulano de Tal\t4,5,6,7\nEma Thomaz\t6,8.5,7,7.5"
alunos = dados.split("\n")

L = []
for registro in alunos:
    aluno = registro.split("\t")
    nome = aluno[0]
    notas = aluno[1].split(",")
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    media = sum(notas)/len(notas)
    L.append([nome, media])
    
exibir_tabela(L)