import numpy as np
import matplotlib.pyplot as plt

#Definição das funções
def desenhar (x, y, tam, v1, v2):
  """desenha a forma geométrica referente ao resultado das eleições no distrito"""
  #cor do vencedor
  if v1 > v2:
    cor = 'c'

  else:
    cor = 'y'
  
  #intensidade da cor

  a = 1 - (min(v1,v2)/max(v1,v2))
  a = min(1, max(a, 0))

  # Lista de coordenadas da figura

  xt = [] #Inicialização da lista de pontos xt
  yt = [] #Inicialização da lista de pontos yt

  for i in range(50):
    t = np.radians(360*i/50)
    xt.append(x+0.8*tam*np.cos(t)/max(np.abs(np.cos(t)),np.abs(np.sin(t))))
    yt.append(y+0.8*tam*np.sin(t)/max(np.abs(np.cos(t)),np.abs(np.sin(t))))

    plt.fill(xt,yt,cor,alpha=a)

#Programa principal

#Leitura dos dados do arquivo

Tabela = np.loadtxt('votos.csv', delimiter = ';') # Lê o arquivo CSV

x = Tabela [:, 0]

y = Tabela [:, 1]

tam = Tabela [:, 2]

s = Tabela [:, 3]

v1 = Tabela [:, 4]

v2 = Tabela [:, 5]


# Desenha cada distrito
plt.axis("equal") #eixos iguais
for i in range(len(Tabela)):
  desenhar(x[i], y[i], tam[i], v1[i], v2[i])

plt.show() #exibe o gráfico

vp1 = sum(v1)
vp2 = sum(v2)

print("Voto popular: ")
print("Candidato 1: %.2f"% vp1)
print("Candidato 2: %.2f"% vp2)

vs1 = 0
vs2 = 0

for i in range(len(Tabela)):

  if v1[i] > v2[i]:
    vs1 += s[i]
  else:
    vs2 += s[i]

print()
print("Número de xerifes: ")
print("Candidato 1: %i" % vs1)
print("Candidato 2: %i" % vs2)

if vp1 > vp2:
  print("Candidato 1 vence")
elif vp2 > vp1:
  print("Candidato 2 vence")
else:
  print("Empate presidencial")