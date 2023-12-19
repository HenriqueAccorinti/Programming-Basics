#Importação dos módulos
from os import *

#Definição das funções
def exibir_quadro(quadro):
    """exibi o quadro de medalhas na forma de Tabela"""
    system("cls")
    print("%10s\t%10s\t%10s\t%10s" %("País", "Ouro", "Prata", "Bronze"))
    for pais in quadro:
        print("%10s\t%10s\t%10s\t%10s" %(pais, quadro[pais]["ouro"], quadro[pais]["prata"], quadro[pais]["bronze"]))
        

#Programa principal
quadro = {}
pais = input("Digite o nome do país: ").title()
while pais != '':
    medalha = input("Digite a medalha conquistada [ouro/prata/bronze]: ").lower()
    if pais not in quadro:
        quadro[pais] = {"ouro":0, "prata":0, "bronze":0}
    quadro[pais][medalha] += 1    
    pais = input("Digite o nome do país: ").title()
    
exibir_quadro(quadro)