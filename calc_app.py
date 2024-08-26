from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']

    if operation == 'add':
        result = float(num1) + float(num2)
    elif operation == 'subtract':
        result = float(num1) - float(num2)
    elif operation == 'multiply':
        result = float(num1) * float(num2)
    elif operation == 'divide':
        result = float(num1) / float(num2)
    else:
        result = 'Invalid Operation'

    return render_template('index2.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
