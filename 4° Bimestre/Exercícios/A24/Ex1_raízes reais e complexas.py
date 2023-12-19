import numpy as np

n = int(input("Digite o grau do polinômio: "))
coefs = []

for i in range (n+1):
    c = float(input("Digite o a%i: " %(n-i)))
    coefs.append(c)
    
P = np.poly1d(coefs)
print(P)

rReal = []
rImag = []

for raiz in P.r:
    if np.imag(raiz) == 0:
        rReal.append(float(np.real(raiz)))
    else:
        rImag.append(raiz)
        
print("Raízes reais:",rReal)
print("Raízes complexas:",rImag)