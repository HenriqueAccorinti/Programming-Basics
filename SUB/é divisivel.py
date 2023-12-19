# Definição das Funções
def divisivel(x,y):
    if x%y == 0:
        return True
    else:
        return False
 
# Programa Principal
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

resp = divisivel(x,y)
# verifica se x é divisível por y

if resp:
    print("sim")

else:
    print("não")
