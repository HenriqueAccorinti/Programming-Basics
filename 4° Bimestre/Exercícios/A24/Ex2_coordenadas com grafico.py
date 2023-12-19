import matplotlib.pyplot as plt

F={(-3.0,-3.0):'y',(-3.0,-2.9):'w',(-3.0,-2.8):'w'}
ListaF =list(F.keys())
print(F)
print()
print(ListaF)

X=[]
Y=[]
cor=[]
cont = 0


for i in ListaF:
    X.append(i[0])
    Y.append(i[1])
    cor += F[i]
    if F[i] == 'w':
        cont += 1
    
    
print()
print(X)
print(Y)
print(cor)
print()
print(cont)
for i in range(len(list(F.keys()))):
    plt.plot(X[i],Y[i], color=F[(X[i],Y[i])], marker='o')
    
plt.show()