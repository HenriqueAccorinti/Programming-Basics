
def ContarVogais(frase):
    v = 0
    for letra in "aeiou":
        v = v + frase.count(letra)
    return v

frase = input("digite uma frase: ").lower()
vogais = ContarVogais(frase)
print("Possui %i vogais" %vogais)