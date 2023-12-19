# https://covid.saude.gov.br/
import numpy as np
import matplotlib.pyplot as plt

def calcularMediaMovel(dados, MM):

    for i in range(7,len(dias)):

        s = 0

        for d in range(7):

            s += dados[d]

        s /= 7

    print( round(s) )

 

def mediaMovelEquivalente(MM):


    d = 0
    while MM[d] > MM[d-1]:

        d += 1

    return d

   


# programa principal
# faz a leitura do arquivo e separa as duas colunas
tabela = np.loadtxt('covid.csv', delimiter=';')
dias = tabela[:,0]

dados = tabela[:,1]

# exibe a situação do último dia do registro
print("%i registros no %iº dia." % (dados[-1], dias[-1]) )

 

# Calcula a média móvel
MM = [0,0,0,0,0,0,0] # sete primeiros dias
calcularMediaMovel(dados, MM)
print("Média móvel da última semana: %i registros." % MM[-1]) # acessa o último registro da média móvel
print("Média móvel semana anterior: %i registros." % MM[-14]) # acessa o 14º registro da média móvel, a partir do último

# verifica se houve redução, estabilidade ou aumento
compMM = 100 * MM[-1] / MM[-14]
 # divide a média móvel do último dia pela de 14 dias antes
if compMM > 115:

    print("Aumento: ↑%.0f%%" % (compMM))

elif compMM < 85:

    print("Redução: ↓%.0f%%" % (100-compMM))

else:

    if MM[-1] > MM[-14]: 

        print("Estabilidade: ↑%.0f%%" % (compMM))

    else:

        print("Estabilidade: ↓%.0f%%" % (100-compMM))

 

# compara a situação atual com o início da pandemia
dia = mediaMovelEquivalente(MM)
print("Equivalente ao %iº dia, com %i registros." % (dia, dados[0]) )

 

# desenha o gráfico
plt.xlabel("Dias")

# desenha todos os registros
plt.bar(dias, dados, color=[.8,.8,.8])


# desenha a média móvel
plt.line(dia, MM, 'r-')

# desenha a linha comparando a situação atual com o início da pandemia
plt.plot( (dia, len(dias)), (MM[dia], MM[dia]) , 'm:' )

 

# para exibir o gráfico
plt.show()