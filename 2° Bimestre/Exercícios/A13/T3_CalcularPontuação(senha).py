def CalcularPontuacao(senha):
    p = 0
    jafoi = ""
    for letra in senha.lower():
        if letra in "abcdefghijklmnopqrstuvwxyz":
            p += 1
        elif letra in "0123456789":
            p += 3
        else:
            p += 4
        if letra in jafoi:
            p -= 3
        jafoi += letra     
    return p
    
A = input("Digite uma senha poderosa: ")
B = CalcularPontuacao(A)
print(B)
