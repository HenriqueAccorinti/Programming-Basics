def NovaSenha(senha):
    ns = ""
    for letra in senha:
        if letra.upper() == 'A':
            ns += '4'            
        elif letra.upper() == 'E':
            ns += '3'
        elif letra.upper() == 'I':
            ns += '1'
        elif letra.upper() == 'O':
            ns += '0'
        else:
            ns += letra

senha = input("Digite sua senha: ")
A = NovaSenha(senha)
print(A)