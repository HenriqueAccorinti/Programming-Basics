# Definição das funções
def exibePolinômio(P):
    """exibe o polinômio bonitinho"""
    s = ""
    for i in range(len(P)):
        s = "%.1f.x**%i + " %(P[i], i) + s
    s = "P(x) = " + s[:-3]
    print(s)

def calculaPolinômio(P, x):
    """calcula o valor de P(x)"""
    s = 0
    for i in range(len(P)):
        s = s + P[i]*x**i
    return s

# Programa principal
N = int(input("Digite o grau do polinômio: "))
coefs = []
for i in range(N + 1):
    x = float(input("Digite o coeficiente a%i: " %i))
    coefs.append(x)

print("\nPolinômio digitado:")    
exibePolinômio(coefs)

x = float(input("Digite o valor de x: "))
P_x = calculaPolinômio(coefs, x)

print("\nO valor de P(%.1f) = %.2f" %(x, P_x))