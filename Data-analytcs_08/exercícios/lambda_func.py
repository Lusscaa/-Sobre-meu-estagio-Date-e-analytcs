import json
import boto3
import requests
from csv import reader
from datetime import datetime

# Constantes
BUCKET_NAME = 'lucasricardo2'
S3_CSV_FILE_NAME = 'Raw/Local/CSV/Movies/2023/05/26/movies.csv'
S3_JSON_FOLDER_NAME = 'Raw/Local/TMDB/JSON/2023/05/29/'
API_KEY = '535ff58a16b388dea61fa253fe66e1e7'

def get_csv_data():
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=S3_CSV_FILE_NAME)
    csv_data = response['Body'].read().decode('utf-8').splitlines()
    return csv_data

def get_movie_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=pt-BR"
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = json.loads(response.text)
        return movie_data
    return None

def write_json_to_s3(json_data):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    json_file_name = f'movies_data_{timestamp}.json'
    json_file_path = f'/tmp/{json_file_name}'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False)

    s3_json_file_name = S3_JSON_FOLDER_NAME + json_file_name
    s3_client.upload_file(json_file_path, BUCKET_NAME, s3_json_file_name)

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    csv_filmes = get_csv_data()

    total_linhas = len(csv_filmes)
    contador = 0
    previous_movie_id = ''
    json_buffer = []

    for indice, linha in enumerate(reader(csv_filmes, delimiter='|')):
        if 'Action,Adventure' in linha[5]:
            if previous_movie_id != linha[0]:
                previous_movie_id = linha[0]
                movie_data = get_movie_data(previous_movie_id)
               
