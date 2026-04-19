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
    당신은 글로벌 거시경제 및 금융 리스크 분석 전문가입니다.
    다음 제공된 데이터를 바탕으로 {country_name}의 현재 경제 리스크 상황을 분석해 주세요.
    
    [데이터]
    - 국가명: {country_name}
    - 종합 리스크 점수: {risk_score} / 100
    - 주요 지표 현황(환율, 유가, 달러인덱스, VIX): {metrics}
    
    반드시 아래의 JSON 포맷으로만 응답해 주세요. 다른 설명이나 마크다운 백틱(```)은 추가하지 마세요.
    {{
        "summary": "현재 지표들을 바탕으로 현재 경제상황이 의미하는 바에 대한 2~3문장 영문 요약"
    }}
    """
    return prompt

def generate_explanation(country_name, risk_score, metrics, headlines=None):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash') 
        
        prompt = build_prompt(country_name, risk_score, metrics, headlines)
        
        # temperature는 그냥 최대한 사실적인 정보를 받고 싶어서 0.1로 했지만 나중에 수정 고려
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
        "title": f"Risk analysis temporarily unavailable for {country_name}",
        "summary": f"The current risk score is {risk_score}, but detailed AI analysis could not be loaded at this moment.",
        "bullets": [
            "Please check your API key or network connection.",
            "Try refreshing the page in a few minutes."
        ]
    }