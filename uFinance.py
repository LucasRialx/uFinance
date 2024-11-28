import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "UC0NTB1I4ZRRVL3T"
BASE_URL = "https://www.alphavantage.co/query"

def get_last_close(ticker):
    """Obtém o último preço de fechamento de uma ação usando Alpha Vantage."""
    if not ticker:
        return "Código do ativo não fornecido."

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    # Verificar o status da resposta
    if response.status_code != 200:
        return f"Erro na requisição à API. Status Code: {response.status_code}. Tente novamente mais tarde."

    data = response.json()

    # Logar o conteúdo da resposta para depuração
    print("Resposta da API:", data)

    try:
        if "Time Series (Daily)" not in data:
            # Se a chave "Time Series (Daily)" não estiver na resposta
            if "Error Message" in data:
                return f"Erro na API: {data['Error Message']}"
            return "Erro ao buscar os dados. Verifique o código do ativo."
        
        last_close = list(data["Time Series (Daily)"].values())[0]["4. close"]
        return f"O último preço de fechamento de {ticker.upper()} foi R${float(last_close):.2f}"

    except KeyError:
        return "Erro ao processar os dados retornados. Verifique o código do ativo."

def get_historical_data(ticker, start_date, end_date):
    """Obtém dados históricos de uma ação em um intervalo de tempo."""
    if not ticker or not start_date or not end_date:
        return "Todos os campos são obrigatórios para consultar os dados históricos."

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return f"Erro na requisição à API. Status Code: {response.status_code}. Tente novamente mais tarde."

    data = response.json()

    print("Resposta da API (Histórico):", data)

    try:
        if "Time Series (Daily)" not in data:
            if "Error Message" in data:
                return f"Erro na API: {data['Error Message']}"
            return "Erro ao buscar dados históricos."
        
        time_series = data["Time Series (Daily)"]
        filtered_data = {date: info for date, info in time_series.items() if start_date <= date <= end_date}
        
        if not filtered_data:
            return "Não há dados disponíveis para o intervalo selecionado."
        
        return filtered_data
    except KeyError:
        return "Erro ao buscar dados históricos."

@app.route('/')
def index():
    """Página inicial"""
    return render_template("index.html")

@app.route('/last_close', methods=["POST"])
def last_close():
    """Consulta o último preço de fechamento de uma ação."""
    ticker = request.form.get("ticker")
    result = get_last_close(ticker)
    return render_template("last_close.html", ticker=ticker, result=result)

@app.route('/historical', methods=["POST"])
def historical():
    """Consulta os dados históricos de uma ação em um intervalo de tempo."""
    ticker = request.form.get("ticker")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    result = get_historical_data(ticker, start_date, end_date)
    return render_template("historical_data.html", ticker=ticker, start_date=start_date, end_date=end_date, result=result)

if __name__ == "__main__":
    app.run(debug=True)
