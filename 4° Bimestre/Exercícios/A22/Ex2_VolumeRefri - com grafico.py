# Importação dos módulos
import numpy as np

# Definição das funções
def f(x):
    "retorna o valor de f(x) dado x"
    if 0<=x<=0.5:
        y = -x*(x-1)+2.5
    if 0.5<x<=1.35:
        y = 2.76
    if 1.35<x<=2.4:
        y = 2.76 * np.cos(0.45 * (x - 1.35))
    if 2.4<x<=5:
        y = 0.08 * (x - 2.4) * (x - 5.5) + 2.46
    if 5<x<=15:
        y = -0.025 * (x - 5) * (x - 12.5) + 2.35
    if 15<x<=18:
        y = 0.05 * (x - 15) * (x - 21) + 1.73
    return y

# Programa principal
H = -1
while not(0 <= H <= 18):
    H = float(input("Digite o valor de H [0 ~ 18]: "))

y = []
dominio = np.arange(0, H, 0.01)
for x in dominio:
    y.append(f(x)**2)
v = np.pi*np.trapz(y, dominio)
print("O volume da garrafa é: %.1f ml" %v)

if H > 15:
    print("Garrafa muito cheia!")    

# próxima semana
import matplotlib.pyplot as plt
plt.fill_between(dominio,np.sqrt(y),color='k')
plt.fill_between(dominio,-np.sqrt(y),color='k')
y = []
dominio = np.arange(0, 18, 0.01)
for x in dominio:
    y.append(f(x)**2)
plt.plot(dominio,np.sqrt(y),dominio,-np.sqrt(y),color='k')
plt.axis("equal")
plt.show()