import numpy as np

def risk_calculate(data):
    exchange = [e for e in (data.get('exchange_rate') or {}).get('values', []) if e is not None]
    equity_index = [eq for eq in (data.get('equity_index') or {}).get('values', []) if eq is not None]
    consumer_price = [cp for cp in (data.get('consumer_price') or {}).get('values', []) if cp is not None]
    bond_yield = [by for by in (data.get('bond_yield') or {}).get('values', []) if by is not None]

    exchange_risk = calculation(exchange, 'exchange_rate')
    equity_index_risk = calculation(equity_index, 'equity_index')
    consumer_price_risk = calculation(consumer_price, 'consumer_price')
    bond_yield_risk = calculation(bond_yield, 'bond_yield')

    final_score = (
        exchange_risk * 0.25 +
        equity_index_risk * 0.25 +
        consumer_price_risk * 0.25 +
        bond_yield_risk * 0.25
    )

    final_score = max(0, min(final_score, 100))

    if final_score < 25:
        risk_level = "Low"
    elif final_score < 50:
        risk_level = "Medium"
    elif final_score < 75:
        risk_level = "High"
    else:
        risk_level = "Very High"

    return {
        "risk_score": round(final_score, 1),
        "risk_level": risk_level
    }

def calculation(values, indicator):
    # 비교할 데이터가 2개 미만인 경우 리스크를 0으로 반환
    if len(values) < 2:
        return 0

    arr_values = np.array(values)
    mean = np.mean(arr_values)
    std = np.std(arr_values)
    
    first = arr_values[0]
    last = arr_values[-1]
    
    # 1. Z-Score (표준점수) 산출: 현재 값이 과거 평균에서 얼마나 벗어났는가?
    if std == 0:
        z_score = 0
    else:
        z_score = (last - mean) / std

    # 2. 단순 등락률 (기간 전체 기준)
    change_pct = ((last - first) / first) * 100 if first != 0 else 0
    
    # 3. 단기 변동성 (Volatility): 기간 내 변화율의 표준편차
    diffs = np.diff(arr_values)
    # 0으로 나누는 오류(ZeroDivisionError) 방지
    safe_arr_values = np.where(arr_values[:-1] == 0, 1e-9, arr_values[:-1]) 
    pct_changes = (diffs / safe_arr_values) * 100
    volatility = np.std(pct_changes) if len(pct_changes) > 0 else 0

    # 지표 성격에 맞는 점수화 함수 호출
    if indicator == 'exchange_rate':
        return exchange_score(z_score, volatility)
    elif indicator == 'equity_index':
        return equity_index_score(z_score, change_pct, volatility)
    elif indicator == 'consumer_price':
        return consumer_price_score(z_score)
    elif indicator == 'bond_yield':
        # 국채 금리는 절대적 차이(bp 개념)도 유의미하므로 넘겨줌
        yield_diff = last - first 
        return bond_yield_score(z_score, yield_diff, volatility)

    return 0

def exchange_score(z_score, volatility):
    # [환율] 방향성(상승/하락)보다는 급격한 변동(양방향) 자체를 글로벌 리스크로 간주
    abs_z = abs(z_score)
    
    if abs_z < 0.5:
        base_score = 10
    elif abs_z < 1.0:
        base_score = 30
    elif abs_z < 2.0:
        base_score = 60
    elif abs_z < 3.0:
        base_score = 85
    else:
        base_score = 100
        
    # 변동성(널뛰기 장세)이 심할 경우 리스크 점수 가산
    risk = base_score + (volatility * 2)
    return min(max(risk, 0), 100)

def equity_index_score(z_score, change_pct, volatility):
    # [주가지수] 큰 폭의 하락(마이너스 등락률 및 Z-score)과 높은 변동성을 리스크로 간주
    if z_score > 1.0 or change_pct > 5:
        base_score = 10   # 호황 (안전)
    elif z_score > 0 or change_pct > 0:
        base_score = 30   # 강보합
    elif z_score > -1.0 or change_pct > -5:
        base_score = 50   # 약보합 및 조정장
    elif z_score > -2.0 or change_pct > -10:
        base_score = 75   # 하락장 (위험)
    else:
        base_score = 90   # 폭락장 (고위험)
        
    # 하락장에 극심한 변동성이 동반될 경우 리스크 추가
    risk = base_score + volatility
    return min(max(risk, 0), 100)

def consumer_price_score(z_score):
    # [소비자 물가] 인플레이션(급등)과 디플레이션(급락) 양방향 모두 경제 위험 (절댓값 평가)
    abs_z = abs(z_score)
    
    if abs_z < 0.5:
        return 15
    elif abs_z < 1.0:
        return 35
    elif abs_z < 2.0:
        return 65
    elif abs_z < 3.0:
        return 85
    else:
        return 100

def bond_yield_score(z_score, yield_diff, volatility):
    # [국채 금리] Z-score 기반의 급등락 및 절대적인 bp 변동성 모두 리스크 요인으로 반영
    abs_z = abs(z_score)
    abs_diff = abs(yield_diff)
    
    if abs_z < 0.5 and abs_diff < 0.2:
        base_score = 15
    elif abs_z < 1.0 and abs_diff < 0.5:
        base_score = 40
    elif abs_z < 2.0:
        base_score = 70
    elif abs_z < 3.0:
        base_score = 85
    else:
        base_score = 100
        
    risk = base_score + (volatility * 1.5)
    return min(max(risk, 0), 100)