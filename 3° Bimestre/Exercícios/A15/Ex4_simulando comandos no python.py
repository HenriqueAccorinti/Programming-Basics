from math import sin, radians

def soma(lista):
    return sum(lista)

def seno(x):
    return sin(radians(x))

def trapezio(B,b,h):
    return ((B + b)*h)/2

comando = input("Digite um comando: ").lower()
comando = comando.replace(' ','')
comando = comando.replace(')','')

comando = comando.split('(')
parametros = comando[1]
comando = comando[0]

parametros = parametros.split(",")
for i in range(len(parametros)):
    parametros[i] = float(parametros[i])

if comando == 'seno':
    resp = seno(parametros[0])
elif comando == 'trpazio':
    resp = trapezio(parametros[0],parametros[1],parametros[2])
elif comando == 'soma':
    resp = soma(parametros)
else:
    resp = "erro: comando não encontrado"
    
print(resp)