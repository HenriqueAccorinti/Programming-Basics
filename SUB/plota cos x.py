# Importações de módulos

from math import *

 

# Definição da função responsável por calcular o termo da série 

def termo(x, i):

    return x**i/factorial(i)

# Programa Principal
x = float(input("Digite o valor de x: "))
 # x deve ser real

i = 1
 # Inicialização da variável i

S = 0
 # Inicialização da variável S

 

while termo(x,i) > 1e-8: # Condição do while, utilize a função termo

    S += termo(x,i)
    i += 1
  # Atualiza o contador


print("O valor de S = %.8f" %S) # Imprimir com 8 casas decimais