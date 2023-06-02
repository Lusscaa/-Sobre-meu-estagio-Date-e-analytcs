import random
import time
import os
import names
import csv

# [Warm up] Reverse em uma lista de inteiros
lista_inteiros = random.sample(range(1, 1001), 250)
lista_inteiros.reverse()
print(lista_inteiros)

# [Warm up] Ordenação de animais em ordem crescente
animais = ['Cachorro', 'Gato', 'Elefante', 'Leão', 'Tigre', 'Girafa', 'Macaco', 'Coelho', 'Panda', 'Zebra', 'Urso', 'Cavalo', 'Pinguim', 'Leopardo', 'Rinoceronte', 'Gorila', 'Camelo', 'Hipopótamo', 'Rato', 'Vaca']
animais_ordenados = sorted(animais)
for animal in animais_ordenados:
    print(animal)

# Salvando os animais em um arquivo CSV
with open('animais.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for animal in animais_ordenados:
        writer.writerow([animal])

# [Laboratório] Gerando um dataset de nomes de pessoas
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open('nomes_aleatorios.txt', 'w') as arquivo_nomes:
    for nome in dados:
        arquivo_nomes.write(nome + '\n')

# Verificando o conteúdo do arquivo
with open('nomes_aleatorios.txt', 'r') as arquivo_nomes:
    conteudo = arquivo_nomes.read()
    print(conteudo)
