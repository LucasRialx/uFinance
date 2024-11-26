from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

def get_last_close(ticker):
    """Obtém o último preço de fechamento de uma ação."""
    stock = yf.Ticker(ticker)
    try:
        last_close = stock.history(period="1d")["Close"][-1]
        return f"O último preço de fechamento de {ticker.upper()} foi R${last_close:.2f}"
    except IndexError:
        return "Erro ao buscar os dados. Verifique o código do ativo."

def get_historical_data(ticker, period, interval):
    """Obtém dados históricos de uma ação."""
    stock = yf.Ticker(ticker)
    try:
        data = stock.history(period=period, interval=interval)
        return data
    except Exception as e:
        return f"Erro ao buscar dados históricos: {e}"

def get_global_indices():
    """Obtém informações das principais bolsas do mundo."""
    indices = {
        "Ibovespa": "^BVSP",
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "Dow Jones": "^DJI",
        "FTSE 100": "^FTSE",
        "DAX (Alemanha)": "^GDAXI",
        "Nikkei 225 (Japão)": "^N225",
    }
    result = {}
    for name, ticker in indices.items():
        index = yf.Ticker(ticker)
        last_close = index.history(period="1d")["Close"][-1]
        result[name] = last_close
    return result

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
    """Consulta dados históricos de uma ação."""
    ticker = request.form.get("ticker")
    period = request.form.get("period")
    interval = request.form.get("interval")
    data = get_historical_data(ticker, period, interval)
    return render_template("historical.html", ticker=ticker, data=data)

@app.route('/global_indices')
def global_indices():
    """Exibe os dados das principais bolsas."""
    indices = get_global_indices()
    return render_template("global_indices.html", indices=indices)

if __name__ == "__main__":
    app.run(debug=True)
