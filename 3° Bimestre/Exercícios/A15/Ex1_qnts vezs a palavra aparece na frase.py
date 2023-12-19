frase = input("Digite uma frase: ").lower()
palavra = input("Digite uma palavra: ").lower()

x = frase.split()
#i = 0
#for item in x:
#    if item == palavra:
#        i += 1
#print(i)
print("A palavra '%s' aparece %i vezes na frase." %(palavra, x.count(palavra)))