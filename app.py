from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()

    with open('static/data.json') as json_file:
        data = json.load(json_file)

    result = [item for item in data if query in item['title'].lower()]

    return render_template('index.html', results=result, query=query)


if __name__ == '__main__':
    app.run(debug=True)
