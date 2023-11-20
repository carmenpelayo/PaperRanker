from flask import Flask, render_template, request, jsonify
from filter_papers import *
from arxiv_scraper import Paper  # Assuming this is your model for papers

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    # Here, you should call the appropriate function from filter_papers.py
    # For demonstration, I'm assuming you'll process the search term to get papers
    # This is a simplified example. You'll need to adapt it based on your actual data and functions
    papers = [Paper(arxiv_id="1234.5678", title=search_term, authors=["Author 1"], abstract="Sample abstract")]
    paper_strings = [paper_to_string(paper) for paper in papers]
    # Call the function from filter_papers.py
    # You'll need to pass the appropriate arguments based on your function's requirements
    filtered_papers = run_on_batch(paper_strings, "Your base prompt", "Your criterion", "Your postfix prompt")
    return jsonify(filtered_papers)

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
