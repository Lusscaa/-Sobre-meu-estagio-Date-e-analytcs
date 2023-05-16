import pandas as pd

df = pd.read_csv('actors.csv')

maior_num_filmes = df.loc[df['Number of Movies'].idxmax()]

ator_ou_atriz = maior_num_filmes['Actor']

num_filmes = maior_num_filmes['Number of Movies']

with open('ex01.txt', 'w', encoding='utf-8') as arquivo:
    print("Ator/Atriz com maior número de filmes:", ator_ou_atriz, file=arquivo)
    print("Número de filmes:", num_filmes, file=arquivo)

print("Ator/Atriz com maior número de filmes:", ator_ou_atriz)
print("Número de filmes:", num_filmes)
