C = 0
S = 0
op = "s"

while (op == 's') or (op == 'S'):
    C = C + 1
    n = float(input("Digite o %i° número: " %C))
    S = S + n**2
    op = input("Deseja inserir outro valor?(s/n): ")
print ("A soma dos quadrados é %.2f" %S)