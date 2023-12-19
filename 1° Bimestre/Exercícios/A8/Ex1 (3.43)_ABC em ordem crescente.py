
A = float(input("Digite A: "))
B = float(input("Digite B: "))
C = float(input("Digite C: "))

if A > B:
    if B > C:
        print(C,B,A)
    elif A > C:
        print(B,C,A)
    else:
        print(B,A,C)
else:
    if A > C:
        print(C,A,B)
    elif B > C:
        print(A,C,B)
    else:
        print(A,B,C)

#OU
        
#maior = max(A,B,C)
#menor = min(A,B,C)
#meio = A + B + C - menor - maior
#print(menor, meio, maior)
        
#OU
        
#A = float(input("Digite A: "))
#B = float(input("Digite B: "))
#C = float(input("Digite C: "))
#
#numeros=[A,B,C]
#numeros.sort()
#print(numeros)