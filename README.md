![image](https://github.com/user-attachments/assets/5d733da0-d62b-4368-bf5f-c48e3f992bb8)

# uFinance com AlphaVantage

Este é um aplicativo web simples desenvolvido em Python usando Flask. O aplicativo permite consultar o último preço de fechamento de uma ação e obter dados históricos usando a API Alpha Vantage.

## Funcionalidades

- Consultar o **último preço de fechamento** de uma ação.
- Consultar **dados históricos** de uma ação em um intervalo de datas.

## Pré-requisitos

- Python 3.8 ou superior
- Conta na [Alpha Vantage](https://www.alphavantage.co/) para obter uma chave de API.

## Configuração

1. **Clone o repositório**:
   ```
   git clone https://github.com/LucasRialx/uFinance
   cd uFinance
  
Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Instale as dependências:

```
pip install -r requirements.txt
```

Configure a chave da API: Substitua a variável API_KEY no arquivo app.py pela sua chave da Alpha Vantage:
```
API_KEY = "SUA_CHAVE_AQUI"
Executando o Projeto
```
Inicie o servidor:
```
python app.py
```
Acesse no navegador:

http://127.0.0.1:5000

Estrutura do Projeto
Copiar código
├── templates/
│   ├── index.html
│   ├── last_close.html
│   ├── historical_data.html
├── app.py
├── requirements.txt
└── README.md

##Exemplo de Uso

Último preço de fechamento: Insira o código da ação (ex.: AAPL) e veja o preço mais recente.
Dados históricos: Insira o código da ação e o intervalo de datas para obter os preços históricos.

##Tecnologias Utilizadas

Python 3
Flask
Requests

##Licença
Este projeto está sob a licença MIT.
