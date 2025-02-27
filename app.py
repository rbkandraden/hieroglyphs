from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Função para carregar os hieróglifos do arquivo JSON
def load_hieroglyphs():
    with open('static/hieroglyphs.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    hieroglyphs_data = load_hieroglyphs()  # Carregar hieróglifos do JSON
    return render_template('index.html', hieroglyphs=hieroglyphs_data['hieroglyphs'])

if __name__ == '__main__':
    app.run(debug=True)
