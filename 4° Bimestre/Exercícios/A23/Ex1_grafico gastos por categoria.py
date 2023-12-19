# Importação dos módulos
import matplotlib.pyplot as plt

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
plt.pie(valores, labels = categorias, autopct = "%.1f%%")
plt.axis("equal")
plt.show()