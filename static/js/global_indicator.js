// 그래프 그렸는지 기억
let isGlobalGraphDrawn = false;

async function drawGlobalGraph() {
    if (isGlobalGraphDrawn) {
        return;
    }

    try {
        const response = await fetch('/api/global/global_indicators');
        if (!response.ok){
            throw new Error(`HTTP error: ${response.status}`);
        }
        
        const data = await response.json();
        const oilData = data.oil_price;
        const dollarData = data.dollar_index;
        const vixData = data.vix;

        const darkThemeOptions = {
            scales: {
                x: {
                    ticks: { color: '#cbd5e1' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                y: {
                    ticks: { color: '#cbd5e1' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            },
            plugins: {
                legend: {
                    labels: { color: '#e2e8f0' }
                }
            }
        };

         // 반복 줄이기 위해 헬퍼 함수로 정리
        const renderChart = (canvasId, seriesData, color) => {
            const canvas = document.getElementById(canvasId);
            if (!canvas || !seriesData) return;

            new Chart(canvas, {
                type: 'line',
                data: {
                    labels: seriesData.dates,
                    datasets: [{
                        label: seriesData.label,
                        data: seriesData.values,
                        borderColor: color.border,
                        backgroundColor: color.bg,
                        fill: false,
                        tension: 0.1
                    }]
                },
                options: darkThemeOptions  
            });
        };

        renderChart('oil-graph',    data.oil_price,    { border: '#f59e0b', bg: 'rgba(245, 158, 11, 0.15)' });
        renderChart('dollar-graph', data.dollar_index, { border: '#10b981', bg: 'rgba(16, 185, 129, 0.15)' });
        renderChart('vix-graph',    data.vix,          { border: '#ef4444', bg: 'rgba(239, 68, 68, 0.15)' });
        renderChart('gold-graph',        data.gold,        { border: '#fbbf24', bg: 'rgba(251, 191, 36, 0.15)' });   // 금색
        renderChart('natural-gas-graph', data.natural_gas, { border: '#60a5fa', bg: 'rgba(96, 165, 250, 0.15)' });   // 파랑
        renderChart('wheat-graph',       data.wheat,       { border: '#d97706', bg: 'rgba(217, 119, 6, 0.15)' });    // 갈색

        isGlobalGraphDrawn = true;

    } catch (error) {
        console.error("글로벌 데이터를 불러오는 데 실패했습니다:", error);
    }
}