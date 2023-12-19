autor = input("Digite uma frase: ").upper()

uEspaco = autor.rfind(" ")
sn = autor[uEspaco+1:]

citacao = ''
p = ''
for letra in autor:
    if letra != ' ':
        p += letra
    else:
        # algoritmo
        if (p!="DA") and (p!="DAS") and (p!="DE") and \
           (p!="DO") and (p!="DOS") and (p!="E"):
            citacao += ' ' + p[0] + '.'
        p = ''
# última palavra
citacao = sn + ',' + citacao
print(citacao)