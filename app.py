from flask import Flask, render_template, jsonify
from services.risk_score import risk_calculate
from services.exchange_data import get_currency_by_country, fetch_exchange_series
from datetime import date, timedelta

app = Flask(__name__)

DUMMY_COUNTRY_DATA = {
    "US": {
        "summary": {
            "country_code": "US",
            "country_name": "United States",
            "risk_level": "Medium",
            "risk_score": 58,
            "risk_color": "#f4b400",
            "headline": "Dollar strength and volatility remain elevated.",
            "indicators": {
                "exchange_rate": {
                    "label": "USD/KRW",
                    "current": 1468.2,
                    "change": 12.4,
                    "change_pct": 0.85,
                    "unit": "KRW"
                },
                "oil_price": {
                    "label": "WTI",
                    "current": 82.6,
                    "change": 1.8,
                    "change_pct": 2.23,
                    "unit": "USD/bbl"
                },
                "dollar_index": {
                    "label": "DXY",
                    "current": 105.3,
                    "change": 0.7,
                    "change_pct": 0.67,
                    "unit": "index"
                },
                "vix": {
                    "label": "VIX",
                    "current": 19.8,
                    "change": 2.1,
                    "change_pct": 11.86,
                    "unit": "index"
                }
            }
        },

        "series": {
            "exchange_rate": {
                "label": "USD/KRW",
                "unit": "KRW",
                "dates": [
                    "04-01", "04-02", "04-03",
                    "04-04", "04-05", "04-06", "04-07"
                ],
                "values": [1452.3, 1456.8, 1459.1, 1461.0, 1463.4, 1465.7, 1468.2]
            },
            "oil_price": {
                "label": "WTI Crude",
                "unit": "USD/bbl",
                "dates": [
                    "04-01", "04-02", "04-03",
                    "04-04", "04-05", "04-06", "04-07"
                ],
                "values": [79.2, 79.8, 80.4, 81.1, 81.9, 82.1, 82.6]
            },
            "dollar_index": {
                "label": "Dollar Index (DXY)",
                "unit": "index",
                "dates": [
                    "04-01", "04-02", "04-03",
                    "04-04", "04-05", "04-06", "04-07"
                ],
                "values": [103.9, 104.1, 104.4, 104.6, 104.9, 105.1, 105.3]
            },
            "vix": {
                "label": "CBOE Volatility Index",
                "unit": "index",
                "dates": [
                    "04-01", "04-02", "04-03",
                    "04-04", "04-05", "04-06", "04-07"
                ],
                "values": [15.4, 15.9, 16.8, 17.2, 18.1, 19.0, 19.8]
            }
        },

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
        # 나중에 dollar index api 연결시킨 후에 밑에 exchange_rate = dollar index 형식으로 바꾸기 
        exchange_rate = None
    else:
        today = date.today()
        
        last_week = today - timedelta(days=7)
        exchange_rate = fetch_exchange_series("USD", new_country_code, last_week, today)
    # risk = risk_calculate(country_data)
    # risk 계산 로직을 pandas를 활용해서 계산으로 바꾸기 
    risk = {"risk_level": "Unknown"}

    series = {
        "exchange_rate": exchange_rate,
        "oil_price": None,
        "dollar_index": None,
        "vix": None
    }
    return jsonify(series=series, risk=risk) 
    ...

@app.route('/api/country/<country_code>/explain')
def country_explain(country_code):
    ai_explanation= DUMMY_COUNTRY_DATA[country_code]['explain']
    return jsonify(ai_explanation)
    ...

if __name__ == '__main__':
    app.run()