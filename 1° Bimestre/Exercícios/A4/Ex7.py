from math import *

def CalcularAltura(Ho,comp,ang):
    """
    Calcula e retorna a altura do vértice
    mais alto de um trapézio, a partir a altura do vértice mais
    baixo, da distância horizontal entres esses vértices e do
    ângulo, em graus.
    """
    rad = radians(ang) #converte graus em radianos
    H = Ho + tan(rad) * comp
    return H

def AreaTrapezio(H,Ho,comp):
    """
    Calcula e retorna a área de um trapézio, recebendo via parâmetro os
    lados maior, menor e a distância entre eles.
    """
    A = (H+Ho)/2 * comp
    return A

comp = float(input("Digite o comprimento: "))
larg = float(input("Digite a largura: "))
Ho = float(input("Digite a altura Ho: "))
a = float(input("Digite o ângulo a: "))
b = float(input("Digite o ângulo b: "))

 #calcular altura maior de cada trapézio:
Hf1 = CalcularAltura(Ho,comp,a)
Hf2 = CalcularAltura(Ho,larg,b)
Hf3 = CalcularAltura(Hf1,larg,b)

#calcular a área de cada trapézio:
Af1 = AreaTrapezio(Hf1,Ho,comp)
Af2 = AreaTrapezio(Hf2,Ho,larg)
Af3 = AreaTrapezio(Hf3,Hf1,larg)
Af4 = AreaTrapezio(Hf3,Hf2,comp)

#calcular a área total do trapézio:
AT = Af1 + Af2 + Af3 + Af4
print("A área lateral do duto é: %.2f cm2" %AT)

#from math import radians, tan
#
#def AreaTrapezio( B, b, h) :
#    return ( B + b ) * h / 2
#
#def CalcularAltura( hMenor, dH, ang ) :
#    ang = radians(ang)
#    return hMenor + dH*tan(ang)
#
## programa principal
#Comp = float(input("Digite o comprimento do duto: "))
#alfa = float(input("Digite o ângulo nessa direção: "))
#Larg = float(input("Digite a largura do duto: "))
#beta = float(input("Digite o ângulo nessa direção: "))
#Ho = float(input("Digite a menor altura: "))
#
#HC = CalcularAltura(Ho, Comp, alfa)
#HL = CalcularAltura(Ho, Larg, beta)
#HT = CalcularAltura(HL, Comp, alfa) 
#
#T1 = AreaTrapezio(Ho, HL, Larg)
#T2 = AreaTrapezio(Ho, HC, Comp)
#T3 = AreaTrapezio(HL, HT, Comp)
#T4 = AreaTrapezio(HC, HT, Larg)
#
#Area = T1 + T2 + T3 + T4
#print("Área da caixa: %.2f" % Area)