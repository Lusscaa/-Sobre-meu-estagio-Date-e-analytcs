import json
import boto3
import requests

# Configurações do Amazon S3
aws_access_key_id = 'AKIAZTNN5SJXGDHX7XNC'
aws_secret_access_key = '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'
aws_s3_bucket = 'lucasricardo'

# Configurações do TMDB
tmdb_api_key = '535ff58a16b388dea61fa253fe66e1e7'

# Criar instância do cliente S3
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Obter dados do TMDB
def get_tmdb_data():
    movie_id = 87827  # ID do filme "Life of Pi"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=pt-BR"
    response = requests.get(url)
    data = response.json()

    # Salvar os dados obtidos em um arquivo JSON no S3
    json_data = json.dumps(data)
    s3_client.put_object(Body=json_data, Bucket=aws_s3_bucket, Key=f'movies/{movie_id}.json')

# Chamar a função para obter os dados do TMDB
get_tmdb_data()
