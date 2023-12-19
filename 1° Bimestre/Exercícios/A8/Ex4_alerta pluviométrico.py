A= float(input("Digite a altura de água (mm): "))
D= float(input("Digite a duração da medição (h): "))
I=A/D

if I<3:
    print("O índice de alerta pluviométrico é considerado normal")
elif 3<=I<8:
    print("O índice de alerta pluviométrico é considerado crítico")
else:
    print("O índice de alerta pluviométrico é considerado alarmante")