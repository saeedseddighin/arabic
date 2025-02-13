from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Sample data (replace with your own list of words and translations)
words = [
    {"word": "hello", "translation": "hola"},
    {"word": "goodbye", "translation": "adiós"},
    {"word": "cat", "translation": "gato"},
]

current_index = 0

@app.route('/')
def index():
    word = words[current_index]["word"]
    return render_template('index.html', word=word)

@app.route('/next')
def next_word():
    global current_index
    if current_index < len(words) - 1:
        current_index += 1
    return jsonify({'word': words[current_index]["word"]})

@app.route('/prev')
def prev_word():
    global current_index
    if current_index > 0:
        current_index -= 1
    return jsonify({'word': words[current_index]["word"]})

@app.route('/show_translation')
def show_translation():
    return jsonify({'translation': words[current_index]["translation"]})

@app.route('/update_translation', methods=['POST'])
def update_translation():
    new_translation = request.json.get('translation')
    words[current_index]["translation"] = new_translation
    return jsonify({'message': 'Translation updated successfully'})

@app.route('/google_word')
def google_word():
    word = words[current_index]["word"]
    return jsonify({'url': f'https://www.google.com/search?q={word}'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
