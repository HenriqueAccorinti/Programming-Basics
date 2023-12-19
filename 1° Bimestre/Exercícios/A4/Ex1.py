import math
G = float(input("Digite o ângulo de inclinação do seu canhão em graus: "))
V = float(input("Digite a velocidade do seu projétil em km/m: "))

def Alcance(Vo,teta):
    """
    Retorna a distância percorrida pelo projétil em metros,
    dados o ângulo (graus) e a velocidade do projétil (km/h)
    """

    M = Vo * 3.6 # conversão km/h em m/s
    R = math.pi/180 * teta # conversão graus em radianos
    g = 9.81
    S = M**2/g * math.sin(2*R)
    return(S)
    
Y = Alcance(V,G)
print("O alcance do seu projétil é: %.1f m" %Y)

#from math import *
#
#def Alcance(Vo,ang):
#    g = 9.81
#    ang = ang * pi / 180
#    S = Vo**2/g * sin(2*ang)
#    return S
#
#Vo = float(input("Digite a velocidade: "))
#teta = float(input("Digite o ângulo: "))
#S = Alcance(Vo, teta)
#print("Alcance: %.2f m" % S)