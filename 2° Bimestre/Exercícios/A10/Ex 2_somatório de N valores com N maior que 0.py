
N = -1
while N < 0:
    N = int(input("Digite o número de termos: "))
if N == 0:
    p = -99
else:
    d = float(input("Digite d: "))
    p = 0
    Sinal = -1
    i = 1
    while i <=N:
        p = p + Sinal/(i+d)
        Sinal = - Sinal
        i = i + 1
print("Resultado =", p)