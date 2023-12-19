import numpy as np

tempo=[]
velocidade=[]
N = int(input("Digite o número de pontos: "))
for i in range(N):

    t = float(input("Digite o tempo do %i° ponto: " % (i+1)))
    v = float(input("Digite a velocidade do %i° ponto: " % (i+1)))
    tempo.append(t)
    velocidade.append(v)

    print()

distancia = np.trapz(velocidade,tempo)

vm = distancia/max(tempo)

print("Distância percorrida: %.2f m" % distancia)
print("Velocidade média: %.2f m/s" % vm)