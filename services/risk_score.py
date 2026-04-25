def risk_calculate(data):
    exchange = [e for e in data['exchange_rate']['values'] if e is not None]
    equity_index = [eq for eq in data['equity_index']['values'] if eq is not None]
    consumer_price = [cp for cp in data['consumer_price']['values'] if cp is not None]
    news_sentiment = [ns for ns in data['news_sentiment']['values'] if ns is not None]

    exchange_risk = calculation(exchange, 'exchange_rate')
    equity_index_risk = calculation(equity_index, 'equity_index')
    consumer_price_risk = calculation(consumer_price, 'consumer_price')
    news_sentiment_risk = calculation(news_sentiment, 'news_sentiment')

    final_score = (
        exchange_risk * 0.30 +
        equity_index_risk * 0.15 +
        consumer_price_risk * 0.25 +
        news_sentiment_risk * 0.30
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

    elif indicator == 'equity_index':
        return equity_index_score(change_pct)

    elif indicator == 'consumer_price':
        return consumer_price_score(change_pct)

    elif indicator == 'news_sentiment':
        return news_sentiment_score(change_pct)

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


def consumer_price_score(change_pct):
    # 소비자 물가(금리) 관련 리스크 평가
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


def news_sentiment_score(change_pct):
    # 뉴스 센티먼트 리스크 평가 (민감하게 반영)
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


def equity_index_score(change_pct):
    # 주가지수 관련 리스크 평가
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