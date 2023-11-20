from flask import Flask, jsonify
from paper_scanner.arxiv_scraper import fetch_papers

app = Flask(__name__)

@app.route('/api/papers')
def get_papers():
    try:
        papers = fetch_papers()
        return jsonify(papers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
