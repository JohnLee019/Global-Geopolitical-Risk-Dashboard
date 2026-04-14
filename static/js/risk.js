async function risk_display(risk) {
        const risk_status = document.getElementById('risk');
        risk_status.textContent = risk['risk_level'];
};