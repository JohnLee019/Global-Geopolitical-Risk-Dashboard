from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests

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

# @app.route('/api/country/<country_code>')
# def country_summary(country_code):
#     country_data = DUMMY_COUNTRY_DATA[country_code]
#     return jsonify(country_data)
#     ...

@app.route('/api/country/<country_code>/series')
def country_series(country_code):
    country_data= DUMMY_COUNTRY_DATA[country_code]['series']
    return jsonify(country_data)
    ...

@app.route('/api/country/<country_code>/explain')
def country_explain(country_code):
    ai_explanation= DUMMY_COUNTRY_DATA[country_code]['explain']
    return jsonify(ai_explanation)
    ...

if __name__ == '__main__':
    app.run()