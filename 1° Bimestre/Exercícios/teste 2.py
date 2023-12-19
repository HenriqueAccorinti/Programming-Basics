	
def EscolherProximoFilme(idade, nFavorito, videoA, videoB):
 if idade > 30:
   return(videoA)
 elif nFavorito < 5:
   return(videoB)
 else:
   return(videoA)
   
i = int(input("i="))
n = int(input("n="))
vA = int(input("A"))
vB = int(input("B"))

y = EscolherProximoFilme(i, n, vA, vB)
print (y)