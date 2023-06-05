import json
import boto3
import requests
import csv

# Configurações do Amazon S3
aws_access_key_id = 'AKIAZTNN5SJXGDHX7XNC'
aws_secret_access_key = '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'
aws_s3_bucket = 'lucasricardo'

# Configurações do TMDB
tmdb_api_key = '535ff58a16b388dea61fa253fe66e1e7'

s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Variáveis para controle das linhas/requisições
total_linhas = 0
total_requisicoes = 0

# Obter dados do CSV
def get_csv_data():
    file_key = 'Raw/Local/CSV/Movies/2023/05/26/movies.csv'
    response = s3_client.get_object(Bucket=aws_s3_bucket, Key=file_key)
    csv_data = response['Body'].read().decode('utf-8')

    process_csv_data(csv_data)

# Processar os dados do CSV
def process_csv_data(csv_data):
    global total_linhas
    global total_requisicoes

    csv_reader = csv.reader(csv_data.splitlines())
    next(csv_reader)  # Pula o cabeçalho do CSV

    for row in csv_reader:
        # Processar cada linha do arquivo CSV
        # Exemplo: imprimir o conteúdo de cada linha
        print(row)

        total_linhas += 1
        total_requisicoes += 1

        # Verificar se atingiu 100 linhas/requisições com sucesso
        if total_requisicoes % 100 == 0:
            criar_arquivo_json()

# Criar arquivo JSON
def criar_arquivo_json():
    global total_linhas

    # Nome do arquivo baseado no número total de linhas
    nome_arquivo = f'dados_{total_linhas}.json'

    # Dados a serem gravados no arquivo JSON
    dados = {
        'total_linhas': total_linhas,
        'total_requisicoes': total_requisicoes
    }

    # Converter dados em formato JSON
    json_data = json.dumps(dados)

    # Enviar arquivo JSON para o Amazon S3
    s3_client.put_object(Body=json_data, Bucket=aws_s3_bucket, Key=nome_arquivo)

    # Reiniciar o contador de requisições
    total_requisicoes = 0

# Chamar a função para obter os dados do CSV
get_csv_data()