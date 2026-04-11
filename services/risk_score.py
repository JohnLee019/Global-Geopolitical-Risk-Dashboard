def risk_calculate(data):
    exchange = data['series']['exchange_rate']['values']
    oil = data['series']['oil_price']['values']
    dollar = data['series']['dollar_index']['values']
    vix = data['series']['vix']['values']
    return