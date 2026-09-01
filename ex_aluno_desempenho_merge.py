# EX_1
import pandas as pd
df_localidades = pd.read_excel("alunos_localidade_carro_merge.xlsx")
df_alunos = pd.read_csv("alunos_desempenho.csv")
df_alunos.info()
df_localidades.info()

#EX_2
pd.merge(df_alunos, df_localidades, on="id_aluno", how="left")

#EX_3

#EX_4
df_localidades.shape
df_alunos.shape

#EX_5

df = pd.merge(df_alunos, df_localidades, on="id_aluno", how="left")
df.info()

#EX_6

pd.merge(df_alunos, df_localidades, on="id_aluno", how="outer", indicator=True)

#EX_7

#EX_8

import requests
import pandas as pd
ceps = df["cep"].unique()
dados_ceps = []
print(dados_ceps)
for cep in ceps:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    dados = response.json()
    dados_ceps.append(dados)
    print(cep)
df_endereço =pd.DataFrame(dados_ceps)

#EX_9

import requests

endereco = "SQN 216 Brasília DF"
url = "https://nominatim.openstreetmap.org/search"

params ={
    "q": endereco,
    "format": "json",
    "limit": 1,
    "countrycodes": "br"
}
headers ={"User-Agent": "meu_projeto_geocoding/1.0"}
response = requests.get(url, params=params, headers=headers)
dados_ibmec = response.json()
lat_ibmec = float(dados_ibmec[0]["lat"])
lon_ibmec = float(dados_ibmec[0]["lon"])
print(lat_ibmec, lon_ibmec)


from math import radians, sin, cos, sqrt, atan2
def calcular_distancia(lat1, lon1, lat2, lon2):
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)