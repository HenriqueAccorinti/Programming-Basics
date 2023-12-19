#import numpy as np
#import matplotlib.pyplot as plt
#
#  
#
#x_min = float(input("Digite o limite inferior de x: ")) # limite inferior de x, deve ser float
#x_max = float(input("Digite o limite superior de x: ")) # limite superior de x, deve ser float
#
#  
#
#x = np.linspace(x_min,x_max,num=70) # cria o domínio com 70 valores
#y = (1/(2*np.pi)**(1/2))*np.exp((-x**2)/2)# cria a função distribuição normal padrão
#
# 
#
#prob = np.trapz(y, x)
# # calcula a área entre a curva, dica: utilize uma função do cálculo numérico
#print("A probabilidade do valor estar entre esse intervalo é %.3f" %prob) # exibe o valor da probabilidade
#
# 
#
#plt.plot(x,y)  # plota o gráfico da função densidade de probabilidade
#plt.fill_between(x,y, alpha = 0.2) # preenche o gráfico
#plt.show()



import numpy as np
import matplotlib.pyplot as plt

x_min = int(input("Digite o limite inferior de x: ")) # limite inferior de x, deve ser inteiro
x_max = int(input("Digite o limite superior de x: ")) # limite superior de x, deve ser inteiro



x = np.linspace(x_min, x_max, num=70) # cria o domínio com 70 valores
y = (1/(2*np.pi)**(1/2))*np.exp((-x**2)/2)# cria a função distribuição normal padrão

 

prob = np.trapz(y,x)
 # calcula a área entre a curva, dica: utilize uma função do cálculo numérico
print("A probabilidade do valor estar entre esse intervalo é %.3f" %prob) # exibe o valor da probabilidade

 
plt.plot(x,y)  # plota o gráfico da função densidade de probabilidade
plt.fill_between(x,y, alpha = 0.2) # preenche o gráfico
plt.show()