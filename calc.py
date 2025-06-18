from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return '''
        <h2>Simple Calculator</h2>
        <form action="/result">
            <input type="number" name="num1" placeholder="Enter first number">
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <input type="number" name="num2" placeholder="Enter second number">
            <button type="submit">Calculate</button>
        </form>
    '''

@app.route('/result')
def result():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 1))
    operation = request.args.get('operation', 'add')

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"

    return f"<h2>Result: {result}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
