from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random_number')
def get_random_number():
    number = random.randint(1, 100)
    return jsonify({'random_number': number})

@app.route('/random_string')
def get_random_string():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    string_length = 10
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return jsonify({'random_string': random_string})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)