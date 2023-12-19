D = 1
s = 0
sinal = 1
while 1/D > 1e-7:
    s = s + sinal*4/D
    D += 2
    sinal = -sinal
print(s)