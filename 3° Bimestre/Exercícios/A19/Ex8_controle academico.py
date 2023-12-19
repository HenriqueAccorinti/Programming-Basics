# Programa principal
dados = "16.96125-7\t8.5,4.5,7,6\n15.07896-3\t4,5,6,7\n16.06542-3\t7,8.5,7,7.5"

alunos = dados.split("\n")
d = {}
for aluno in alunos:
    linha = aluno.split("\t")
    RA = linha[0]
    notas = linha[1].split(",")
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    d[RA] = notas
    
chaves = list(d.keys())
chaves.sort()
print("%10s\t%5s\t%5s\t%5s\t%5s" %("RA", "P1", "P2", "P3", "P4"))
for RA in chaves:
    print("%10s\t%5s\t%5s\t%5s\t%5s" %(RA, d[RA][0], d[RA][1], d[RA][2], d[RA][3]))
    
RA = input("Digite o RA que deseja saber a média: ")
if RA in d:
    m = sum(d[RA])/len(d[RA])
    print("A média do aluno é: %.1f" %m)
else:
    print("RA não encontrado!")