frase = input("Digite uma frase: ").lower()
palavra = input("Digite uma palavra: ").lower()
contaPalavra = 0

p = ''
for letra in frase:
    if letra != ' ':
        p = p + letra
        #print(p)
    else:
        # montou uma palavra
        ###############################
        # algoritmo do exercício
        ###############################
        if p == palavra:
            contaPalavra += 1
        ###############################
        p = ''
        
# última palavra
###############################
# algoritmo do exercício
###############################
if p == palavra:
    contaPalavra += 1
###############################

print("A palavra '%s' apareceu %i vezes." % (palavra, contaPalavra))