frase = input("Digite uma frase: ").lower()
letras = input("Digite uma letra: ").lower()

qtd = 0
p = ''
for letra in frase:
    if letra != ' ':
        p += letra
    else:
        if p.find(letras) == 0:
            qtd += 1
        p = ''
        
if p.find(letras) == 0:
    qtd += 1

print("A letra '%s' é início de %s palavras" %(letras,qtd))