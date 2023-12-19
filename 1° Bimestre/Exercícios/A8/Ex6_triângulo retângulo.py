a = float(input("digite um numero a: "))
b = float(input("digite um numero b: "))
c = float(input("digite um numero c: "))

if (a<b+c) and (b<a+c) and (c<a+b):
    print("a, b, c podem ser lados de um triangulo")

    h = max(a,b,c)
    cat1 = min(a,b,c)
    cat2 = a+b+c-h-cat1
    
    if (h**2 == cat1**2 + cat2**2):
      print("é um triangulo retangulo")
      print(f"{h:.2f} é a hipotenusa e {cat1:.2f} e {cat2:.2f} sao os dois catetos")
    else: 
        print("nao é um triangulo retangulo")
        
        
else:
    print("a, b, c nao podem ser lados de um triangulo")