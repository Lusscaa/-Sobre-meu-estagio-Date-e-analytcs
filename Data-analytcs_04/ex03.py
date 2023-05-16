from functools import reduce

def calcula_saldo(lancamentos) -> float:
    #continue este cÃ³digo
    valores = list(map(lambda x: x[0] if x[1] == "C" else -x[0], lancamentos))
    res = reduce(lambda x,y: x+y, valores)
    return res

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
    ]

print(calcula_saldo(lancamentos))