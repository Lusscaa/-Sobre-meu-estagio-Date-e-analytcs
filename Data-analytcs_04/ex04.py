def calcular_valor_maximo(operadores, operandos):
    
    numeros = list(zip(operadores, operandos))


    funcoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '%': lambda a, b: a % b
    }

    resultados = list(map(lambda x: funcoes[x[0]](x[1][0], x[1][1]), numeros))

    # Retorna o resultado máximo
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos))
