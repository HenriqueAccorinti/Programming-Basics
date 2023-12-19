frase1 = input("digite uma frase: ").lower().replace(' ','')
frase2 = input("digite outra frase: ").lower().replace(' ','')

jafoi = ''
for letra in frase1:
    if (letra in frase2) and (letra not in jafoi):
        print(letra)
        jafoi += letra