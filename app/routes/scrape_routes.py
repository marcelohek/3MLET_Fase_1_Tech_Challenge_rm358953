from flask import request, jsonify
from app import app, auth
from app.services.scraping_service import  get_table_data


@app.route('/scrape/table/02_producao', methods=['GET'])
@auth.login_required
def scrape_table_producao():
    """
    Extrai os dados da tabela Produção de vinhos, sucos e derivados. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Produto:
              type: string
              description: Produto.
            Quantidade (L.):
              type: string
              description: Quantidade (L.).
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_02'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/03_01_processamento_viniferas', methods=['GET'])
@auth.login_required
def scrape_table_processamento_viniferas():
    """
    Extrai os dados da tabela Uvas viníferas processadas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Cultivar:
              type: string
              description: Cultivar.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_03',
        'subopcao': 'subopt_01'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/03_02_processamento_americanas_e_hibridas', methods=['GET'])
@auth.login_required
def scrape_table_processamento_americanas_e_hibridas():
    """
    Extrai os dados da tabela Uvas americanas e híbridas processadas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Cultivar:
              type: string
              description: Cultivar.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_03',
        'subopcao': 'subopt_02'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/03_03_processamento_uvas_de_mesa', methods=['GET'])
@auth.login_required
def scrape_table_processamento_uvas_de_mesa():
    """
    Extrai os dados da tabela Uvas de mesa processadas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Cultivar:
              type: string
              description: Cultivar.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_03',
        'subopcao': 'subopt_03'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/03_04_processamento_sem_classificacao', methods=['GET'])
@auth.login_required
def scrape_table_processamento_sem_classificacao():
    """
    Extrai os dados da tabela Uvas sem classificação processadas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Sem definição:
              type: string
              description: Sem definição.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_03',
        'subopcao': 'subopt_04'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)



@app.route('/scrape/table/04_comercializacao', methods=['GET'])
@auth.login_required
def scrape_table_comercializacao():
    """
    Extrai os dados da tabela Comercialização de vinhos e derivados. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Produto:
              type: string
              description: Produto.
            Quantidade (L.):
              type: string
              description: Quantidade (L.).
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_04',
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)



@app.route('/scrape/table/05_01_importacao_vinhos_de_mesa', methods=['GET'])
@auth.login_required
def scrape_table_importacao_vinhos_de_mesa():
    """
    Extrai os dados da tabela Importação de vinhos de mesa. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_05',
        'subopcao': 'subopt_01'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/05_02_importacao_espumantes', methods=['GET'])
@auth.login_required
def scrape_table_importacao_espumantes():
    """
    Extrai os dados da tabela Importação de espumantes. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_05',
        'subopcao': 'subopt_02'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/05_03_importacao_uvas_frescas', methods=['GET'])
@auth.login_required
def scrape_table_importacao_uvas_frescas():
    """
    Extrai os dados da tabela Importação de uvas frescas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_05',
        'subopcao': 'subopt_03'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)


@app.route('/scrape/table/05_04_importacao_uvas_passas', methods=['GET'])
@auth.login_required
def scrape_table_importacao_uvas_passas():
    """
    Extrai os dados da tabela Importação de uvas passas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_05',
        'subopcao': 'subopt_04'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/05_05_importacao_suco_de_uva', methods=['GET'])
@auth.login_required
def scrape_table_importacao_suco_de_uva():
    """
    Extrai os dados da tabela Importação de suco de uva. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_05',
        'subopcao': 'subopt_05'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)


@app.route('/scrape/table/06_01_exportacao_vinhos_de_mesa', methods=['GET'])
@auth.login_required
def scrape_table_exportacao_vinhos_de_mesa():
    """
    Extrai os dados da tabela Exportação de vinhos de mesa. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_06',
        'subopcao': 'subopt_01'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/06_02_exportacao_espumantes', methods=['GET'])
@auth.login_required
def scrape_table_exportacao_espumantes():
    """
    Extrai os dados da tabela Exportação de espumantes. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_06',
        'subopcao': 'subopt_02'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/06_03_exportacao_uvas_frescas', methods=['GET'])
@auth.login_required
def scrape_table_exportacao_uvas_frescas():
    """
    Extrai os dados da tabela Exportação de uvas frescas. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_06',
        'subopcao': 'subopt_03'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)

@app.route('/scrape/table/06_04_exportacao_suco_de_uva', methods=['GET'])
@auth.login_required
def scrape_table_exportacao_suco_de_uva():
    """
    Extrai os dados da tabela Exportação de vinhos de mesa. Caso não seja informado o parâmetro ano, será consultado o ano de 2023.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: ano
        in: query
        type: int
        required: false
    responses:
      200:
        description: Conteúdo da tabela.
        schema:
          type: object
          properties:
            Países:
              type: string
              description: País.
            Quantidade (Kg):
              type: string
              description: Quantidade (Kg).
            Valor (US$):
              type: string
              description: Valor (US$).            
      400:
        description: Erro de requisição. O Parâmetro ano deve estar entre 1970 e 2023.
      401:
        description: Não autorizado.
    """

    url='http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        'opcao': 'opt_06',
        'subopcao': 'subopt_04'
    }

    # Verifica se o parâmetro 'ano' foi enviado na requisição
    ano = request.args.get('ano')
    if ano:
        params['ano'] = ano  # Adiciona 'ano' ao dicionário de parâmetros se ele existir

    return get_table_data(url,params)