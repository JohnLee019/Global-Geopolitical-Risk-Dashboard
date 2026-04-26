from fredapi import Fred
import os
from dotenv import load_dotenv

load_dotenv()
FRED_API_KEY = os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)

def get_bond_yield(country_code, label, start_date):
    series_id = COUNTRY_TO_INTEREST_RATE.get(country_code)
    
    if not series_id:
        return None
        
    try:
        data = fred.get_series(series_id, observation_start=start_date)
        
        if data.empty:
            return None
            
        data = data.dropna()
        
        dates = []
        values = []
        for date, value in data.items():
            dates.append(date.strftime("%Y-%m-%d"))
            values.append(round(value, 2))
        
        series = {
        "label": label,
        "unit": "GBY",
        "dates": dates,
        "values": values
        }

        return series
        
    except Exception as e:
        print(f"FRED API 호출 에러: {e}")
        return None

# 10년물 국채 금리 (10-Year Government Bond Yield) FRED 시리즈 ID 매핑
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
    "AR": None,           # Argentina (10년물 제공 안됨)
    "AM": None,           # Armenia
    "AW": None,           # Aruba
    "AU": "IRLTLT01AUM156N", # Australia
    "AT": "IRLTLT01ATM156N", # Austria 
    "AZ": None,           # Azerbaijan
    "BS": None,           # Bahamas
    "BH": None,           # Bahrain
    "UM-FQ": None,        # Baker Island
    "BD": None,           # Bangladesh
    "BB": None,           # Barbados
    "BY": None,           # Belarus
    "BE": "IRLTLT01BEM156N", # Belgium 
    "BZ": None,           # Belize
    "BJ": None,           # Benin
    "BM": None,           # Bermuda
    "BT": None,           # Bhutan
    "BO": None,           # Bolivia
    "BQ": None,           # Bonair, Saint Eustachius and Saba
    "BA": None,           # Bosnia and Herzegovina
    "BW": None,           # Botswana
    "BV": None,           # Bouvet Island
    "BR": None,           # Brazil
    "IO": None,           # British Indian Ocean Territory
    "VG": None,           # British Virgin Islands
    "BN": None,           # Brunei Darussalam
    "BG": None,           # Bulgaria
    "BF": None,           # Burkina Faso
    "BI": None,           # Burundi
    "KH": None,           # Cambodia
    "CM": None,           # Cameroon
    "CA": "IRLTLT01CAM156N", # Canada
    "CV": None,           # Cape Verde
    "KY": None,           # Cayman Islands
    "CF": None,           # Central African Republic
    "TD": None,           # Chad
    "CL": "IRLTLT01CLM156N", # Chile
    "CN": None,           # China (FRED에서 공식 10년물 미제공)
    "CX": None,           # Christmas Island
    "CC": None,           # Cocos (Keeling) Islands
    "CO": "IRLTLT01COM156N", # Colombia
    "KM": None,           # Comoros
    "CK": None,           # Cook Islands
    "CR": "IRLTLT01CRM156N", # Costa Rica
    "HR": None,           # Croatia
    "CU": None,           # Cuba
    "CW": None,           # Curaçao
    "CY": None,           # Cyprus
    "CZ": "IRLTLT01CZM156N", # Czechia
    "CI": None,           # Côte d'Ivoire
    "CD": None,           # Democratic Republic of Congo
    "DK": "IRLTLT01DKM156N", # Denmark
    "DJ": None,           # Djibouti
    "DM": None,           # Dominica
    "DO": None,           # Dominican Republic
    "EC": None,           # Ecuador
    "EG": None,           # Egypt
    "SV": None,           # El Salvador
    "GQ": None,           # Equatorial Guinea
    "ER": None,           # Eritrea
    "EE": "IRLTLT01EEM156N", # Estonia 
    "ET": None,           # Ethiopia
    "FK": None,           # Falkland Islands
    "FO": None,           # Faroe Islands
    "FM": None,           # Federated States of Micronesia
    "FJ": None,           # Fiji
    "FI": "IRLTLT01FIM156N", # Finland 
    "FR": "IRLTLT01FRM156N", # France 
    "GF": None,           # French Guiana
    "PF": None,           # French Polynesia
    "TF": None,           # French Southern and Antarctic Lands
    "GA": None,           # Gabon
    "GM": None,           # Gambia
    "GE": None,           # Georgia
    "DE": "IRLTLT01DEM156N", # Germany 
    "GH": None,           # Ghana
    "GI": None,           # Gibraltar
    "GO": None,           # Glorioso Islands
    "GR": "IRLTLT01GRM156N", # Greece 
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
    "HU": "IRLTLT01HUM156N", # Hungary
    "IS": "IRLTLT01ISM156N", # Iceland
    "IN": "IRLTLT01INM156N", # India
    "ID": "IRLTLT01IDM156N", # Indonesia
    "IR": None,           # Iran
    "IQ": None,           # Iraq
    "IE": "IRLTLT01IEM156N", # Ireland 
    "IM": None,           # Isle of Man
    "IL": "IRLTLT01ILM156N", # Israel
    "IT": "IRLTLT01ITM156N", # Italy 
    "JM": None,           # Jamaica
    "JP": "IRLTLT01JPM156N", # Japan
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
    "LV": "IRLTLT01LVM156N", # Latvia 
    "LB": None,           # Lebanon
    "LS": None,           # Lesotho
    "LR": None,           # Liberia
    "LY": None,           # Libya
    "LI": None,           # Liechtenstein
    "LT": "IRLTLT01LTM156N", # Lithuania 
    "LU": "IRLTLT01LUM156N", # Luxembourg 
    "MO": None,           # Macau
    "MK": None,           # Macedonia
    "MG": None,           # Madagascar
    "MW": None,           # Malawi
    "MY": None,           # Malaysia
    "MV": None,           # Maldives
    "ML": None,           # Mali
    "MT": None,           # Malta
    "MH": None,           # Marshall Islands
    "MQ": None,           # Martinique
    "MR": None,           # Mauritania
    "MU": None,           # Mauritius
    "YT": None,           # Mayotte
    "MX": "IRLTLT01MXM156N", # Mexico
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
    "NL": "IRLTLT01NLM156N", # Netherlands 
    "NC": None,           # New Caledonia
    "NZ": "IRLTLT01NZM156N", # New Zealand
    "NI": None,           # Nicaragua
    "NE": None,           # Niger
    "NG": None,           # Nigeria
    "NU": None,           # Niue
    "NF": None,           # Norfolk Island
    "KP": None,           # North Korea
    "MP": None,           # Northern Mariana Islands
    "NO": "IRLTLT01NOM156N", # Norway
    "OM": None,           # Oman
    "PK": None,           # Pakistan
    "PW": None,           # Palau
    "PS": None,           # Palestinian Territories
    "PA": None,           # Panama
    "PG": None,           # Papua New Guinea
    "PY": None,           # Paraguay
    "PE": None,           # Peru
    "PH": None,           # Philippines
    "PN": None,           # Pitcairn Islands
    "PL": "IRLTLT01PLM156N", # Poland
    "PT": "IRLTLT01PTM156N", # Portugal 
    "PR": None,           # Puerto Rico
    "QA": None,           # Qatar
    "CG": None,           # Republic of Congo
    "RE": None,           # Reunion
    "RO": None,           # Romania
    "RU": "IRLTLT01RUM156N", # Russia
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
    "SA": None,           # Saudi Arabia
    "SN": None,           # Senegal
    "RS": None,           # Serbia
    "SC": None,           # Seychelles
    "SL": None,           # Sierra Leone
    "SG": None,           # Singapore
    "SX": None,           # Sint Maarten
    "SK": "IRLTLT01SKM156N", # Slovakia 
    "SI": "IRLTLT01SIM156N", # Slovenia 
    "SB": None,           # Solomon Islands
    "SO": None,           # Somalia
    "ZA": "IRLTLT01ZAM156N", # South Africa
    "GS": None,           # South Georgia and South Sandwich Islands
    "KR": "IRLTLT01KRM156N", # South Korea
    "SS": None,           # South Sudan
    "ES": "IRLTLT01ESM156N", # Spain 
    "LK": None,           # Sri Lanka
    "SD": None,           # Sudan
    "SR": None,           # Suriname
    "SJ": None,           # Svalbard and Jan Mayen
    "SE": "IRLTLT01SEM156N", # Sweden
    "CH": "IRLTLT01CHM156N", # Switzerland
    "SY": None,           # Syria
    "TW": None,           # Taiwan
    "TJ": None,           # Tajikistan
    "TZ": None,           # Tanzania
    "TH": None,           # Thailand
    "TL": None,           # Timor-Leste
    "TG": None,           # Togo
    "TK": None,           # Tokelau
    "TO": None,           # Tonga
    "TT": None,           # Trinidad and Tobago
    "TN": None,           # Tunisia
    "TR": "IRLTLT01TRM156N", # Turkey
    "TM": None,           # Turkmenistan
    "TC": None,           # Turks and Caicos Islands
    "TV": None,           # Tuvalu
    "VI": None,           # US Virgin Islands
    "UG": None,           # Uganda
    "UA": None,           # Ukraine
    "AE": None,           # United Arab Emirates
    "GB": "IRLTLT01GBM156N", # United Kingdom
    "US": "DGS10",        # United States (10-Year Treasury Constant Maturity)
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