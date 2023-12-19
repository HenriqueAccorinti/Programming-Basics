# Importação de Módulos
import numpy as np
import matplotlib.pyplot as plt
from math import cos

# Definição das Funções
def f(x):
    y = abs(cos(x))

    return y

# Programa Principal
x_min = int(input("Digite o valor de x mínimo: "))
x_max = int(input("Digite o valor de x máximo: "))

x = np.linspace(x_min, x_max, num = 100) # Cria o vetor x de x_min a x_max com 100
print(x)
y = []
# Cria o vetor y vazio

for i in x:
    aux = f(i)
# Calcula o valor de f(x), utilizando a função
   
    y.append(aux)
 # Adiciona o valor de aux ao final do vetor y

plt.plot(x,y)
 # Plota o gráfico de f(x)

plt.show()
 # Exibe o gráfico