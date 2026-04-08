let currentChart = null;

async function drawGraph(code, metric){
  try{
      const response = await fetch(`/api/country/${code}/series`);
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }

      const data = await response.json();
      const series = data.exchange_rate;
      const ctx = document.getElementById('graph');
      const container = document.querySelector('.graph-container');
      const errorEl = container.querySelector('.graph-error');
      const canvas = document.getElementById('graph');

      // 그래프 상자 다시 생성 
      canvas.style.display = 'block';
      errorEl.style.display = 'none';

      // 이렇게 안 하면 그래프가 계속 남음 
      if (currentChart) {
        currentChart.destroy();
      }

      currentChart =new Chart(ctx, {
          type: 'line',
          data: {
            labels: series.dates,
            datasets: [{
              label: series.label,
              data: series.values,
              fill: false,
              tension: 0.1
            }]
          }
        });
  } catch (error){
    if (currentChart) {
      currentChart.destroy();
      currentChart = null;
    }

    const container = document.querySelector('.graph-container');
    const errorEl = container.querySelector('.graph-error');
    const canvas = document.getElementById('graph');
    
    // 그래프 상자 삭제
    canvas.style.display = 'none';
    if (errorEl) {
      errorEl.textContent = `Current country's graph is not available. Please try it again later on.`;
    }
    errorEl.style.display ='block'
  }
 }
 
