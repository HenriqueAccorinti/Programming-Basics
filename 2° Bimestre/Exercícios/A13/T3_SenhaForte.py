def ForcaDaSenha(senha):
    
    #p = CalcularPontuação(senha)
    print("A sua senha é:")
    if p < 10:
        print("Muito fraca")
    elif p < 12:
        print("Fraca")
    elif p < 18:
        print("Regular")
    elif p < 25:
        print("Forte")
    else:
        print("Muito Forte")
        
p = int(input("digite uma pontuação: "))
A = ForcaDaSenha(p)
print(A)