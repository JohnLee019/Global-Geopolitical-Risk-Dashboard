from fredapi import Fred
import os
from dotenv import load_dotenv

load_dotenv()
FRED_API_KEY = os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)
def get_cosumer_price(country_code, label, start_date):
    series_id = COUNTRY_TO_INTEREST_RATE.get(country_code)
    
    if not series_id:
        return None, None
        
    try:
        data = fred.get_series(series_id, observation_start=start_date)
        
        if data.empty:
            return None, None
            
        data = data.dropna()
        
        dates = []
        values = []
        for date, value in data.items():
            dates.append(date.strftime("%Y-%m-%d"))
            values.append(round(value, 2))
        
        series = {
        "label": label,
        "unit": "CPI",
        "dates": dates,
        "values": values
        }

        return series
        
    except Exception as e:
        print(f"FRED API 호출 에러: {e}")
        return None, None
    
# 기준금리 (Interest Rate) FRED 시리즈 ID 매핑
# 주요국은 단기/기준금리 시리즈 ID를 매핑, 지원하지 않는 국가는 None으로 처리
COUNTRY_TO_INTEREST_RATE = {
    "AF": None,           # Afghanistan
    "AX": None,           # Aland Islands
    "AL": None,           # Albania
    "DZ": None,           # Algeria
    "AS": None,           # American Samoa
    "AD": None,           # Andorra
    "AO": None,           # Angola
    "AI": None,           # Anguilla
    "AG": None,           # Antigua and Barbuda
    "AR": "INTDSRARM193N",# Argentina
    "AM": None,           # Armenia
    "AW": None,           # Aruba
    "AU": "INTDSRAUM193N",# Australia
    "AT": "ECBDFR",       # Austria (Eurozone)
    "AZ": None,           # Azerbaijan
    "BS": None,           # Bahamas
    "BH": None,           # Bahrain
    "UM-FQ": None,        # Baker Island
    "BD": None,           # Bangladesh
    "BB": None,           # Barbados
    "BY": None,           # Belarus
    "BE": "ECBDFR",       # Belgium (Eurozone)
    "BZ": None,           # Belize
    "BJ": None,           # Benin
    "BM": None,           # Bermuda
    "BT": None,           # Bhutan
    "BO": None,           # Bolivia
    "BQ": None,           # Bonair, Saint Eustachius and Saba
    "BA": None,           # Bosnia and Herzegovina
    "BW": None,           # Botswana
    "BV": None,           # Bouvet Island
    "BR": "INTDSRBRM193N",# Brazil
    "IO": None,           # British Indian Ocean Territory
    "VG": None,           # British Virgin Islands
    "BN": None,           # Brunei Darussalam
    "BG": None,           # Bulgaria
    "BF": None,           # Burkina Faso
    "BI": None,           # Burundi
    "KH": None,           # Cambodia
    "CM": None,           # Cameroon
    "CA": "INTDSRCAM193N",# Canada
    "CV": None,           # Cape Verde
    "KY": None,           # Cayman Islands
    "CF": None,           # Central African Republic
    "TD": None,           # Chad
    "CL": "INTDSRCLM193N",# Chile
    "CN": "INTDSRCNM193N",# China
    "CX": None,           # Christmas Island
    "CC": None,           # Cocos (Keeling) Islands
    "CO": "INTDSRCOM193N",# Colombia
    "KM": None,           # Comoros
    "CK": None,           # Cook Islands
    "CR": None,           # Costa Rica
    "HR": None,           # Croatia
    "CU": None,           # Cuba
    "CW": None,           # Curaçao
    "CY": "ECBDFR",       # Cyprus (Eurozone)
    "CZ": "INTDSRCZM193N",# Czechia
    "CI": None,           # Côte d'Ivoire
    "CD": None,           # Democratic Republic of Congo
    "DK": "INTDSRDKM193N",# Denmark
    "DJ": None,           # Djibouti
    "DM": None,           # Dominica
    "DO": None,           # Dominican Republic
    "EC": None,           # Ecuador
    "EG": None,           # Egypt
    "SV": None,           # El Salvador
    "GQ": None,           # Equatorial Guinea
    "ER": None,           # Eritrea
    "EE": "ECBDFR",       # Estonia (Eurozone)
    "ET": None,           # Ethiopia
    "FK": None,           # Falkland Islands
    "FO": None,           # Faroe Islands
    "FM": None,           # Federated States of Micronesia
    "FJ": None,           # Fiji
    "FI": "ECBDFR",       # Finland (Eurozone)
    "FR": "ECBDFR",       # France (Eurozone)
    "GF": None,           # French Guiana
    "PF": None,           # French Polynesia
    "TF": None,           # French Southern and Antarctic Lands
    "GA": None,           # Gabon
    "GM": None,           # Gambia
    "GE": None,           # Georgia
    "DE": "ECBDFR",       # Germany (Eurozone)
    "GH": None,           # Ghana
    "GI": None,           # Gibraltar
    "GO": None,           # Glorioso Islands
    "GR": "ECBDFR",       # Greece (Eurozone)
    "GL": None,           # Greenland
    "GD": None,           # Grenada
    "GP": None,           # Guadeloupe
    "GU": None,           # Guam
    "GT": None,           # Guatemala
    "GG": None,           # Guernsey
    "GN": None,           # Guinea
    "GW": None,           # Guinea-Bissau
    "GY": None,           # Guyana
    "HT": None,           # Haiti
    "HM": None,           # Heard Island and McDonald Islands
    "HN": None,           # Honduras
    "HK": None,           # Hong Kong
    "UM-HQ": None,        # Howland Island
    "HU": "INTDSRHUM193N",# Hungary
    "IS": None,           # Iceland
    "IN": "INTDSRINM193N",# India
    "ID": "INTDSRIDM193N",# Indonesia
    "IR": None,           # Iran
    "IQ": None,           # Iraq
    "IE": "ECBDFR",       # Ireland (Eurozone)
    "IM": None,           # Isle of Man
    "IL": "INTDSRILM193N",# Israel
    "IT": "ECBDFR",       # Italy (Eurozone)
    "JM": None,           # Jamaica
    "JP": "INTDSRJPM193N",# Japan
    "UM-DQ": None,        # Jarvis Island
    "JE": None,           # Jersey
    "UM-JQ": None,        # Johnston Atoll
    "JO": None,           # Jordan
    "JU": None,           # Juan De Nova Island
    "KZ": None,           # Kazakhstan
    "KE": None,           # Kenya
    "KI": None,           # Kiribati
    "XK": None,           # Kosovo
    "KW": None,           # Kuwait
    "KG": None,           # Kyrgyzstan
    "LA": None,           # Lao People's Democratic Republic
    "LV": "ECBDFR",       # Latvia (Eurozone)
    "LB": None,           # Lebanon
    "LS": None,           # Lesotho
    "LR": None,           # Liberia
    "LY": None,           # Libya
    "LI": None,           # Liechtenstein
    "LT": "ECBDFR",       # Lithuania (Eurozone)
    "LU": "ECBDFR",       # Luxembourg (Eurozone)
    "MO": None,           # Macau
    "MK": None,           # Macedonia
    "MG": None,           # Madagascar
    "MW": None,           # Malawi
    "MY": "INTDSRMYM193N",# Malaysia
    "MV": None,           # Maldives
    "ML": None,           # Mali
    "MT": "ECBDFR",       # Malta (Eurozone)
    "MH": None,           # Marshall Islands
    "MQ": None,           # Martinique
    "MR": None,           # Mauritania
    "MU": None,           # Mauritius
    "YT": None,           # Mayotte
    "MX": "INTDSRMXM193N",# Mexico
    "UM-MQ": None,        # Midway Islands
    "MD": None,           # Moldova
    "MC": None,           # Monaco
    "MN": None,           # Mongolia
    "ME": None,           # Montenegro
    "MS": None,           # Montserrat
    "MA": None,           # Morocco
    "MZ": None,           # Mozambique
    "MM": None,           # Myanmar
    "NA": None,           # Namibia
    "NR": None,           # Nauru
    "NP": None,           # Nepal
    "NL": "ECBDFR",       # Netherlands (Eurozone)
    "NC": None,           # New Caledonia
    "NZ": "INTDSRNZM193N",# New Zealand
    "NI": None,           # Nicaragua
    "NE": None,           # Niger
    "NG": None,           # Nigeria
    "NU": None,           # Niue
    "NF": None,           # Norfolk Island
    "KP": None,           # North Korea
    "MP": None,           # Northern Mariana Islands
    "NO": "INTDSRNOM193N",# Norway
    "OM": None,           # Oman
    "PK": None,           # Pakistan
    "PW": None,           # Palau
    "PS": None,           # Palestinian Territories
    "PA": None,           # Panama
    "PG": None,           # Papua New Guinea
    "PY": None,           # Paraguay
    "PE": "INTDSRPEM193N",# Peru
    "PH": "INTDSRPHM193N",# Philippines
    "PN": None,           # Pitcairn Islands
    "PL": "INTDSRPLM193N",# Poland
    "PT": "ECBDFR",       # Portugal (Eurozone)
    "PR": None,           # Puerto Rico
    "QA": None,           # Qatar
    "CG": None,           # Republic of Congo
    "RE": None,           # Reunion
    "RO": None,           # Romania
    "RU": "INTDSRRUM193N",# Russia
    "RW": None,           # Rwanda
    "BL": None,           # Saint Barthelemy
    "SH": None,           # Saint Helena
    "KN": None,           # Saint Kitts and Nevis
    "LC": None,           # Saint Lucia
    "MF": None,           # Saint Martin
    "PM": None,           # Saint Pierre and Miquelon
    "VC": None,           # Saint Vincent and the Grenadines
    "WS": None,           # Samoa
    "SM": None,           # San Marino
    "ST": None,           # Sao Tome and Principe
    "SA": "INTDSRSAM193N",# Saudi Arabia
    "SN": None,           # Senegal
    "RS": None,           # Serbia
    "SC": None,           # Seychelles
    "SL": None,           # Sierra Leone
    "SG": "INTDSRSGM193N",# Singapore
    "SX": None,           # Sint Maarten
    "SK": "ECBDFR",       # Slovakia (Eurozone)
    "SI": "ECBDFR",       # Slovenia (Eurozone)
    "SB": None,           # Solomon Islands
    "SO": None,           # Somalia
    "ZA": "INTDSRZAM193N",# South Africa
    "GS": None,           # South Georgia and South Sandwich Islands
    "KR": "INTDSRKRM193N",# South Korea
    "SS": None,           # South Sudan
    "ES": "ECBDFR",       # Spain (Eurozone)
    "LK": None,           # Sri Lanka
    "SD": None,           # Sudan
    "SR": None,           # Suriname
    "SJ": None,           # Svalbard and Jan Mayen
    "SE": "INTDSRSEM193N",# Sweden
    "CH": "INTDSRCHM193N",# Switzerland
    "SY": None,           # Syria
    "TW": None,           # Taiwan
    "TJ": None,           # Tajikistan
    "TZ": None,           # Tanzania
    "TH": "INTDSRTHM193N",# Thailand
    "TL": None,           # Timor-Leste
    "TG": None,           # Togo
    "TK": None,           # Tokelau
    "TO": None,           # Tonga
    "TT": None,           # Trinidad and Tobago
    "TN": None,           # Tunisia
    "TR": "INTDSRTRM193N",# Turkey
    "TM": None,           # Turkmenistan
    "TC": None,           # Turks and Caicos Islands
    "TV": None,           # Tuvalu
    "VI": None,           # US Virgin Islands
    "UG": None,           # Uganda
    "UA": None,           # Ukraine
    "AE": None,           # United Arab Emirates
    "GB": "INTDSRGBM193N",# United Kingdom
    "US": "FEDFUNDS",     # United States (Federal Funds Rate)
    "UY": None,           # Uruguay
    "UZ": None,           # Uzbekistan
    "VU": None,           # Vanuatu
    "VA": None,           # Vatican City
    "VE": None,           # Venezuela
    "VN": None,           # Vietnam
    "UM-WQ": None,        # Wake Island
    "WF": None,           # Wallis and Futuna
    "EH": None,           # Western Sahara
    "YE": None,           # Yemen
    "ZM": None,           # Zambia
    "ZW": None,           # Zimbabwe
    "SZ": None            # eSwatini
}