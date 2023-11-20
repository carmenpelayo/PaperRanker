from flask import Flask, jsonify
from arxiv_scraper import *
from filter_papers import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my paper ranking website!'

@app.route('/scrape')
def scrape_papers():
    search_term = request.args.get('search', 'math.AC')  # Default to 'math.AC' if no search term is provided
    try:
        papers = get_papers_from_arxiv_rss_api(search_term, None)
        papers_json = json.dumps(papers, cls=EnhancedJSONEncoder)
        return papers_json
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
