from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_cuurency_rate(base, target): #base = 내가 사용할 환율, target= 내가 변환할 환율
    primary_url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base}.json"
    fallback_url = f"https://latest.currency-api.pages.dev/v1/currencies/{base}.json"
    try:
        response = requests.get(primary_url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception:
        response = requests.get(fallback_url, timeout=5)
        response.raise_for_status()
        data = response.json()
    return data[base][target]

@app.route('/', methods=['GET'])
def index():
    currency_list = [
        ('cny', 'Chinese Yuan'),
        ('usd', 'Dollar'),
        ('jpy', 'Japanese Yen'),
        ('krw', 'Korean Won'),
        ('gbp', 'Pound')
    ]
    return render_template('index.html', currency_list=currency_list)

@app.route('/exchange', methods=['POST'])
def exchange():
    base = request.form['base']
    target = request.form['target']

    currency_list = [
        ('cny', 'Chinese Yuan'),
        ('usd', 'Dollar'),
        ('jpy', 'Japanese Yen'),
        ('krw', 'Korean Won'),
        ('gbp', 'Pound')
    ]
    exchanged_value = fetch_cuurency_rate(base, target)
    return render_template('index.html', exchanged_value=exchanged_value, currency_list=currency_list)

@app.route('/news')
def news():
    pass

if __name__ == '__main__':
    app.run()