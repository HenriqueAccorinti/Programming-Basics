# Definição das funções
def lerProjetos(projetos, N):
    """preenche um dicionário com as informações dos projetos"""
    for i in range(N):
        cod = input("Digite o código do projeto %i: " %(i + 1)).upper()
        tempo = int(input("Digite o tempo de execução do projeto %i: " %(i + 1)))
        projetos[cod] = tempo

# Programa principal
projetos = {}
N = int(input("Digite quantos projetos deseja cadastrar: "))
lerProjetos(projetos, N)
chaves = list(projetos.keys())
chaves.sort()
print("%10s\t%s" %("Projeto", "Tempo"))
for c in chaves:
    print("%10s\t%s" %(c, projetos[c]))