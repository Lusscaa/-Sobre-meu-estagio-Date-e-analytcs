import pandas as pd

df = pd.read_csv('actors.csv')

filmes_mais_frequentes = df['#1 Movie'].value_counts().head(1)

filmes = filmes_mais_frequentes.index.tolist()

frequencia = filmes_mais_frequentes.values.tolist()[0]

with open('ex04.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Filme(s) mais frequente(s): " + ', '.join(filmes) + "\n")
    arquivo.write("Frequência: " + str(frequencia))

print("Resultado gravado em ex04.txt")
