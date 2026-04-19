def risk_calculate(data):
    exchange = [e for e in data['exchange_rate']['values'] if e is not None]
    oil = [o for o in data['oil_price']['values'] if o is not None]
    dollar = [d for d in data['dollar_index']['values'] if d is not None]
    vix = [v for v in data['vix']['values'] if v is not None]

    exchange_risk = calculation(exchange, 'exchange_rate')
    oil_risk = calculation(oil, 'oil_price')
    dollar_risk = calculation(dollar, 'dollar_index')
    vix_risk = calculation(vix, 'vix')

    final_score = (
        exchange_risk * 0.30 +
        oil_risk * 0.15 +
        dollar_risk * 0.25 +
        vix_risk * 0.30
    )

    # 0보다 작아지지 않게 하고, 100보다 커지지 않게
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
    if len(values) < 2:
        return 0

    first = values[0]
    last = values[-1]

    if first == 0:
        return 0

    change_pct = ((last - first) / first) * 100

    if indicator == 'exchange_rate':
        return exchange_score(change_pct)

    elif indicator == 'oil_price':
        return oil_score(change_pct)

    elif indicator == 'dollar_index':
        return dollar_score(change_pct)

    elif indicator == 'vix':
        return vix_score(change_pct)

    return 0


def exchange_score(change_pct):
    # USD/KRW 기준: 상승 = 원화 약세 = 위험 증가
    if change_pct <= -5:
        return 0
    elif change_pct < 0:
        return 10
    elif change_pct < 2:
        return 30
    elif change_pct < 5:
        return 60
    elif change_pct < 10:
        return 80
    else:
        return 100


def dollar_score(change_pct):
    # 달러 인덱스 상승 = 글로벌 긴장/유동성 압박
    if change_pct <= -3:
        return 0
    elif change_pct < 0:
        return 10
    elif change_pct < 2:
        return 25
    elif change_pct < 5:
        return 50
    elif change_pct < 10:
        return 75
    else:
        return 100


def vix_score(change_pct):
    # VIX 상승은 가장 민감하게 반영
    if change_pct <= -10:
        return 0
    elif change_pct < 0:
        return 5
    elif change_pct < 5:
        return 30
    elif change_pct < 10:
        return 55
    elif change_pct < 20:
        return 80
    else:
        return 100


def oil_score(change_pct):
    # 유가는 급등이 위험, 급락도 경기침체 신호일 수 있어 약한 위험 부여
    if change_pct <= -10:
        return 20
    elif change_pct < -3:
        return 10
    elif change_pct < 3:
        return 20
    elif change_pct < 7:
        return 45
    elif change_pct < 15:
        return 70
    else:
        return 90