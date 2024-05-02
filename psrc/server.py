from flask import Flask, render_template, request
import numpy as np
import solver 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    rows = int(request.form['rows'])
    cols = int(request.form['cols'])
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = float(request.form[f'element_{i}_{j}'])
    solver.row_reduce(matrix.tolist(), rows, cols)
    return 'Matrix solved!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
