def novaSenha(senha):
  ns=""
  letras="ABCEGHIOQSTXZ"
  numeros = "48(36#10957%2"
  for letra in senha.upper():
    p = letras.find(letra)
    if p != -1:
      ns += numeros[p]
    else:
      ns += letra
  print(ns)
  
senha='senhalegal'
novaSenha(senha)