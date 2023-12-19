from random import randint

jogadores = ['Goku','Vegeta','Gohan','Videl','N17','N18','Jiren']
print(jogadores)

for numero in range(len(jogadores)-1):
    pos = randint(0,len(jogadores))
    eliminado = jogadores.pop(pos)
    print(jogadores)
    print(eliminado)