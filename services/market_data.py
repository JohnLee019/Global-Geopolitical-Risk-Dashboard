import requests

COUNTRY_TO_CURRENCY = {
    "US": "USD",  # United States
    "KR": "KRW",  # South Korea
    "JP": "JPY",  # Japan
    "CN": "CNY",  # China
    "GB": "GBP",  # United Kingdom
    "DE": "EUR",  # Germany
    "FR": "EUR",  # France
    "IT": "EUR",  # Italy
    "ES": "EUR",  # Spain
    "NL": "EUR",  # Netherlands
    "BE": "EUR",  # Belgium
    "CH": "CHF",  # Switzerland
    "CA": "CAD",  # Canada
    "AU": "AUD",  # Australia
    "NZ": "NZD",  # New Zealand
    "IN": "INR",  # India
    "BR": "BRL",  # Brazil
    "MX": "MXN",  # Mexico
    "RU": "RUB",  # Russia
    "TR": "TRY",  # Turkey
    "SA": "SAR",  # Saudi Arabia
    "AE": "AED",  # UAE
    "SG": "SGD",  # Singapore
    "HK": "HKD",  # Hong Kong
    "TW": "TWD",  # Taiwan
    "ID": "IDR",  # Indonesia
    "TH": "THB",  # Thailand
    "MY": "MYR",  # Malaysia
    "VN": "VND",  # Vietnam
    "ZA": "ZAR",  # South Africa
}

def normalize_country_code(country_code):
    return (country_code or "").strip().upper()


def get_currency_by_country(country_code):
    code = normalize_country_code(country_code)
    return COUNTRY_TO_CURRENCY.get(code)

def fetch_exchange_series(base_currency, quotes_currency, start, end):
    base_url = "https://api.frankfurter.dev/v2/rates"
    params = {
        "base": base_currency,
        "quotes": quotes_currency,
        "from": start,
        "to": end
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data