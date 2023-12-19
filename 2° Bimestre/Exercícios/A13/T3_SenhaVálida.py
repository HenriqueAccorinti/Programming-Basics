def SenhaValida(senha):
    return (len(senha) >= 8) and (senha.find(" ", 1,len(senha)-1)!=-1 )
    #return(senha.find(" ", 1,len(senha)))
    
A = input("digite: ")
B = SenhaValida(A)
print(B)