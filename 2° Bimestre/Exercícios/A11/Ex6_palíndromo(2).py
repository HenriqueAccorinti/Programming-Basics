frase = input("Digite uma frase: ").lower().replace(" ", "")
print(frase)
fraseInv = frase[::-1]
print(fraseInv)
if frase == fraseInv:
    print("É palíndromo")
else:
    print("Não é palíndromo")