import pandas as pd

df = pd.read_csv('actors.csv')

df['Average per Movie'] = df['Total Gross'] / df['Number of Movies']

maior_media = df.loc[df['Average per Movie'].idxmax()]

ator_ou_atriz = maior_media['Actor']

with open('ex03.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Ator/Atriz com maior média por filme: " + ator_ou_atriz)

print("Resultado gravado em ex03.txt")
