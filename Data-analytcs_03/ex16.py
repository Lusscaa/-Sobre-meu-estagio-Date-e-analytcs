def soma_string_numeros(string):
    numeros = string.split(',')
    soma = 0
    for num in numeros:
        soma += int(num)
    return soma


s = "1,3,4,6,10,76"
resultado = soma_string_numeros(s)
print(resultado)
