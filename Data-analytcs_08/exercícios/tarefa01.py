import requests
import pandas as pd
from IPython.display import display

api_key = "535ff58a16b388dea61fa253fe66e1e7"
movie_id = 87827  # ID do filme "Life of Pi"

url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

if 'title' in data:
    filme = {
        'Titulo': data['title'],
        'Data de lançamento': data['release_date'],
        'Visão geral': data['overview'],
        'Votos': data['vote_count'],
        'Média de votos:': data['vote_average']
    }

    df = pd.DataFrame([filme])
    display(df)
else:
    print("Filme não encontrado.")