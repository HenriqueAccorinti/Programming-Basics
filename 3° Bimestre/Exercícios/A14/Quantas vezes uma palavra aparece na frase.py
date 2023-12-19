frase = input("Digite uma frase: ").lower
palavra = input("Digite uma palavra: ").lower

Lista = frase.split()
print("Apalavra apareceu %i vezes." %Lista.count(palavra))