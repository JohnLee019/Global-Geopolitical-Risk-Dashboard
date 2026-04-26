import yfinance as yf

def equity_data(country_code, label, start, end):  
    ticker_symbol, unit = COUNTRY_TO_EQUITY.get(country_code)
    if not ticker_symbol:
        return None, None
    
    ticker = yf.Ticker(ticker_symbol)
    historical_data = ticker.history(start=start, end=end)
    if historical_data.empty:        
        return None, None
    
    dates = []
    values = []
    for date, row in historical_data.iterrows():
        dates.append(date.strftime("%Y-%m-%d"))
        values.append(round(row["Close"], 2))
    
    series = {
        "label": unit,
        "unit": unit,
        "dates": dates,
        "values": values
    }
    return series

# 값이 존재하는 나라들과 안정적으로 가져올 수 있는 나라들만 
# 주식 시장이 없는 것돌도 상당수, 그리고 yfinance에서 무료로 가져올 수 없는 나라도 None
COUNTRY_TO_EQUITY = {
    "AF": None,       # Afghanistan
    "AX": None,       # Aland Islands
    "AL": None,       # Albania
    "DZ": None,       # Algeria
    "AS": None,       # American Samoa
    "AD": None,       # Andorra
    "AO": None,       # Angola
    "AI": None,       # Anguilla
    "AG": None,       # Antigua and Barbuda
    "AR": ("^MERV", "MERVAL"),  # Argentina
    "AM": None,       # Armenia
    "AW": None,       # Aruba
    "AU": ("^AXJO", "S&P/ASX 200"),  # Australia
    "AT": ("^ATX", "ATX"),  # Austria
    "AZ": None,       # Azerbaijan
    "BS": None,       # Bahamas
    "BH": None,       # Bahrain
    "UM-FQ": None,    # Baker Island
    "BD": None,       # Bangladesh
    "BB": None,       # Barbados
    "BY": None,       # Belarus
    "BE": ("^BFX", "BEL 20"),  # Belgium
    "BZ": None,       # Belize
    "BJ": None,       # Benin
    "BM": None,       # Bermuda
    "BT": None,       # Bhutan
    "BO": None,       # Bolivia
    "BQ": None,       # Bonaire, Saint Eustatius and Saba
    "BA": None,       # Bosnia and Herzegovina
    "BW": None,       # Botswana
    "BV": None,       # Bouvet Island
    "BR": ("^BVSP", "IBOVESPA"),  # Brazil
    "IO": None,       # British Indian Ocean Territory
    "VG": None,       # British Virgin Islands
    "BN": None,       # Brunei Darussalam
    "BG": None,       # Bulgaria
    "BF": None,       # Burkina Faso
    "BI": None,       # Burundi
    "KH": None,       # Cambodia
    "CM": None,       # Cameroon
    "CA": ("^GSPTSE", "S&P/TSX Composite"),  # Canada
    "CV": None,       # Cape Verde
    "KY": None,       # Cayman Islands
    "CF": None,       # Central African Republic
    "TD": None,       # Chad
    "CL": ("^IPSA", "S&P/CLX IPSA"),  # Chile
    "CN": ("000001.SS", "SSE Composite"),  # China
    "CX": None,       # Christmas Island
    "CC": None,       # Cocos (Keeling) Islands
    "CO": ("^IGBC", "IGBC"),  # Colombia
    "KM": None,       # Comoros
    "CK": None,       # Cook Islands
    "CR": None,       # Costa Rica
    "HR": None,       # Croatia
    "CU": None,       # Cuba
    "CW": None,       # Curaçao
    "CY": None,       # Cyprus
    "CZ": ("^PX", "PX Index"),  # Czechia
    "CI": None,       # Côte d'Ivoire
    "CD": None,       # Democratic Republic of Congo
    "DK": ("^OMXC20", "OMX Copenhagen 20"),  # Denmark
    "DJ": None,       # Djibouti
    "DM": None,       # Dominica
    "DO": None,       # Dominican Republic
    "EC": None,       # Ecuador
    "EG": ("^EGX30", "EGX 30"),  # Egypt
    "SV": None,       # El Salvador
    "GQ": None,       # Equatorial Guinea
    "ER": None,       # Eritrea
    "EE": None,       # Estonia
    "ET": None,       # Ethiopia
    "FK": None,       # Falkland Islands
    "FO": None,       # Faroe Islands
    "FM": None,       # Federated States of Micronesia
    "FJ": None,       # Fiji
    "FI": ("^OMXH25", "OMX Helsinki 25"),  # Finland
    "FR": ("^FCHI", "CAC 40"),  # France
    "GF": None,       # French Guiana
    "PF": None,       # French Polynesia
    "TF": None,       # French Southern and Antarctic Lands
    "GA": None,       # Gabon
    "GM": None,       # Gambia
    "GE": None,       # Georgia
    "DE": ("^GDAXI", "DAX"),  # Germany
    "GH": None,       # Ghana
    "GI": None,       # Gibraltar
    "GO": None,       # Glorioso Islands
    "GR": ("GD.AT", "Athens General"),  # Greece
    "GL": None,       # Greenland
    "GD": None,       # Grenada
    "GP": None,       # Guadeloupe
    "GU": None,       # Guam
    "GT": None,       # Guatemala
    "GG": None,       # Guernsey
    "GN": None,       # Guinea
    "GW": None,       # Guinea-Bissau
    "GY": None,       # Guyana
    "HT": None,       # Haiti
    "HM": None,       # Heard Island and McDonald Islands
    "HN": None,       # Honduras
    "HK": ("^HSI", "Hang Seng"),  # Hong Kong
    "UM-HQ": None,    # Howland Island
    "HU": ("^BUX", "BUX Index"),  # Hungary
    "IS": None,       # Iceland
    "IN": ("^BSESN", "SENSEX"),  # India
    "ID": ("^JKSE", "IDX Composite"),  # Indonesia
    "IR": None,       # Iran
    "IQ": None,       # Iraq
    "IE": ("^ISEQ", "ISEQ Overall"),  # Ireland
    "IM": None,       # Isle of Man
    "IL": ("^TA125.TA", "TA-125"),  # Israel
    "IT": ("FTSEMIB.MI", "FTSE MIB"),  # Italy
    "JM": None,       # Jamaica
    "JP": ("^N225", "Nikkei 225"),  # Japan
    "UM-DQ": None,    # Jarvis Island
    "JE": None,       # Jersey
    "UM-JQ": None,    # Johnston Atoll
    "JO": None,       # Jordan
    "JU": None,       # Juan De Nova Island
    "KZ": None,       # Kazakhstan
    "KE": None,       # Kenya
    "KI": None,       # Kiribati
    "XK": None,       # Kosovo
    "KW": None,       # Kuwait
    "KG": None,       # Kyrgyzstan
    "LA": None,       # Lao People's Democratic Republic
    "LV": None,       # Latvia
    "LB": None,       # Lebanon
    "LS": None,       # Lesotho
    "LR": None,       # Liberia
    "LY": None,       # Libya
    "LI": None,       # Liechtenstein
    "LT": None,       # Lithuania
    "LU": None,       # Luxembourg
    "MO": None,       # Macau
    "MK": None,       # Macedonia
    "MG": None,       # Madagascar
    "MW": None,       # Malawi
    "MY": ("^KLSE", "FTSE Bursa Malaysia KLCI"),  # Malaysia
    "MV": None,       # Maldives
    "ML": None,       # Mali
    "MT": None,       # Malta
    "MH": None,       # Marshall Islands
    "MQ": None,       # Martinique
    "MR": None,       # Mauritania
    "MU": None,       # Mauritius
    "YT": None,       # Mayotte
    "MX": ("^MXX", "IPC Mexico"),  # Mexico
    "UM-MQ": None,    # Midway Islands
    "MD": None,       # Moldova
    "MC": None,       # Monaco
    "MN": None,       # Mongolia
    "ME": None,       # Montenegro
    "MS": None,       # Montserrat
    "MA": None,       # Morocco
    "MZ": None,       # Mozambique
    "MM": None,       # Myanmar
    "NA": None,       # Namibia
    "NR": None,       # Nauru
    "NP": None,       # Nepal
    "NL": ("^AEX", "AEX Index"),  # Netherlands
    "NC": None,       # New Caledonia
    "NZ": ("^NZ50", "S&P/NZX 50"),  # New Zealand
    "NI": None,       # Nicaragua
    "NE": None,       # Niger
    "NG": None,       # Nigeria
    "NU": None,       # Niue
    "NF": None,       # Norfolk Island
    "KP": None,       # North Korea
    "MP": None,       # Northern Mariana Islands
    "NO": ("OBX.OL", "OBX Index"),  # Norway
    "OM": None,       # Oman
    "PK": ("^KSE", "KSE 100"),  # Pakistan
    "PW": None,       # Palau
    "PS": None,       # Palestinian Territories
    "PA": None,       # Panama
    "PG": None,       # Papua New Guinea
    "PY": None,       # Paraguay
    "PE": None,       # Peru
    "PH": ("PSEI.PS", "PSEi Index"),  # Philippines
    "PN": None,       # Pitcairn Islands
    "PL": ("^WIG20", "WIG20"),  # Poland
    "PT": ("PSI20.LS", "PSI 20"),  # Portugal
    "PR": None,       # Puerto Rico
    "QA": None,       # Qatar
    "CG": None,       # Republic of Congo
    "RE": None,       # Reunion
    "RO": None,       # Romania
    "RU": ("IMOEX.ME", "MOEX Russia"),  # Russia
    "RW": None,       # Rwanda
    "BL": None,       # Saint Barthelemy
    "SH": None,       # Saint Helena
    "KN": None,       # Saint Kitts and Nevis
    "LC": None,       # Saint Lucia
    "MF": None,       # Saint Martin
    "PM": None,       # Saint Pierre and Miquelon
    "VC": None,       # Saint Vincent and the Grenadines
    "WS": None,       # Samoa
    "SM": None,       # San Marino
    "ST": None,       # Sao Tome and Principe
    "SA": ("^TASI.SR", "Tadawul All Share"),  # Saudi Arabia
    "SN": None,       # Senegal
    "RS": None,       # Serbia
    "SC": None,       # Seychelles
    "SL": None,       # Sierra Leone
    "SG": ("^STI", "Straits Times Index"),  # Singapore
    "SX": None,       # Sint Maarten
    "SK": None,       # Slovakia
    "SI": None,       # Slovenia
    "SB": None,       # Solomon Islands
    "SO": None,       # Somalia
    "ZA": ("^J203.JO", "Johannesburg All Share"),  # South Africa
    "GS": None,       # South Georgia and South Sandwich Islands
    "KR": ("^KS11", "KOSPI"),  # South Korea
    "SS": None,       # South Sudan
    "ES": ("^IBEX", "IBEX 35"),  # Spain
    "LK": None,       # Sri Lanka
    "SD": None,       # Sudan
    "SR": None,       # Suriname
    "SJ": None,       # Svalbard and Jan Mayen
    "SE": ("^OMX", "OMX Stockholm 30"),  # Sweden
    "CH": ("^SSMI", "SMI Index"),  # Switzerland
    "SY": None,       # Syria
    "TW": ("^TWII", "TAIEX"),  # Taiwan
    "TJ": None,       # Tajikistan
    "TZ": None,       # Tanzania
    "TH": ("^SET.BK", "SET Index"),  # Thailand
    "TL": None,       # Timor-Leste
    "TG": None,       # Togo
    "TK": None,       # Tokelau
    "TO": None,       # Tonga
    "TT": None,       # Trinidad and Tobago
    "TN": None,       # Tunisia
    "TR": ("XU100.IS", "BIST 100"),  # Turkey
    "TM": None,       # Turkmenistan
    "TC": None,       # Turks and Caicos Islands
    "TV": None,       # Tuvalu
    "VI": None,       # US Virgin Islands
    "UG": None,       # Uganda
    "UA": None,       # Ukraine
    "AE": None,       # United Arab Emirates
    "GB": ("^FTSE", "FTSE 100"),  # United Kingdom
    "US": ("^GSPC", "S&P 500"),  # United States
    "UY": None,       # Uruguay
    "UZ": None,       # Uzbekistan
    "VU": None,       # Vanuatu
    "VA": None,       # Vatican City
    "VE": ("^IBC", "IBC Index"),  # Venezuela
    "VN": ("^VNINDEX.VN", "VN-Index"),  # Vietnam
    "UM-WQ": None,    # Wake Island
    "WF": None,       # Wallis and Futuna
    "EH": None,       # Western Sahara
    "YE": None,       # Yemen
    "ZM": None,       # Zambia
    "ZW": None,       # Zimbabwe
    "SZ": None        # eSwatini
}