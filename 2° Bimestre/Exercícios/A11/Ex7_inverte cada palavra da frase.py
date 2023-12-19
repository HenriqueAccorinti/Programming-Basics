frase = "Instituto Mauá de Tecnologia"

nf = ''
p = ''
for letra in frase:
    if letra != ' ':
        p = p + letra
    else:
        # algoritmo
        nf = nf + p[::-1] + ' '
        p = ''
# última palavra
nf = nf + p[::-1]
print(nf)