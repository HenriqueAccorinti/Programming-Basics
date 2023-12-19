import numpy as np
import matplotlib.pyplot as plt

# faz a leitura da imagem cujos valores são separados por ponto-e-vírgula
tabela = np.loadtxt('img.csv',delimiter=";")

# determina o tamanho da imagem a partir da última linha da tabela (convertendo o valor para inteiro)


NC = int(tabela[-1][0])
NL = int(tabela[-1][1])
print("O tamanho da imagem é: %i x %i" % (NC, NL))

# separa as colunas da tabela nas componentes de cor
R = tabela[:,0]

G = tabela[:,1]

B = tabela[:,2]

# transforma o vetor em matriz
R = R[:-1].reshape(NL,NC)
G = G[:-1].reshape(NL,NC)
B = B[:-1].reshape(NL,NC)

# percorre cada linha e coluna da matriz


for L in tabela:    
    for C in L:
# desenha um quadrado de tamanho 10 com a cor obtida do arquivo
        plt.plot(C, NL-L, markersize=10, markerfacecolor=[ R[L,C], G[L,C], B[L,C] ], markeredgecolor=[ R[L,C], G[L,C], B[L,C] ])

# mostra a imagem final
plt.show()