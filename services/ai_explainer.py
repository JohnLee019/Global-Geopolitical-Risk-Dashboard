import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("GEMINI_API_KEY loaded:", bool(os.getenv("GEMINI_API_KEY")))

genai.configure(api_key=GEMINI_API_KEY)


def build_prompt(country_name, risk_score, metrics, headlines=None):
    prompt = f"""
    You are an expert in global macroeconomic and financial risk analysis.
    Please analyze the current economic risk situation for {country_name} based on the provided data.
    
    [Data]
    - Country: {country_name}
    - Overall Risk Score: {risk_score} / 100
    - Key Indicators (exchange rate, equity index, consumer price index, 10-year bond yield): {metrics}
    
    Respond STRICTLY in JSON format as shown below. Do not include any markdown formatting like ```json, and do not add any conversational text.
    {{
        "summary": "Write a concise 2-3 sentence English summary explaining what the current macroeconomic situation implies based on the provided indicators."
    }}
    """
    return prompt

def generate_explanation(country_name, risk_score, metrics, headlines=None):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash') 
        
        prompt = build_prompt(country_name, risk_score, metrics, headlines)
        
        # temperature는 0.1로 유지하여 가장 확률이 높고 일관된 분석 결과를 얻도록 설정
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1, 
                response_mime_type="application/json"
            )
        )
        
        result = json.loads(response.text)
        return result
        
    except Exception as e:
        print(f"AI API 호출 오류: {e}")
        return fallback_explanation(country_name, risk_score)

def fallback_explanation(country_name, risk_score):
    return {
        "summary": f"The current risk score is {risk_score}, but detailed AI analysis could not be loaded at this moment.",
    }