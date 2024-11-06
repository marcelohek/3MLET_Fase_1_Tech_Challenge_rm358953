# API para scraping do site da Embrapa 

Este é um projeto de API desenvolvido com Flask, que inclui web scraping e autenticação básica.

## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Web Scraping**: Extrai dados das tabelas das páginas web do site da Embrapa (http://vitibrasil.cnpuv.embrapa.br/) usando BeautifulSoup.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.

## 📁 Estrutura do Projeto

```bash
intro_api/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── scrape_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── scraping_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   └── config.py
├── requirements.txt
├── README.md
└── run.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`routes/`**: Contém as rotas organizadas por funcionalidades.
  - **`services/`**: Serviços para lógica de negócios, como scraping.
  - **`utils/`**: Utilitários, como autenticação.
  - **`config.py`**: Configurações da aplicação Flask.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Documentação do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/marcelohek/3MLET_Fase_1_Tech_Challenge_rm358953.git
cd 3MLET_Fase_1_Tech_Challenge_rm358953
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000`.


## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.
