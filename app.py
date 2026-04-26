from flask import Flask, render_template, jsonify
from flask_caching import Cache
from services.risk_score import risk_calculate
from services.exchange_data import get_currency_by_country, fetch_exchange_series
from services.common_data import final_data
from services.equity import equity_data
from services.consumer_price import get_cosumer_price
from services.bond_yield import get_bond_yield
from services.ai_explainer import generate_explanation
from datetime import date, timedelta

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 120})

@cache.memoize(timeout=180) 
def get_market_data(country_code):
    new_country_code = get_currency_by_country(country_code)
    today = date.today()
    last_month = today - timedelta(days=30)
    year = today - timedelta(days=365)
    
    if not new_country_code:
        return None, None, None

    if new_country_code == "USD":
        # 프런트에서 버튼 이름이 dollar index라고 나오게 바꾸기 
        exchange_rate = final_data("DX-Y.NYB", "Dollar Index (DXY)", "index")
    else:
        exchange_rate = fetch_exchange_series("USD", new_country_code, last_month, today)

    equity_index = equity_data(country_code, "Equity index" ,last_month, today)
    consumer_price = get_cosumer_price(country_code, "Consumer Price Index" ,year)
    bond_yield = get_bond_yield(country_code, "10-Year Government Bond Yield", year)
    series = {
        "exchange_rate": exchange_rate,
        'equity_index': equity_index,
        'consumer_price': consumer_price,
        'bond_yield': bond_yield,
    }
    
    # risk = risk_calculate(series)
    risk = {"risk_level": "None"}
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

@app.route('/api/global/global_indicators')
@cache.memoize(timeout=300) 
def global_indicator():
    oil_price = final_data("CL=F", "WTI Crude", "USD/bbl")
    dollar_index = final_data("DX-Y.NYB", "Dollar Index (DXY)", "index")
    vix = final_data("^VIX", "CBOE Volatility Index (VIX)", "index")

    series = {
        "oil_price": oil_price,
        "dollar_index": dollar_index,
        "vix": vix
    }

    return jsonify(series)

if __name__ == '__main__':
    app.run()