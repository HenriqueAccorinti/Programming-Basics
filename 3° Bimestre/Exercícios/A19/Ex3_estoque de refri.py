# Definição das funções
def valor_estoque(L):
    """retorna o valor total em estoque"""
    s = 0
    for i in L:
        s = s + i["quantidade"]*i["preço"]
    return s

def comprar_refri(L):
    """exibe os refrigerantes em falta no estoque"""
    print("\nComprar esses refrigerantes:")
    for i in L:
        if i["quantidade"] == 0:
            print("%s (%s)" %(i["nome"], i["origem"]))

# Programa principal
Lista = []
N = int(input("Digite a quantidade de refrigerantes: "))
for i in range(N):
    nome = input("Digite o nome do refrigerante: ")
    origem = input("Digite a origem do refrigerante %s: " %nome)
    quantidade = int(input("Digite a quantidade do refrigerante %s: " %nome))
    preço = float(input("Digite o preço do refrigerante %s: " %nome))
    d = {"nome": nome, "origem": origem, "quantidade": quantidade, "preço": preço}
    Lista.append(d)

# Lista = [
# {'nome':'Etubaina Orlando', 'origem':'Piracicaba', 'quantidade':25, 'preço':3.50},
# {'nome':'Cotuba', 'origem':'São José do Rio Preto', 'quantidade':20, 'preço':3.50},
# {'nome':'Gengibirra Limonge', 'origem':'Rio das Pedras', 'quantidade':12, 'preço':3.00},
# {'nome':'Inca Kola', 'origem':'Peru', 'quantidade':2, 'preço':12.00},
# {'nome':'Guaraná Jesus', 'origem':'Maranhão', 'quantidade':0, 'preço':4.50}
# ]
    
total = valor_estoque(Lista)
print("O valor total em estoque é: R$%.2f" %total)
comprar_refri(Lista)