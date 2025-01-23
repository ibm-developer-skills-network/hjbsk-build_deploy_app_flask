from flask import Flask, render_template, request
from Maths.mathematics import summation, substraction, multiplication


app = Flask("Mathematics Problem Solver")

@app.route("/sum", methods=['POST'])
def sum_route():
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    return str(summation(num1, num2))

@app.route("/sub", methods=['POST'])
def sub_route():
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    return str(substraction(num1, num2))

@app.route("/mul", methods=['POST'])
def mul_route():
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    return str(multiplication(num1, num2))

@app.route("/", methods=['GET', 'POST'])
def render_index_page():
    action = None
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    if 'add' in request.form:
        action = sum_route()
    elif 'sub' in request.form:
        action = sub_route()
        
    elif 'mul' in request.form:
        action = mul_route()
        
    else:
        pass
    
    return render_template('index.html',num1=num1, num2=num2, action=action)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083, debug=True)
