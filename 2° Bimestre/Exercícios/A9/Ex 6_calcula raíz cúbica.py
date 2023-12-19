a = float(input("Digite um valor: "))
x = a

while abs(x**3 - a) > (1E-6):
    x -= (x**3 - a)/(3*x**2)
print('A raíz cúbica de %f vale: %.2f' %(a,x))