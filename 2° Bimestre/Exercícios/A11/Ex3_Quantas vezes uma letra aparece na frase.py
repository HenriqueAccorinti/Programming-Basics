frase = input("Digite uma frase: ").lower()
letra = input("Digite um caractere: ").lower()
contaLetra = frase.count(letra)
print("O caractere '%s' apareceu %i vezes." % (letra, contaLetra) )