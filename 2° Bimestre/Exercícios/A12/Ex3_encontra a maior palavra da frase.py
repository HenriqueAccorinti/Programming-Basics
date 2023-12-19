frase = input("Digite uma frase: ")

maior = 0
p = ''
for letra in frase:
    if letra != ' ':
        p = p + letra
    else:
        # montou uma palavra
        ###############################
        # algoritmo do exercício
        ###############################
        if len(p) > maior:
            maior = len(p)
            maiorPalavra = p
        ###############################
        p = ''
        
# última palavra
###############################
# algoritmo do exercício
###############################
if len(p) > maior:
            maior = len(p)
            maiorPalavra = p
###############################

print("A maior palavra é '%s' e tem %i caracteres." % (maiorPalavra,maior))