from flask import Flask, render_template, jsonify
from services.risk_score import risk_calculate
from services.exchange_data import get_currency_by_country, fetch_exchange_series
from services.common_data import final_data
from datetime import date, timedelta


app = Flask(__name__)

DUMMY_COUNTRY_DATA = {
    "US": {
        "explain": {
            "title": "Why is the U.S. risk level medium?",
            "summary": "The U.S. shows a medium risk profile because the dollar is strengthening, oil prices are rising, and market volatility has also moved up.",
            "bullets": [
                "A stronger dollar can pressure global liquidity and emerging market assets.",
                "Higher oil prices may raise inflation concerns.",
                "The recent rise in VIX suggests investors are becoming more cautious."
            ]
        }
    }
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/country/<country_code>/series')
def country_series(country_code):
    new_country_code = get_currency_by_country(country_code)
    if (new_country_code == "USD"):
        dollar_index = final_data("DX-Y.NYB", "Dollar Index (DXY)", "index")
        # 지금은 dollar index로 설정했지만 나중에는 US만 환율 그래프를 안보이게 하던지 할지 생각하기 
        exchange_rate = dollar_index
    else:
        today = date.today()
        
        last_week = today - timedelta(days=7)
        exchange_rate = fetch_exchange_series("USD", new_country_code, last_week, today)

    oil_price = final_data("CL=F", "WTI Crude", "USD/bbl")
    dollar_index = final_data("DX-Y.NYB", "Dollar Index (DXY)", "index")
    vix = final_data("^VIX", "CBOE Volatility Index (VIX)", "index")

    series = {
        "exchange_rate": exchange_rate,
        "oil_price": oil_price,
        "dollar_index": dollar_index,
        "vix": vix
    }
    # risk 계산 로직을 pandas를 활용해서 계산으로 바꾸기 
    # risk = {"risk_level": "Unknown"}
    risk = risk_calculate(series)

    return jsonify(series=series, risk=risk) 
    ...

@app.route('/api/country/<country_code>/explain')
def country_explain(country_code):
    ai_explanation= DUMMY_COUNTRY_DATA[country_code]['explain']
    return jsonify(ai_explanation)
    ...

if __name__ == '__main__':
    app.run()