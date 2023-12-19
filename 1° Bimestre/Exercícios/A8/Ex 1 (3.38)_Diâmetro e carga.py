from math import pi

D = float(input("Digite o diâmetro: "))
Q = float(input("Digite a carga: "))

if D>100:
    n = 2
elif D<50:
    n = 6
else:
    n = 4
    
S = 4*Q / (pi*D**2) * n
print("A tensão vale: %.2f" %S)