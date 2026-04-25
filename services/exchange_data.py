import requests

def get_currency_by_country(country_code):
    return COUNTRY_TO_CURRENCY.get(country_code)

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
    converted = convert_exchange(data, quotes_currency)
    return converted

def convert_exchange(data, new_country_data):
    dates = []
    values = []

    for item in data:
        dates.append(item['date'])
        values.append(item['rate'])

    series_exchange = {
        "label": f"USD/{new_country_data}",
        "unit": f"{new_country_data}",
        "dates": dates, 
        "values": values
    }
    return series_exchange

COUNTRY_TO_CURRENCY = {
    "AF": "AFN",  # Afghanistan
    "AX": "EUR",  # Aland Islands
    "AL": "ALL",  # Albania
    "DZ": "DZD",  # Algeria
    "AS": "USD",  # American Samoa
    "AD": "EUR",  # Andorra
    "AO": "AOA",  # Angola
    "AI": "XCD",  # Anguilla
    "AG": "XCD",  # Antigua and Barbuda
    "AR": "ARS",  # Argentina
    "AM": "AMD",  # Armenia
    "AW": "AWG",  # Aruba
    "AU": "AUD",  # Australia
    "AT": "EUR",  # Austria
    "AZ": "AZN",  # Azerbaijan
    "BS": "BSD",  # Bahamas
    "BH": "BHD",  # Bahrain
    "UM-FQ": "USD",  # Baker Island
    "BD": "BDT",  # Bangladesh
    "BB": "BBD",  # Barbados
    "BY": "BYN",  # Belarus
    "BE": "EUR",  # Belgium
    "BZ": "BZD",  # Belize
    "BJ": "XOF",  # Benin
    "BM": "BMD",  # Bermuda
    "BT": "BTN",  # Bhutan
    "BO": "BOB",  # Bolivia
    "BQ": "USD",  # Bonair, Saint Eustachius and Saba
    "BA": "BAM",  # Bosnia and Herzegovina
    "BW": "BWP",  # Botswana
    "BV": "NOK",  # Bouvet Island
    "BR": "BRL",  # Brazil
    "IO": "USD",  # British Indian Ocean Territory
    "VG": "USD",  # British Virgin Islands
    "BN": "BND",  # Brunei Darussalam
    "BG": "BGN",  # Bulgaria
    "BF": "XOF",  # Burkina Faso
    "BI": "BIF",  # Burundi
    "KH": "KHR",  # Cambodia
    "CM": "XAF",  # Cameroon
    "CA": "CAD",  # Canada
    "CV": "CVE",  # Cape Verde
    "KY": "KYD",  # Cayman Islands
    "CF": "XAF",  # Central African Republic
    "TD": "XAF",  # Chad
    "CL": "CLP",  # Chile
    "CN": "CNY",  # China
    "CX": "AUD",  # Christmas Island
    "CC": "AUD",  # Cocos (Keeling) Islands
    "CO": "COP",  # Colombia
    "KM": "KMF",  # Comoros
    "CK": "NZD",  # Cook Islands
    "CR": "CRC",  # Costa Rica
    "HR": "EUR",  # Croatia
    "CU": "CUP",  # Cuba
    "CW": "ANG",  # Curaçao
    "CY": "EUR",  # Cyprus
    "CZ": "CZK",  # Czechia
    "CI": "XOF",  # Côte d'Ivoire
    "CD": "CDF",  # Democratic Republic of Congo
    "DK": "DKK",  # Denmark
    "DJ": "DJF",  # Djibouti
    "DM": "XCD",  # Dominica
    "DO": "DOP",  # Dominican Republic
    "EC": "USD",  # Ecuador
    "EG": "EGP",  # Egypt
    "SV": "USD",  # El Salvador
    "GQ": "XAF",  # Equatorial Guinea
    "ER": "ERN",  # Eritrea
    "EE": "EUR",  # Estonia
    "ET": "ETB",  # Ethiopia
    "FK": "FKP",  # Falkland Islands
    "FO": "DKK",  # Faroe Islands
    "FM": "USD",  # Federated States of Micronesia
    "FJ": "FJD",  # Fiji
    "FI": "EUR",  # Finland
    "FR": "EUR",  # France
    "GF": "EUR",  # French Guiana
    "PF": "XPF",  # French Polynesia
    "TF": "EUR",  # French Southern and Antarctic Lands
    "GA": "XAF",  # Gabon
    "GM": "GMD",  # Gambia
    "GE": "GEL",  # Georgia
    "DE": "EUR",  # Germany
    "GH": "GHS",  # Ghana
    "GI": "GIP",  # Gibraltar
    "GO": "EUR",  # Glorioso Islands
    "GR": "EUR",  # Greece
    "GL": "DKK",  # Greenland
    "GD": "XCD",  # Grenada
    "GP": "EUR",  # Guadeloupe
    "GU": "USD",  # Guam
    "GT": "GTQ",  # Guatemala
    "GG": "GBP",  # Guernsey
    "GN": "GNF",  # Guinea
    "GW": "XOF",  # Guinea-Bissau
    "GY": "GYD",  # Guyana
    "HT": "HTG",  # Haiti
    "HM": "AUD",  # Heard Island and McDonald Islands
    "HN": "HNL",  # Honduras
    "HK": "HKD",  # Hong Kong
    "UM-HQ": "USD",  # Howland Island
    "HU": "HUF",  # Hungary
    "IS": "ISK",  # Iceland
    "IN": "INR",  # India
    "ID": "IDR",  # Indonesia
    "IR": "IRR",  # Iran
    "IQ": "IQD",  # Iraq
    "IE": "EUR",  # Ireland
    "IM": "GBP",  # Isle of Man
    "IL": "ILS",  # Israel
    "IT": "EUR",  # Italy
    "JM": "JMD",  # Jamaica
    "JP": "JPY",  # Japan
    "UM-DQ": "USD",  # Jarvis Island
    "JE": "GBP",  # Jersey
    "UM-JQ": "USD",  # Johnston Atoll
    "JO": "JOD",  # Jordan
    "JU": "EUR",  # Juan De Nova Island
    "KZ": "KZT",  # Kazakhstan
    "KE": "KES",  # Kenya
    "KI": "AUD",  # Kiribati
    "XK": "EUR",  # Kosovo
    "KW": "KWD",  # Kuwait
    "KG": "KGS",  # Kyrgyzstan
    "LA": "LAK",  # Lao People's Democratic Republic
    "LV": "EUR",  # Latvia
    "LB": "LBP",  # Lebanon
    "LS": "LSL",  # Lesotho
    "LR": "LRD",  # Liberia
    "LY": "LYD",  # Libya
    "LI": "CHF",  # Liechtenstein
    "LT": "EUR",  # Lithuania
    "LU": "EUR",  # Luxembourg
    "MO": "MOP",  # Macau
    "MK": "MKD",  # Macedonia
    "MG": "MGA",  # Madagascar
    "MW": "MWK",  # Malawi
    "MY": "MYR",  # Malaysia
    "MV": "MVR",  # Maldives
    "ML": "XOF",  # Mali
    "MT": "EUR",  # Malta
    "MH": "USD",  # Marshall Islands
    "MQ": "EUR",  # Martinique
    "MR": "MRU",  # Mauritania
    "MU": "MUR",  # Mauritius
    "YT": "EUR",  # Mayotte
    "MX": "MXN",  # Mexico
    "UM-MQ": "USD",  # Midway Islands
    "MD": "MDL",  # Moldova
    "MC": "EUR",  # Monaco
    "MN": "MNT",  # Mongolia
    "ME": "EUR",  # Montenegro
    "MS": "XCD",  # Montserrat
    "MA": "MAD",  # Morocco
    "MZ": "MZN",  # Mozambique
    "MM": "MMK",  # Myanmar
    "NA": "NAD",  # Namibia
    "NR": "AUD",  # Nauru
    "NP": "NPR",  # Nepal
    "NL": "EUR",  # Netherlands
    "NC": "XPF",  # New Caledonia
    "NZ": "NZD",  # New Zealand
    "NI": "NIO",  # Nicaragua
    "NE": "XOF",  # Niger
    "NG": "NGN",  # Nigeria
    "NU": "NZD",  # Niue
    "NF": "AUD",  # Norfolk Island
    "KP": "KPW",  # North Korea
    "MP": "USD",  # Northern Mariana Islands
    "NO": "NOK",  # Norway
    "OM": "OMR",  # Oman
    "PK": "PKR",  # Pakistan
    "PW": "USD",  # Palau
    "PS": "ILS",  # Palestinian Territories
    "PA": "PAB",  # Panama
    "PG": "PGK",  # Papua New Guinea
    "PY": "PYG",  # Paraguay
    "PE": "PEN",  # Peru
    "PH": "PHP",  # Philippines
    "PN": "NZD",  # Pitcairn Islands
    "PL": "PLN",  # Poland
    "PT": "EUR",  # Portugal
    "PR": "USD",  # Puerto Rico
    "QA": "QAR",  # Qatar
    "CG": "XAF",  # Republic of Congo
    "RE": "EUR",  # Reunion
    "RO": "RON",  # Romania
    "RU": "RUB",  # Russia
    "RW": "RWF",  # Rwanda
    "BL": "EUR",  # Saint Barthelemy
    "SH": "SHP",  # Saint Helena
    "KN": "XCD",  # Saint Kitts and Nevis
    "LC": "XCD",  # Saint Lucia
    "MF": "EUR",  # Saint Martin
    "PM": "EUR",  # Saint Pierre and Miquelon
    "VC": "XCD",  # Saint Vincent and the Grenadines
    "WS": "WST",  # Samoa
    "SM": "EUR",  # San Marino
    "ST": "STN",  # Sao Tome and Principe
    "SA": "SAR",  # Saudi Arabia
    "SN": "XOF",  # Senegal
    "RS": "RSD",  # Serbia
    "SC": "SCR",  # Seychelles
    "SL": "SLE",  # Sierra Leone
    "SG": "SGD",  # Singapore
    "SX": "ANG",  # Sint Maarten
    "SK": "EUR",  # Slovakia
    "SI": "EUR",  # Slovenia
    "SB": "SBD",  # Solomon Islands
    "SO": "SOS",  # Somalia
    "ZA": "ZAR",  # South Africa
    "GS": "FKP",  # South Georgia and South Sandwich Islands
    "KR": "KRW",  # South Korea
    "SS": "SSP",  # South Sudan
    "ES": "EUR",  # Spain
    "LK": "LKR",  # Sri Lanka
    "SD": "SDG",  # Sudan
    "SR": "SRD",  # Suriname
    "SJ": "NOK",  # Svalbard and Jan Mayen
    "SE": "SEK",  # Sweden
    "CH": "CHF",  # Switzerland
    "SY": "SYP",  # Syria
    "TW": "TWD",  # Taiwan
    "TJ": "TJS",  # Tajikistan
    "TZ": "TZS",  # Tanzania
    "TH": "THB",  # Thailand
    "TL": "USD",  # Timor-Leste
    "TG": "XOF",  # Togo
    "TK": "NZD",  # Tokelau
    "TO": "TOP",  # Tonga
    "TT": "TTD",  # Trinidad and Tobago
    "TN": "TND",  # Tunisia
    "TR": "TRY",  # Turkey
    "TM": "TMT",  # Turkmenistan
    "TC": "USD",  # Turks and Caicos Islands
    "TV": "AUD",  # Tuvalu
    "VI": "USD",  # US Virgin Islands
    "UG": "UGX",  # Uganda
    "UA": "UAH",  # Ukraine
    "AE": "AED",  # United Arab Emirates
    "GB": "GBP",  # United Kingdom
    "US": "USD",  # United States
    "UY": "UYU",  # Uruguay
    "UZ": "UZS",  # Uzbekistan
    "VU": "VUV",  # Vanuatu
    "VA": "EUR",  # Vatican City
    "VE": "VES",  # Venezuela
    "VN": "VND",  # Vietnam
    "UM-WQ": "USD",  # Wake Island
    "WF": "XPF",  # Wallis and Futuna
    "EH": "MAD",  # Western Sahara
    "YE": "YER",  # Yemen
    "ZM": "ZMW",  # Zambia
    "ZW": "ZWL",  # Zimbabwe
    "SZ": "SZL",  # eSwatini
}