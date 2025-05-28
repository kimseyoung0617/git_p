from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def api_hello():
    return jsonify(message='Hello, Flask!')

@app.route('/api/echo', methods=['POST'])
ef api_echo():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify(greeting=f'Hello, {name}!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
