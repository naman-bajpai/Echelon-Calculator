from flask import Flask, render_template, request
import numpy as np
import sympy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    rows = int(request.form['rows'])
    cols = int(request.form['cols'])
    

    matrix_data = [[sympy.Symbol(f'element_{i}_{j}') for j in range(cols)] for i in range(rows)]
    sympy_matrix = sympy.Matrix(matrix_data)
    

    reduced_matrix = sympy_matrix.rref()
    
    return render_template('solution.html', original_matrix=sympy_matrix, reduced_matrix=reduced_matrix)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
