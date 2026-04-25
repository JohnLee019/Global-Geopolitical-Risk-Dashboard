let currentChart = null;

async function drawGraph(code, metric){
  const canvas = document.getElementById('graph');
  const container = document.querySelector('.graph-container');
  const errorEl = container.querySelector('.graph-error');

  const styleMap = {
    exchange_rate: {
      borderColor: '#2563eb',
      backgroundColor: 'rgba(37, 99, 235, 0.15)'
    },
    equity_index: {
      borderColor: '#f59e0b',
      backgroundColor: 'rgba(245, 158, 11, 0.15)'
    },
    consumer_price: {
      borderColor: '#10b981',
      backgroundColor: 'rgba(16, 185, 129, 0.15)'
    },
    news_sentiment: {
      borderColor: '#ef4444',
      backgroundColor: 'rgba(239, 68, 68, 0.15)'
    }
  };

  try{
    const response = await fetch(`/api/country/${code}/series`);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    
    const data = await response.json();
    const series = data.series[metric];

    risk_display(data.risk)

    // 그래프 상자 다시 생성 
    canvas.style.display = 'block';
    errorEl.style.display = 'none';

    // 이렇게 안 하면 그래프가 계속 남음 
    if (currentChart) {
      currentChart.destroy();
    }

    currentChart = new Chart(canvas, {
      type: 'line',
      data: {
        labels: series.dates,
        datasets: [{
          label: series.label,
          data: series.values,
          fill: false,
          tension: 0.1,
          borderColor: styleMap[metric]['borderColor'],
          backgroundColor: styleMap[metric]['backgroundColor']
        }]
      }
    });
  } catch (error){
    const metricMap = {
      'exchange-rate': 'exchange_rate',
      'equity-index': 'equity_index',
      'consumer-price': 'consumer_price',
      'news-sentiment': 'news_sentiment',
    };

    if (currentChart) {
      currentChart.destroy();
      currentChart = null;
    }

    // 그래프 상자 삭제
    canvas.style.display = 'none';
    if (errorEl) {
      errorEl.textContent = `${metricMap[metric]} is currently not available. Please try it again later on.`;
    }
    errorEl.style.display = 'block';
    risk_display({risk_level: 'No data'});
  }
}