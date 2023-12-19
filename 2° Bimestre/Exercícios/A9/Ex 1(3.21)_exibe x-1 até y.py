from time import sleep

a = int(input("Digite a: "))
b = int(input("Digite b: "))
maior = max(a,b)
menor = min(a,b)

while maior>=menor:
    print(maior)
    maior = maior - 1
    # maior -= 1
    sleep(1)