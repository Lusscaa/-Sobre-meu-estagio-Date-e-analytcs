import json

with open('person.json', 'r') as x:
    conteudo = x.read()
    dados = json.loads(conteudo)
    print(dados)