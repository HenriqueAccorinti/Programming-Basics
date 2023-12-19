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
  
  




#import numpy as np
#import matplotlib.pyplot as plt
#
#
#def desenhar(x,y,tam,v1,v2):
#    if v1>v2:
#        cor = 'c'
#    else:
#        cor = 'y'
#    
#    a = 1 - (min(v1,v2)/max(v1,v2))
#    a = min(1,max(a,0))
#    
#    xt = []
#    yt = []
#    
#    for i in range(50):
#        t = np.radians(360*1/50)
#        xt.append(x+0.8*tam*np.cos(t)/max(np.abs(np.cos(t)),np.abs(np.sin(t))))
#        yt.append(x+0.8*tam*np.sin(t)/max(np.abs(np.cos(t)),np.abs(np.sin(t))))
#        
#    plt.fill(xt,yt,color=cor,alpha=a)
#        
#
#tabela = np.array([[22362,49148,17629,150000,57290000,11420000],
#[42818,77865,17629,30000,25500000,103650000],
#[83729,94780,22135,240000,42780000,177610000],
#[164372,89273,30495,430000,21630000,145040000],
#[113626,55442,24705,280000,21750000,41450000],
#[70354,37740,20245,300000,56240000,126480000],
#[91990,0.3516,20245,20000,10410000,50890000],
#[140000,0.0000,24069,250000,129990000,86140000],
#[189942,-37395,27089,310000,44100000,221290000],
#[118740,-66112,34723,80000,69430000,198490000],
#[205066,-89419,27089,340000,450000,22200000],
#[272503,-122156,33630,300000,179250000,148420000],
#[322917,-166678,33630,260000,96490000,202880000],
#[167092,-135251,29579,480000,12830000,12290000],
#[172329,-194176,29579,420000,98690000,98830000],
#[95071,-234769,30021,430000,134680000,6200000],
#[114058,-177808,30021,360000,241270000,42600000],
#[-19151,-196721,67273,930000,377160000,186240000]])
#
#
#
#x= tabela[:,0]
#y= tabela[:,1]
#tam=tabela[:,2]
#a=tabela[:,3]
#v1=tabela[:,4]
#v2=tabela[:,5]
#        
## plt.axis("equal")
#
#for i in range(len(tabela)):
#    desenhar(x[i],y[i],tam[i],v1[i],v2[i])
#
#plt.show()
#
#vp1=sum(v1)
#vp2=sum(v2)
#
#print("voto popular: ")
#print('candidato 1: %.2f'%vp1)
#print('candidato 2: %.2f'%vp2)
#
#va1=0
#va2=0
#
#for i in range(len(tabela)):
#    if v1[i] > v2[i]:
#        va1 += a[i]
#    else:
#        va2 += a[i]
#        
#print()
#print('numero de xerifes: ')
#print("candidato 1: %i"%va1)
#print('candidato 2: %i'%va2)
#
#if vp1 > vp2:
#    print('candidto 1 vence')
#elif vp2 > vp1:
#    print('candidato 2 vence')
#else:
#    print('enpate presidencial')