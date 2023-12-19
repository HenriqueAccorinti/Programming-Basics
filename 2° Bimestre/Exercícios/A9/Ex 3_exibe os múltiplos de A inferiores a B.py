a = float(input("Digite a: "))
b = float(input("Digite b: "))
maior = max(a,b)
menor = min(a,b)
S = menor

while maior>menor:
    print(menor)
    menor = menor + S