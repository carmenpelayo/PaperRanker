from flask import Flask, jsonify
from arxiv_scraper import *
from filter_papers import *

app = Flask(__name__)

@app.route('/scrape')
def scrape_papers():
    try:
        scraped_papers = scrape_arxiv_papers()
        return jsonify(scraped_papers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/filter')
def filter_papers():
    try:
        # Assuming you need to pass the scraped papers to the filter function
        # You might need to adjust this based on how your scripts work
        papers_to_filter = scrape_arxiv_papers()
        filtered_papers = filter_arxiv_papers(papers_to_filter)
        return jsonify(filtered_papers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
