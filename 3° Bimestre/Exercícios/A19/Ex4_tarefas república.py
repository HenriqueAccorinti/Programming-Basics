# Programa principal
tarefas = {}
op = "S"
while op == "S":
    nome = input("Digite o nome: ").title()
    tarefa = input("Digite a tarefa: ")
    dia = input("Digite o dia: ").lower()
    if nome not in tarefas:
        tarefas[nome] = {dia: tarefa}
    else:
        if dia not in tarefas[nome]:
            tarefas[nome][dia] = tarefa
        else:
            print("%s já tem uma tarefa em %s." %(nome, dia))
            
    op = input("Deseja inserir outra tarefa [S/N]: ").upper()
    
dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
for d in dias:
    print(d)
    for p in tarefas:
        if d in tarefas[p]:
            print("%s deve %s" %(p, tarefas[p][d]))
    print()