from math import sqrt, sin, radians

def funcao(x):
    y = sqrt(sin(radians(x))**2+2*x)
    return y

h = (1/10)**5
Xo = float(input("Digite Xo: "))
X1 = Xo + h/2
X2 = Xo - h/2

msec = (funcao(X1) - funcao(X2))/h
print("A inclinação da reta é: %.2f" %msec)

#from math import *
#
#def f(x) :
#    return sqrt(sin(radians(x))**2 + 2*x)
#    
#xo = float(input("Digite o valor de xo: "))
#h = 1e-5
#msec = (f(xo+h/2)-f(xo-h/2))/h
#print ("Coeficiente algular em %.3f = %.3f" % (xo, msec))