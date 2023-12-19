import webbrowser, sys, requests, bs4, json

CEP = input("Digite o CEP desejado: ")
res = requests.get('https://viacep.com.br/ws/'+CEP+'/json/')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
JSON_Datalist = soup.get_text()
dados = json.loads(JSON_Datalist)

if 'erro' in dados:
    print("CEP inválido.")    
else:
    print('CEP: %s' % dados['cep'])
    print('Endereço: %s' % dados['logradouro'])
    print('Complemento: %s' % dados['complemento'])
    print('Bairro: %s' % dados['bairro'])
    print('Cidade: %s' % dados['localidade'])
    print('Estado: %s' % dados['uf'])
    