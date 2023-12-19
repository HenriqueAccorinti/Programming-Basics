from math import sqrt

L = float(input("Digite o lado: "))
N = int(input("Digite quantas parcelas: "))

Ao = L**2 * sqrt(3)/4
S = 0
k = 1
while k<=N:
    S = S + (4/9)**(k-1)
    #S += (4/9)**(k-1)
    k += 1
AFN = (1+S/3)*Ao
print(AFN)