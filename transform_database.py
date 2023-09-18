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



