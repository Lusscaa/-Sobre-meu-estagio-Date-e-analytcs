def conta_vogais(texto:str)-> int:
    vogais = ["a","e","i","o","u","A","E","I","O","U"]
    return len(list(filter(lambda x: x in vogais, texto)))

print(conta_vogais(texto="Abradacabra"))
