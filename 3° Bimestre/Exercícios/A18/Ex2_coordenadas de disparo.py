# Programa principal
tiros = {}
op = "S"
while op == "S":
    x = float(input("Digite a coordenada x do disparo: "))
    y = float(input("Digite a coordenada y do disparo: "))
    d = (x**2 + y**2)**(1/2)
    tiros[(x,y)] = 10 - d//10
    op = input("Deseja cadastrar um outro disparo [S/N]: ").upper()

pt_max = max(tiros.values())
print("Pontuação máxima:", pt_max)    
print("Melhores Pontuações")
print("%15s\t%s" %("Disparo", "Pontuação"))
for d in tiros:
    if tiros[d] == pt_max:
        print("%15s\t%s" %(d, tiros[d]))