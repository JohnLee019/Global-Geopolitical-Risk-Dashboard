async function explanation(code){
    try {
        const response = await fetch(`/api/country/${code}/explain`);
        const data = await response.json()
        const summary = document.getElementById('ai-explanation');
        summary.textContent = data.summary;
    } catch (error) {
        summary.textContent = 'Currently now avaliable. Please try it again later on.'
    }
}