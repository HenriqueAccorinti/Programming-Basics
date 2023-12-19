def formatarHorario(d, h, m, s):
    """formata o horario no padrão xxhxxmxxs"""
    h = h + 24*d
    print("%02ih%0im%02is" % (h, m, s))

# programa principal

d = int(input("Digite o número de dias: "))
h = int(input("Digite o número de horas: "))
m = int(input("Digite o número de minutos: "))
s = int(input("Digite o número de segundos: "))

formatarHorario(d, h, m, s)