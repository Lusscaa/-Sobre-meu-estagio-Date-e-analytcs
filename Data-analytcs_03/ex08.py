primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for j, nome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[j]
    idade = idades[j]
    print('{} - {} {} está com {} anos'.format(j, nome, sobrenome, idade))