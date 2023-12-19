from math import sqrt

def Lado( x1, y1, x2, y2 ) :
    return sqrt( (x2-x1)**2 + (y2-y1)**2)

#programa principal
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))
x3 = float(input("Digite x1: "))
y3 = float(input("Digite x2: "))

A = Lado(x1, y1, x2, y2)
B = Lado(x2, y2, x3, y3)
C = Lado(x1, y1, x3, y3)

S = (A+B+C) / 2
Area = sqrt( S * (S-A) * (S-B) * (S-C) )

print(Area)

#from math import sqrt
#
#def Lado( x1, y1, x2, y2 ) :
#    return sqrt( (x2-x1)**2 + (y2-y1)**2 )
#
## programa principal
#x1 = float(input("Digite x1: "))
#y1 = float(input("Digite y1: "))
#x2 = float(input("Digite x2: "))
#y2 = float(input("Digite y2: "))
#x3 = float(input("Digite x3: "))
#y3 = float(input("Digite y3: "))
#
#A = Lado(x1, y1, x2, y2)
#B = Lado(x2, y2, x3, y3)
#C = Lado(x1, y1, x3, y3)
#
#S = (A+B+C) / 2
#Area = sqrt( S * (S-A) * (S-B) * (S-C) )
#
#print(Area)