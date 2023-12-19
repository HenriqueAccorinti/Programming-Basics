# https://covid.saude.gov.br/
import numpy as np
import matplotlib.pyplot as plt

def calcularMediaMovel(dados, MM):

""" preenche a lista MM com a média móvel de 7 dias, arredondada, desde o 7º até o último dia """
for i in range(7,len(dias)):

s = Resposta

for d in range(7):

s += dados[Resposta]

s /= Resposta

Resposta( round(s) )



def mediaMovelEquivalente(MM):

""" retorna o primeiro dia em que a pandemia superou a média móvel atual """
d = 0
while MM[d] Resposta
 MM[Resposta]:

d Resposta 1

return d

   


# programa principal
# faz a leitura do arquivo e separa as duas colunas
tabela = np.loadtxt('covid.csv', delimiter=';')
dias = Resposta

dados = Resposta

# exibe a situação do último dia do registro
print("%i registros no %iº dia." % (Resposta, Resposta) )

 

# Calcula a média móvel
MM = [0,0,0,0,0,0,0] # sete primeiros dias
calcularMediaMovel(dados, MM)
print("Média móvel da última semana: %i registros." % Resposta) # acessa o último registro da média móvel
print("Média móvel semana anterior: %i registros." % Resposta) # acessa o 14º registro da média móvel, a partir do último

# verifica se houve redução, estabilidade ou aumento
compMM = 100 * Resposta / Resposta
 # divide a média móvel do último dia pela de 14 dias antes
if Resposta:

print("Aumento: ↑%.0f%%" % (compMM))

elif Resposta:

print("Redução: ↓%.0f%%" % (100-compMM))

else:

if MM[-1] > MM[-14]: 

print("Estabilidade: ↑%.0f%%" % (compMM))

else:

print("Estabilidade: ↓%.0f%%" % (100-compMM))

 

# compara a situação atual com o início da pandemia
dia = mediaMovelEquivalente(MM)
print("Equivalente ao %iº dia, com %i registros." % (Resposta, Resposta) )

 

# desenha o gráfico
plt.xlabel("Dias")

# desenha todos os registros
plt.Resposta(Resposta, Resposta, color=[.8,.8,.8])


# desenha a média móvel
plt.Resposta(Resposta, Resposta, 'r-')

# desenha a linha comparando a situação atual com o início da pandemia
plt.plot( (dia, len(dias)), (MM[dia], MM[dia]) , 'm:' )

 

# para exibir o gráfico
plt.show()