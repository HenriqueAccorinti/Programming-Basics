L = []
  #Cria uma lista vazia

N = int(input("Quantos elementos deseja digitar: "))
i = 0
while i <N:
    x = int(input("Digite o elemento %i: " %i)) #x deve ser real
    L.append(x) #Adiciona x ao final da lista
    i = i + 1

 

media = sum(L)/len(L)
  #Calcula a média


L.sort()
if len(L)%2 == 0:
    mediana = (L[len(L)//2] + L[len(L)//2 - 1])/2
  #Cálculo da mediana se a quantidade for par
else:
    mediana = L[len(L)//2]
  #Cálculo da mediana se a quantidade for impar


print("A média é %.2f e a mediana é %.2f." %(media, mediana ))