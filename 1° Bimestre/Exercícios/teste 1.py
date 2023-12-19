# Definição das funções
def conica(x, y):
    """Função para determinar a posição de uma coordenada
    em uma função cônica -85x²+61xy-42y²+352x+222y = 1068
    retorna 0 se o ponto estiver na borda da função cônica
    retorna -1 se o ponto estiver na região externa da função cônica
    retorna 1 se o ponto estiver na região interna da função cônica"""
 
    z = -85*x**2+61*x*y-42*y**2+352*x+222*y
 # Expressão da função cônica
 

    if z==1068: # Condição para estar na borda da função cônica
        return 0
    elif z>1068: # Condição para estar na região externa da função cônica
        return -1
    else: # Condição para estar na região interna da função cônica
        return 1

# Programa principal
# Entrada de dados
x = float(input("Digite a coordenada em x: ")) # x é do tipo real
y = float(input("Digite a coordenada em y: ")) # y é do tipo real

posicao = conica(x,y)  # Chamada da função
if posicao == 0:
    print("O ponto (%.1f, %.1f) está na borda da função cônica" %(x, y))
elif posicao == 1:
    print("O ponto (%.1f, %.1f) está na região interna da função cônica" %(x, y))
else:
    print("O ponto (%.1f, %.1f) está na região externa da função cônica" %(x, y))