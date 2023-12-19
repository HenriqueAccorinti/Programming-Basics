from math import *

def delta(a,b,c):
    return b**2 - (4*a*c)

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

d = delta(a,b,c)
if d > 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    print("As raízes são %.2f e %.2f: " %(x1,x2))
else:
    if d == 0:
        x1 = (-b + sqrt(d))/(2*a)
        print("A raíz é %.2f: " %x1)
    else:
        print("Não existem raízes reais.")