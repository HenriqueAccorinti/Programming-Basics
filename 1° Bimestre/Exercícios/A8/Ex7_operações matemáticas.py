def operação(a,b,c):

    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b==0:
            r="divisão por zero"
        else:
           r=a/b 
    else:
        r="operador inválido"
            
    return r

a=float(input("digite um número:"))
b=float(input("digite outro número:"))
c=input("digite um operador matematico:")
resp=operação(a,b,c)
print(resp)