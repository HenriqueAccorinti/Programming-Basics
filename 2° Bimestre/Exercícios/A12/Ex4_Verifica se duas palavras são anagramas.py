def VerificarAnagrama(p1, p2):
    resp = False
    cont = 0
    if len(p1) == len (p2):
        for letra in p1:
            if p1.count(letra) == p2.count(letra):
                cont += 1
        resp = len(p1) == cont
    return resp
    
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if VerificarAnagrama(palavra1, palavra2):
    print("São anagramas")
else:
    print("Não são anagramas")