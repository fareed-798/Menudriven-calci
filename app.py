from flask import Flask, request, jsonify
app = Flask(__name__)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    try:
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)