# Global Macroeconomic Risk Map

A web-based dashboard designed to analyze, quantify, and visualize macroeconomic risks for countries worldwide. The application features an interactive world map that provides users with real-time financial data, a calculated risk score, and AI-generated summaries of a country's current economic situation.

<img width="2372" height="1305" alt="image of the website" src="https://github.com/user-attachments/assets/f0e72be0-077a-430e-bd40-12d9c7f16abd" />

## Features

* **Interactive World Map:** Click on any country to retrieve its specific economic data and risk profile using `jsVectorMap`.
* **Macroeconomic Indicators:** Visualizes historical data (via `Chart.js`) for key economic metrics:
    * Exchange Rates (vs. USD)
    * Equity Indices (Major national stock market indices)
    * Consumer Price Index (CPI)
    * 10-Year Government Bond Yields
* **Risk Score Calculation:** Dynamically calculates an economic risk score (0-100) and risk level (Low, Medium, High, Very High) based on recent Z-scores, percentage changes, and volatility across the collected indicators.
* **AI-Powered Economic Explanations:** Utilizes Google's Gemini API to generate concise, expert-level summaries explaining the implications of a country's current macroeconomic situation.
* **Global Indicators:** A dedicated section to track overarching global trends, including WTI Crude Oil Prices, the US Dollar Index (DXY), and the CBOE Volatility Index (VIX).
* **Caching:** Implements `Flask-Caching` to optimize API response times and reduce redundant external data requests.

## Tech Stack

**Frontend:**
* HTML5, CSS3, JavaScript
* [Chart.js](https://www.chartjs.org/) (Data visualization)
* [jsVectorMap](https://jvm-docs.vercel.app/) (Interactive map)

**Backend:**
* Python 3
* Flask (Web framework)
* Flask-Caching

**Data Sources & External APIs:**
* [yfinance](https://pypi.org/project/yfinance/): Equity indices and global market data.
* [FRED API (Federal Reserve Economic Data)](https://fred.stlouisfed.org/docs/api/fred/): Consumer Price Index and Bond Yields.
* [Frankfurter API](https://www.frankfurter.app/docs/): Real-time and historical exchange rates.
* [Google Gemini API](https://ai.google.dev/): Generative AI for economic summaries.

## Installation and Setup

### Prerequisites
* Python 3.8+
* API Keys for FRED and Google Gemini.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/johnlee019/global-geopolitical-risk-dashboard.git](https://github.com/johnlee019/global-geopolitical-risk-dashboard.git)
    cd global-geopolitical-risk-dashboard
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    FRED_API_KEY=your_fred_api_key_here
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```

6.  **Access the dashboard:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure

```text
├── app.py                  # Main Flask application and routing
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── services/               # Backend logic and data fetching
│   ├── ai_explainer.py     # Gemini API integration for summaries
│   ├── bond_yield.py       # FRED API integration for bond yields
│   ├── common_data.py      # yfinance integration for global indicators
│   ├── consumer_price.py   # FRED API integration for CPI
│   ├── equity.py           # yfinance integration for stock indices
│   ├── exchange_data.py    # Frankfurter API integration for FX rates
│   └── risk_score.py       # Algorithm for calculating economic risk
├── static/                 # Frontend assets
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── js/
│       ├── ai.js           # Handles AI explanation fetching
│       ├── chart.js        # Logic for rendering indicator charts
│       ├── global_indicator.js # Logic for global indicator charts
│       ├── map.js          # jsVectorMap initialization and interactions
│       └── risk.js         # Updates UI with risk score
└── templates/
    └── index.html          # Main HTML template
