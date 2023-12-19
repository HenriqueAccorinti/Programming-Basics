i = 0
n = int(input("Digite um numero: "))
n1 = n
F = n
while n > 1:
    i = i + 1
    n = n - 1
    F = F * n
print ("Fatorial de %i = %i" %(n1 , F))

#n = int(input("Digite um número: "))
#f = 1
#i = 1
#while i <= n:
#    f *= i
#    i += 1
#print ("%i! = %i" % (n,f))