# Importação dos módulos
import numpy as np

# Definição das funções
def lerVetor(x):
    """preenche o vetor passado como referência com os valores digitados pelo
       usuário"""
    for i in range(len(x)):
        x[i] = float(input("Digite o valor do elemento %i do vetor: " %i))

# Programa principal
u = np.zeros(3)
v = np.zeros(3)
w = np.zeros(3)

lerVetor(u)
lerVetor(v)
lerVetor(w)

M = np.array([u, v, w])
print(M)

if np.linalg.det(M) == 0:
    print("Os vetores são linearmente dependentes.")
else:
    print("Os vetores não são linearmente dependentes.")