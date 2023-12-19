import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 15, 3)
v =[6, 12, 12, 0, -12]

# nomes nos eixos
plt.xlabel('t(s)')
plt.ylabel('V(m/s)')

# linhas tracejadas vermelhas e eixo X
for p in range(len(t)):
    plt.plot([t[p], t[p]], [0, v[p]], "r--", linewidth=2)
    plt.plot([0, t[p]], [v[p], v[p]], "r--", linewidth=2)
    
plt.plot([0, t[len(t)-1]], [0,0], 'k', linewidth=3)

# curva da velocidade com espessura 4
plt.plot(t,v, linewidth=4, color='darkblue')

# preenchimento do gráfico com transparência 0.1
plt.fill_between(t, v, color='magenta', alpha=0.1)

# e para finalizar
plt.show()