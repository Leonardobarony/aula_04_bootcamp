import csv

# Caminho para o csv
caminho_do_arquivo: str = 'exemplo.csv'

# Inicializa uma lista para armazenar os dados
arquivo_csv: list = []

# usa o gerenciador de contexto "with" para abrir e fechar o arquivo apos rodar
with open(file=caminho_do_arquivo, mode='r' , encoding='utf-8') as arquivo:
    #Cria um objeto leitor de csv
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)