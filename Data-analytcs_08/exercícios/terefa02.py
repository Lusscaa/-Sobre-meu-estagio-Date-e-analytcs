import json
import boto3
import requests

# Configurações do Amazon S3
aws_access_key_id = 'AKIAZTNN5SJXGDHX7XNC'
aws_secret_access_key = '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'
aws_s3_bucket = 'lucasricardo2'

# Configurações do TMDB
tmdb_api_key = '535ff58a16b388dea61fa253fe66e1e7'

s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Obter dados do TMDB
url = f"https://api.themoviedb.org/3/discover/movie?api_key={tmdb_api_key}&language=pt-BR&with_genres=28,12"
response = requests.get(url)
data = response.json()
results = data['results']

file_index = 1
movies_list = []
line_count = 0

for result in results:
    movies_list.append(result)
    line_count += 1

    # Verificar se atingiu 100 linhas ou é o último filme
    if line_count >= 100 or result == results[-1]:
        subset_data = {'results': movies_list}
        json_data = json.dumps(subset_data)
        file_key = f'movies/action_adventure_movies_{file_index}.json'
        s3_client.put_object(Body=json_data, Bucket=aws_s3_bucket, Key=file_key)
        movies_list = []
        line_count = 0
        file_index += 1