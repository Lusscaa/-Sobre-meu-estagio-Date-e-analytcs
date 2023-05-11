import pandas as pd

df = pd.read_csv('actors.csv')

media_filmes = df['Number of Movies'].mean()

with open('ex02.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Média de número de filmes: " + str(media_filmes))

print("Média gravada em ex02.txt")
