async function explanation(code){
    const summary = document.getElementById('ai-explanation');
    summary.textContent = "Explanation is loading..."
    try {
        const response = await fetch(`/api/country/${code}/explain`);
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json()
        summary.textContent = data.summary;
    } catch (error) {
        const summary = document.getElementById('ai-explanation');
        summary.textContent = 'Current Economy Explanation is currently not available. Please try it again later on.'
    }
}