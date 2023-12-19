a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

if (a<b+c) and (b<c+a) and (c<a+b):
    print("É um triangulo")
    if (a==b==c):
        print("É equilatero")     
    elif (a==b) or (a==c) or (b==c):
        print("É isosceles")
    else:
       print("É escaleno")
        
else:
    print("Não é um triangulo")