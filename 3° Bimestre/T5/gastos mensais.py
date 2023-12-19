def exibe_extrato(conta):
    """exibe o extrato da conta bancária"""
    print("%42s" %"Extrato Bancário")
    print("%10s\t%10s\t%10s\t%10s" %("Dia", "Depósito", "Saque", "Pagamento"))
    for dia in range(1,32):
        if (dia in conta["D"]) or (dia in conta["S"]) or (dia in conta["P"]):
            print("%10s\t" %dia, end = "")
            if (dia in conta["D"]):
                print("%10.2f\t" %conta["D"][dia], end = "")
            else:
                print("%10s\t" %" ", end = "")
            if (dia in conta["S"]):
                print("%10.2f\t" %conta["S"][dia], end = "")
            else:
                print("%10s\t" %" ", end = "")
            if (dia in conta["P"]):
                print("%10.2f\t" %conta["P"][dia], end = "")
            else:
                print("%10s\t" %" ", end = "")
            print()
        
def exibe_saldo(conta):
    """exibe o saldo da conta"""
    saldo = 0
    for op in conta["D"]:
        saldo += conta["D"][op]
    for op in conta["S"]:
        saldo -= conta["S"][op]
    for op in conta["P"]:
        saldo -= conta["P"][op]
    print("\nO saldo total da conta é: R$%.2f" %saldo)

# Programa principal
conta = {'D': {}, 'S': {}, 'P': {}}  
op = ''
while op != 'F':
    op = input("Digite a operação bancária (D/S/P) ou F para sair: ").upper()
    if op in conta:
        valor = float(input("Digite o valor: "))
        dia = int(input("Digite a dia da operação: "))
        conta[op][dia] = valor
    else:
        if op != "F":
            print("Operação Inválida!")

exibe_extrato(conta) # exibe o extrato
exibe_saldo(conta) # exibe o saldo