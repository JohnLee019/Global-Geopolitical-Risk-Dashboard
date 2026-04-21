from flask import Flask, render_template, jsonify
from flask_caching import Cache
from services.risk_score import risk_calculate
from services.exchange_data import get_currency_by_country, fetch_exchange_series
from services.common_data import final_data
from services.ai_explainer import generate_explanation
from datetime import date, timedelta

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 120})

@cache.memoize(timeout=120) 
def get_market_data(country_code):
    country_code = country_code.strip().upper()
    new_country_code = get_currency_by_country(country_code)
    
    if not new_country_code:
        return None, None, None

    oil_price = final_data("CL=F", "WTI Crude", "USD/bbl")
    dollar_index = final_data("DX-Y.NYB", "Dollar Index (DXY)", "index")
    vix = final_data("^VIX", "CBOE Volatility Index (VIX)", "index")

    if new_country_code == "USD":
        exchange_rate = dollar_index
    else:
        today = date.today()
        last_week = today - timedelta(days=30)
        exchange_rate = fetch_exchange_series("USD", new_country_code, last_week, today)

    series = {
        "exchange_rate": exchange_rate,
        "oil_price": oil_price,
        "dollar_index": dollar_index,
        "vix": vix
    }
    
    risk = risk_calculate(series)
    return series, risk, new_country_code

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/country/<country_code>/series')
def country_series(country_code):
    series, risk, country_name = get_market_data(country_code)
    if not series:
        return jsonify({"error": "Unsupported country code"}), 400
    
    return jsonify(series=series, risk=risk) 

@app.route('/api/country/<country_code>/explain')
def country_explain(country_code):
    series, risk, country_name = get_market_data(country_code)
    if not series:
        return jsonify({"error": "Unsupported country code"}), 400
    
    ai_explanation = generate_explanation(country_name=country_name, risk_score=risk.get("risk_score"), metrics=series)

    return jsonify(ai_explanation)

if __name__ == '__main__':
    app.run()