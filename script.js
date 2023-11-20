async function fetchPapers() {
    try {
        const response = await fetch('/api/papers'); // Adjust the API endpoint as needed
        const papers = await response.json();
        const paperListElement = document.getElementById('paper-list');
        papers.forEach(paper => {
            const paperElement = document.createElement('div');
            paperElement.className = 'paper';
            paperElement.innerHTML = `<h2>${paper.title}</h2><p>${paper.authors.join(', ')}</p>`;
            paperListElement.appendChild(paperElement);
        });
    } catch (error) {
        console.error('Error fetching papers:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchPapers);
