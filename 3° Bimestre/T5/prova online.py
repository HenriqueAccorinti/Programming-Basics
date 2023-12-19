# mensagens cadastradas no sistema
msgs = {
    "fim": "O tempo da prova terminou. Você será desconectado e suas respostas salvas.",
    "wc": "Tudo bem. Você pode se ausentar durante 3 minutos.",
    "aguarde": "Por favor, aguarde um instante.",
    "ajuda": "Posso ajudar?",
    "celular": "Você está olhando muito para baixo. Não é permitido o uso de outros dispositivos durante a prova. Caso isso se repita, você será desclassificado.",
    "360": "Você está olhando muito para o lado. Por favor, gire a câmera 360° mostrando todo o ambiente em que você está.",
    "conversa": "Estou captando uma conversa próximo à você. Não é permitido que outras pessoas estejam no mesmo ambiente que você durante a prova.",
    "cadastro": "Por favor, coloque a foto do seu documento de identidade (RG, CNH ou RNE) em frente a sua câmera, com a parte da foto visível.",
    "doc virado": "Prezado candidato, a foto do documento está mostrando os seus dados, entretanto deveria mostrar a sua foto. Por gentileza, refaça o procedimento de identificação.",
    "foto escura": "Sua foto está muito escura. Ilumine o ambiente e refaça o procedimento.",
    "foto doc": "Prezado candidato, a foto do documento não está visível. Por gentileza, refaça o procedimento de identificação.",
    "foto cand": "Prezado candidato, a captura da sua foto não ficou adequadamente visível. Por favor refaça o procedimento de captura de sua imagem.",
    "breve": "Vamos iniciar a prova em breve!",
    "início": "Pode iniciar a prova!",
    "não": "Não é possível neste momento."
}

pc = input("Digite a palavra-chave: ").lower()

while pc != '':
    if pc in msgs:
        print(msgs[pc])
    
    else:
        lista = []
        for item in msgs:
            if pc in msgs[item]:
                lista.append(msgs[item])
        lista.sort()
        print("Foram encontradas %i mensagens relacionadas.\n" % len(lista))
        
        for item in lista:
            print(item)
            print()
            
    pc = input("Digite a palavra-chave: ").lower()
    