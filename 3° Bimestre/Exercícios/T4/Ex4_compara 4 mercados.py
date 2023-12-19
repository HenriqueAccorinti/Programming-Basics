# exibe a tabela com o cabeçalho dos mercados

def exibirTabela( Tab, Merc ):
    Tab.sort()

    print("               \t%7s\t%7s\t%7s\t%7s" %tuple(Merc))
    
    for linha in Tab:
        print("%15s\t%7s\t%7s\t%7s\t%7s" % tuple(linha))


# programa principal

# cadastro da lista de mercados
Mercados = []
for i in range(4):
    mercado = input("Digite o nome de um mercado: ").upper()
    Mercados.append( mercado )

# cadastro dos produtos
N = int(input("Digite a quantidade de itens: "))
Tabela = []

for i in range(N):
    produto = input("Digite o nome do produto: ")
    Tabela.append([produto,False,False,False,False])
 
op = 'S'
while op == 'S':
    produto = input("Digite o nome do produto: ")
    mercado = input("Digite o mercado: ").upper()

    if mercado in Mercados:
        m = Mercados.index( mercado ) + 1
        for linha in Tabela:
            if linha[0] == produto:
                linha[m] = True

    exibirTabela(Tabela,Mercados)   

    op = input("Outro produto (S/N)? ").upper()