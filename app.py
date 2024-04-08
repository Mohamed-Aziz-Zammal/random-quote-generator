

import requests
import bs4
import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



def get_quote(quote_type):
    html = requests.get(f"https://www.keepinspiring.me/?s={quote_type}")
    html_parser = bs4.BeautifulSoup(html.text, "html.parser")
    all_quotes = html_parser.findAll("div", attrs={"class": "entry-summary"})
    random_number = random.randint(0, len(all_quotes) - 1)
    return all_quotes[random_number].text.strip()

@app.route('/quote', methods=['POST'])
def get_quote_web():
    quote_type = request.json.get('type')
    if quote_type not in ["science", "life", "love"]:
        return jsonify({'error': 'Invalid quote type'}), 400
    quote_text = get_quote(quote_type)
    return jsonify({'quote': quote_text})

if __name__ == '__main__':
    app.run(debug=True)



