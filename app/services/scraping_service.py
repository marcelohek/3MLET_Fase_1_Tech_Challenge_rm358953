import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import jsonify
    
    
def get_table_data(url, params):
    try:

        ano = params.get('ano')
        # Caso o parâmetro ano seja menor que 1970 ou maior que 2023
        if ano and (int(ano) < 1970 or int(ano) > 2023):
            return jsonify({"error":'Parâmetro ano deve estar entre 1970 e 2023.'}), 400

        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra a tabela "tb_base tb_dados"
        tabela = soup.find('table', {'class': 'tb_base tb_dados'})

        # Extrai os nomes das colunas
        table_headers = [th.get_text(strip=True) for th in tabela.find_all('th')]
        print(table_headers)

        # Extrai as linhas da tabela
        table_rows = tabela.find_all('tr')

        # Extrai os dados de cada linha e armazenar em uma lista
        data = []
        for row in table_rows[1:]:  # Ignorar a primeira linha de cabeçalho
            cols = row.find_all('td')
            cols = [col.get_text(strip=True) for col in cols]
            data.append(cols)

        # Cria o DataFrame usando os nomes das colunas e os dados extraídos
        df = pd.DataFrame(data, columns=table_headers)

        # Converte o DataFrame para um dicionário de lista e retorna como JSON
        data = df.to_dict(orient="records")
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    