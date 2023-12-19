def NovaSenha(senha):
    ns = ""
    n = len(senha)%10
    i = 0
    while i < len(senha):
        ns += senha[i:i+1] + str(n)
        n -= 1
        if n == -1:
            n = 9
            i += 1
    
A = input("Digite uma senha: ")
B = NovaSenha(A)
print(B)