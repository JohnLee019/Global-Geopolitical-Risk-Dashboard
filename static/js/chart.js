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
    bond_yield: {
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

    // None 값이면 그냥 바로 Catch error 쪽으로
    if (!series) {
      throw new Error("Current country data is not available");
    }

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
      },
      options: {
        scales: {
          x: {
            ticks: { color: '#cbd5e1' }, // x축 글씨 색상 밝게
            grid: { color: 'rgba(255, 255, 255, 0.1)' } // x축 배경 선 색상 연하게
          },
          y: {
            ticks: { color: '#cbd5e1' }, // y축 글씨 색상 밝게
            grid: { color: 'rgba(255, 255, 255, 0.1)' } // y축 배경 선 색상 연하게
          }
        },
        plugins: {
          legend: {
            labels: { color: '#e2e8f0' } // 상단 데이터 라벨(범례) 글씨 색상 밝게
          }
        }
      }
    });
  } catch (error){
    const metricMap = {
      'exchange_rate': 'Exchange Rate',
      'equity_index': 'Equity Index',
      'consumer_price': 'Consumer Price Index',
      'bond_yield': '10-Year Bond Yield'
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