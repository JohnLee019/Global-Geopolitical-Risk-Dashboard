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

        new Chart(document.getElementById('oil-graph'), {
            type: 'line',
            data: {
                labels: oilData.dates,
                datasets: [{
                    label: oilData.label,
                    data: oilData.values,
                    borderColor: '#f59e0b',
                    backgroundColor: 'rgba(245, 158, 11, 0.15)',
                    fill: false,
                    tension: 0.1
                }]
            }
        });

        new Chart(document.getElementById('dollar-graph'), {
            type: 'line',
            data: {
                labels: dollarData.dates,
                datasets: [{
                    label: dollarData.label,
                    data: dollarData.values,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.15)',
                    fill: false,
                    tension: 0.1
                }]
            }
        });

        new Chart(document.getElementById('vix-graph'), {
            type: 'line',
            data: {
                labels: vixData.dates,
                datasets: [{
                    label: vixData.label,
                    data: vixData.values,
                    borderColor: '#ef4444',
                    backgroundColor: 'rgba(239, 68, 68, 0.15)',
                    fill: false,
                    tension: 0.1
                }]
            }
        });

        isGlobalGraphDrawn = true;

    } catch (error) {
        console.error("글로벌 데이터를 불러오는 데 실패했습니다:", error);
    }
}