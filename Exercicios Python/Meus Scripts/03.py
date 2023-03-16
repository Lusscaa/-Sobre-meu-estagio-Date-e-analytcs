from random import random

def moeda():
    valor = random()
    if valor > 0.5:
        return "cara"
    return "Coroa"

print('Vamo Lá {} '.format(moeda()))
