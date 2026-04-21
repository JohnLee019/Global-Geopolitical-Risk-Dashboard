import yfinance as yf

def final_data(ticker_data, label, unit):
    dates, values = fetch_series(ticker_data)
    series = {
        "label": label,
        "unit": unit,
        "dates": dates,
        "values": values
    }
    return series

def fetch_series(ticker_label):
    ticker = yf.Ticker(ticker_label)
    historical_data = ticker.history(period="1mo") 

    dates = []
    values = []

    if historical_data.empty:
        return None
    
    for date, row in historical_data.iterrows():
        dates.append(date.strftime("%Y-%m-%d"))
        values.append(round(row["Close"], 2))

    return dates, values