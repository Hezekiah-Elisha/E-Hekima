from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(message='Hello, World!'), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)