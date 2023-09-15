import json
import pandas as pd
database = pd.read_json('broken_database_1.json')
database1 = pd.read_json('broken_database_2.json')

listNomes = []
listMarcas = []

for nome in database['nome']:
    nome = nome.replace('ø','o')
    nome = nome.replace('æ','a')
    listNomes.append(nome) 
database['nome']=listNomes
database.to_json('fixed_database.json',orient='records')

for marca in database1['marca']:
    marca = marca.replace('ø','o')
    marca = marca.replace('æ','a')
    listMarcas.append(marca) 
database1['marca']=listMarcas
database1.to_json('fixed_database1.json', orient='records')


#   ø = o
#   æ = a

# import json

# # Nome do arquivo JSON original
# broken_database = 'broken_database_1.json'

# # Nome do arquivo JSON modificado
# fixed_database = 'fixed_database_1.json'

# #Caracteres que você deseja substituir

# caracter_antigo = ['ø','æ']
# caracter_novo = ['o','a']

# # Abrir o arquivo JSON original para leitura
# with open(broken_database, 'r') as broken_database:
#     #Ler o contéudo do arquivo original
#     broken_arquivo = json.load(broken_database)

# # Função para percorrer o dicionário e substituir caracteres

# def substituir_caracteres(dicionario, antigo, novo):
#     if isinstance (dicionario, dict):
#         for chave, valor in dicionario.items():
#             if isinstance (valor, str):
#                dicionario[chave] = valor.replace(antigo, novo)
#             elif isinstance (valor, (list,dict)):
#                substituir_caracteres(valor, antigo, novo) 
