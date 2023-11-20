document.getElementById('search-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var searchTerm = document.getElementById('search-field').value;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/scrape?search=' + encodeURIComponent(searchTerm), true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var results = JSON.parse(xhr.responseText);
            displayResults(results);
        } else {
            console.error('Error fetching data');
        }
    };
    xhr.send();
});

function displayResults(results) {
    var resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results
    results.forEach(function(paper) {
        var paperDiv = document.createElement('div');
        paperDiv.innerHTML = 'Title: ' + paper.title + '<br>Authors: ' + paper.authors.join(', ');
        resultsDiv.appendChild(paperDiv);
    });
}

