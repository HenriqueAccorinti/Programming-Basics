def Bissexto(A):
    return (A%400==0) or ((A%4==0) and not (A%100==0))

A = int(input("Digite o ano: "))
M = int(input("Digite o mês: "))
if (M==4) or (M==6) or (M==9) or (M==11):
    d= 30
elif M==2:
    if Bissexto(A):
        d=29
    else:
        d=28
else:
    d=31
print("O mês tem %i dias" %d)