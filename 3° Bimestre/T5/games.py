#programa principal 
N = int(input("Digite a quantidade de jogos que deseja comprar: "))
L = {} #inicialização do local onde os jogos serão salvos

for i in range(N):
    jogo = input("Digite o nome do jogo: ").upper()
    L [jogo] = {"loja" : "", "preço": 9999}

op = "S"
while op == "S":
    jogo = ""
    while jogo not in L :
        jogo = input("Qual jogo deseja atualizar o preço: ").upper()
        if jogo not in L:
            print("Jogo não encontrado, informe um nome válido que esteja na lista!")
    loja = input("Digite o nome da loja: ")
    preço = float(input("Digite o preço do jogo %s na loja %s: " % (jogo,loja)))
    if preço < L[jogo]["preço"]:
        L[jogo]["loja"] = loja #atualiza loja
        L[jogo]["preço"] = preço #atualiza preço
    op = input("Deseja atualizar outro jogo [S/N]: ").upper()

total = 0
for jogo in L:
    total += L[jogo]['preço']
    print("O melhor lugar para você comprar o jogo %s é na loja %s com o preço de: R$%.2f" % (jogo,L[jogo]["loja"],L[jogo]["preço"]))
print("O total que você vai gastar com jogos é: R$%.2f" % total)