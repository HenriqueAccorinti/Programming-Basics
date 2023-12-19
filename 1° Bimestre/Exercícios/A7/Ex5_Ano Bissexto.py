def Bissexto(A):
    return (A%400==0) or ((A%4==0) and not (A%100==0))

A = int(input("Digite o ano: "))
B = Bissexto(A)
print(B)