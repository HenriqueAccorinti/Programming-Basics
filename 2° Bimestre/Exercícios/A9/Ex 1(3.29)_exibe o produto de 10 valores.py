p = 1
i = 1

while i <= 10:
    v = float(input("Digite o %i° valor: " %i))
    i = i + 1
    p = p * v
print("O produto dos 10 primeiros valores é: %.2f" %p)