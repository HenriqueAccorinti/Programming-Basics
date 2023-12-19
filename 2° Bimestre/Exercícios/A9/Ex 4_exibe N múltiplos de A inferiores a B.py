     
menor = 0
maior = 0
n = 0
i = 0
        
while (menor <= 0) or (maior < menor) or (n <= 0):
        print ("'a' e 'n' devem ser maiores que 0")
        a = float(input("Digite a: "))
        b = float(input("Digite b: "))
        n = int(input("Digite n: "))
        
        maior = max(a,b)
        menor = min(a,b)
        S = menor
        
while (maior > menor) and (i < n):
    print(menor)
    i = i + 1
    menor = menor + S