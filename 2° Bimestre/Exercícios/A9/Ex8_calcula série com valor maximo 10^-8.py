#Exercício Feliz
from math import factorial

op = 's'                               # Caso 4
while op == 's':                       # Caso 4
    x = float(input("Digite x: "))
    s = 2 + x/factorial(3)
    i = 0
    while x**i/factorial(i) > 1e-8:    # Caso 2
        s = s + x**i/factorial(i)
        i = i + 2
    print(s)
    op = ''                                  # Caso 3
    while not ((op == 's') or (op == 'n')):  # Caso 3
        op = input("Calcular novamente (S/N)? ").lower() # Caso 4+3