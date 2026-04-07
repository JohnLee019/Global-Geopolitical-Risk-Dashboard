from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# def fetch_currency_rate(base, target): #base = 내가 사용할 환율, target= 내가 변환할 환율
#     primary_url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base}.json"
#     fallback_url = f"https://latest.currency-api.pages.dev/v1/currencies/{base}.json"
#     try:
#         response = requests.get(primary_url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#     except Exception:
#         response = requests.get(fallback_url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#     return data[base][target]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/country/<country_code>')
def country_summary(country_code):
    ...

@app.route('/api/country/<country_code>/series')
def country_series(country_code):
    ...

@app.route('/api/country/<country_code>/explain')
def country_explain(country_code):
    ...

if __name__ == '__main__':
    app.run()