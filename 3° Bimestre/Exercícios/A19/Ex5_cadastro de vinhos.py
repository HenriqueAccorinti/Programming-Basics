# Programa principal
Lista = []
N = int(input("Digite a quantidade de vinhos: "))
for i in range(N):
    nome = input("Digite o nome do vinho: ")
    vinicola = input("Digite o nome da vinícola: ")
    safra = int(input("Digite o ano da safra: "))
    pais = input("Digite o país de origem: ")
    uva = input("Digite o tipo da uva: ")
    quant = int(input("Digite a quantidade: "))
    d = {"nome": nome,
         "vinicola": vinicola,
         "safra": safra,
         "pais": pais,
         "uva": uva,
         "quant": quant}
    Lista.append(d)
    
uvas = {}
for vinho in Lista:
    if vinho["quant"] != 0:
        if vinho["uva"] not in uvas:
            uvas[vinho["uva"]] = 1
        else:
            uvas[vinho["uva"]] += 1
            
chaves = list(uvas.keys())
chaves.sort()
for uva in chaves:
    print("%s: %i" %(uva, uvas[uva]))