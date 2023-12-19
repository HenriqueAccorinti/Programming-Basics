
def F1(c):
    cont = 0
    d = 'AEIOU'
    
    for letra in c:
        if letra in d:
            cont += 1
        
    return cont
    

a =input("Digite: ").upper()
b = F1(a)
print (b)