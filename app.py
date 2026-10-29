from Flask import Flask,request,jsonify
app = Flask(__name__)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    a = float(data.get('a',0))
    b = float(data.get('b',0))
    if operation=='add':
        result = add(a, b)
    elif operation=='sub':
        result = subtract(a, b)
    else:
        return jsonify({'error': 'Invalid operation'}),400
    return jsonify({'result': result})
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)