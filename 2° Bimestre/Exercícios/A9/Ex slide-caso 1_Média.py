N = int(input("digite a qntd de valores: "))

S = 0
i = 1

while i <=N:
    X = float(input("Digite o %i° valor: " %i))
    S = S + X
    i = i + 1

Média = S/N
print("A média vale: %.3f" % Média)