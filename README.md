# Golden Raspberry API

Esta API permite a leitura da lista de indicados e vencedores da categoria 'Pior Filme' do Golden Raspberry Awards.
A API lê a lista de indicados de uma fonte de dados CSV, armazenar os dados na memória e fornecer dados do produtores com o maior e menor intervalo entre duas premiações.

## Tecnologias Utilizadas
- Python 3
- Flask
- SQLite (banco de dados em memória)
- SQLAlchemy (ORM para manipulação do banco de dados)

## Estrutura do Projeto
```
/golden_raspberry_api
│── /app
│   │── __init__.py         # Inicializa o Flask app
│   │── database.py         # Configuração do banco de dados
│   │── models.py           # Definição dos modelos ORM
│   │── routes.py           # Endpoints da API
│   │── services.py         # Lógica de negócios
│   │── utils.py            # Função para carregar CSV
│
│── /tests
│   │── test_integration.py # Testes de integração
│   │── test_services.py 	# Testes de unitário
│
│── Movielist.csv           # Arquivo CSV com os dados
│── main.py                 # Entrada principal da aplicação
│── README.md               # Documentação do projeto
│── requirements.txt        # Dependências do projeto (se necessário)
```

## Configuração e Execução
### 1. Clonar o repositório
```
git clone https://github.com/josueccim/golden_raspberry_api
cd golden_raspberry_api
```

### 2. Criar um ambiente virtual e ativá-lo
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar as dependências
```
pip install -r requirements.txt
```

### 4. Executar a API
```
python main.py
```
A API estará disponível em `http://127.0.0.1:5000`

## Endpoints
### 1. Obter o produtor com maior e menor intervalo entre prêmios consecutivos
**GET /producers/max-min-interval**

**Resposta de Exemplo:**
```json
{
    "max": {
        "producer": "Produtor X",
        "interval": 10,
        "previousWin": 2000,
        "followingWin": 2010
    },
    "min": {
        "producer": "Produtor Y",
        "interval": 1,
        "previousWin": 2018,
        "followingWin": 2019
    }
}
```

## Testes de Integração
Para rodar os testes:
```
pytest tests/test_integration.py
```

## Licença
MIT License

