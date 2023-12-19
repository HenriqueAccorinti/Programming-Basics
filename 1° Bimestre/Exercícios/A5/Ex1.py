def formatarHorario(h, m, s):
    """formata o horario no padrão xxhxxmxxs"""
    print("%02ih%0im%02is" % (h, m, s))

# programa principal
h = 3
m = 15
s = 7
formatarHorario(h, m, s)