from flask import Flask, render_template, request
from sympy import symbols, diff, log, simplify, exp

app = Flask(__name__)

@app.route('/hitung', methods=['POST'])
def hitung():
    if request.method == 'POST':
        function_str = request.form['inputFunction']
        function_type = request.form['functionType']
        
        # Hitung turunan sesuai dengan jenis fungsi
        result = calculate_derivative(function_str, function_type)

        return render_template('calculate.html', result=result)
    
def calculate_derivative(function_str, function_type):
    x = symbols('x')
    try:
        function = simplify(function_str)
        if function_type == 'aljabar':
            derivative = diff(function, x)
            return derivative
        elif function_type == 'logaritma':
            derivative = diff(log(function), x)
            return derivative
        elif function_type == 'eksponen':
            derivative = diff(exp(function), x)
            return derivative
        else:
            return "Jenis fungsi tidak valid"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        function_str = request.form['inputFunction']
        function_type = request.form['functionType']
        result = calculate_derivative(function_str, function_type)

    return render_template('calculate.html', result=result)

@app.route('/profile')
def profile():
    # Placeholder for profile information
    return render_template('profile.html')

@app.route('/materi')
def materi():
    # Placeholder for study materials
    return render_template('materi.html')

if __name__ == '__main__':
    app.run(debug=True)
