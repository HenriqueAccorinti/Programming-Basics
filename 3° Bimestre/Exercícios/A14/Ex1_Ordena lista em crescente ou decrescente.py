N = int(input("Digite o número de itens: "))
L = []

i = 0
while i < N:
    x = float(input("Digite o elemento %i: " %(i + 1)))
    L.append(x)
    i = i + 1

op = input("Deseja ordenar em ordem crescente ou decrescente [C/D]: ").upper()
if op == 'C':
    L.sort()
else:  
    L.sort(reverse = True)

print(L)