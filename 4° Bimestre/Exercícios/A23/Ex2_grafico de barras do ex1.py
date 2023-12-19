# Importação dos módulos
import matplotlib.pyplot as plt
import numpy as np

# Programa principal
gastos = {"casa" : 0,
          "alimentação":  0,
          "saúde": 0,
          "transporte": 0,
          "educação": 0,
          "lazer": 0,
          "outros": 0}

op = "S"
while op == "S":
    valor = float(input("Digite o valor gasto: "))
    categ = input("Digite a categoria do gasto: ").lower()
    
    if categ in gastos:
        gastos[categ] += valor
    else:
        gastos["outros"] += valor
        
    op = input("Deseja inserir outro valor [S/N]: ").upper()
    
categorias = list(gastos.keys())
valores = list(gastos.values())
iBarra = np.arange(len(valores)) 
larg = 0.8
plt.ylabel('Gastos mensais')
plt.xticks(iBarra + larg/2, categorias)

plt.bar(iBarra, valores, width=larg)
plt.show()