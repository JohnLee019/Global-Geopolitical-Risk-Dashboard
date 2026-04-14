async function explanation(code){
    try {
        const response = await fetch(`/api/country/${code}/explain`);
        const summary = document.getElementById('ai-explanation');
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json()
        summary.textContent = data.bullets;
    } catch (error) {
        const summary = document.getElementById('ai-explanation');
        summary.textContent = 'Current Economy Explanation is currently not available. Please try it again later on.'
    }
}