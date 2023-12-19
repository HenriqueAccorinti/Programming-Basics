from math import sqrt

def LerValores(X,N):
    for i in range(N):
        v = float(input("digite o valor i%: " %(i+1)))
        X.append(v)
        

N = int(input("Digite a quantidade de valores: "))
X = []
LerValores(X,N)
print(X)

m = sum(X)/N

s = 0
for i in range(N):
    s += abs(X[i]-m)**2
dp = sqrt(s/(N-1))

print("Média = %.3f\nDesvio Padrão = %.3f" %(m, dp))