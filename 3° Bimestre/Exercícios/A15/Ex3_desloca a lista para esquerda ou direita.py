# Programa principal
N = int(input("Digite a quantidade de elementos na lista: "))
L = []
for i in range(N):
    x = int(input("Digite o elemento %i: " %(i+1)))
    L.append(x)

print("Lista original:")
print(L)
    
direção = ""
while direção != "D" and direção != "E":
   direção = input("Qual a direção que deseja deslocar a lista [E/D]: ").upper()

qtd = int(input("Quantas posições deseja deslocar: "))

for i in range(qtd):
    if direção == "E":
        x = L.pop(0)
        L.append(x)
    elif direção == "D":
        x = L.pop()
        L.insert(0, x)
        
print("Lista deslocada:")
print(L)