
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}</h1>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(1, parameter +1)]

    return '<br>'.join(numbers)

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return jsonify(error="Division by zero is not allowed"), 400
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return jsonify(error="Modulo by zero is not allowed"), 400
        result = num1 % num2
    else:
        return jsonify(error="Unsupported operation"), 400

    # Return the result as a JSON response
    return jsonify(num1=num1, operation=operation, num2=num2, result=result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
