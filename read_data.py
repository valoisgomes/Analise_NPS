"""
Este código baixa um arquivo CSV de feedbacks do Google Drive e carrega os dados em um DataFrame pandas.

O arquivo é identificado por um ID único ('file_id'), que é extraído da URL do arquivo no Google Drive.
A URL do arquivo no Google Drive tem o seguinte formato:
https://drive.google.com/file/d/FILE_ID/view?usp=sharing

"""

import gdown
import pandas as pd

file_id = '1-JOR_8rtkQVnsSYQtL3WllK-KeaAIsek'
gdown.download(f'https://drive.google.com/uc?id={file_id}', 'data_lake_igreja.csv')

dados = pd.read_csv('data_lake_igreja.csv', delimiter=';')