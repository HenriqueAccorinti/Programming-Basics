frase = input("Digite uma frase: ").lower()

maior = 0
caractere = ''

for letra in frase:
    nc = frase.count(letra)

    if nc > maior:
        maior = nc
        caractere = letra
        
print(maior)
print(caractere)