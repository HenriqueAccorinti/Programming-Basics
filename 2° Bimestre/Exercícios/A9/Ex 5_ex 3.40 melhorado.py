
i = 0
op = 's'

while op == 's':
    n = int(input("Digite um numero: "))
    n1 = n
    F = n
    while n > 1:
        i = i + 1
        n = n - 1
        F = F * n
    print ("Fatorial de %i = %i" %(n1 , F))
    op = input("Quer saber o fatorial de outro numero? (s/n): ")