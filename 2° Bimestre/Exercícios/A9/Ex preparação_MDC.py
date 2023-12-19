A = 204
B = 84

def MDC(A,B):
    Resto = A % B

    while not(Resto == 0):
        A = B
        B = Resto
        Resto = A % B
    return B    
C = MDC(A,B)
print(C)