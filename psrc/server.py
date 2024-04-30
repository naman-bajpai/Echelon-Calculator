from flask import Flask, jsonify, request, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
from flask import render_template


app = Flask(__name__)

@app.route('/upload', methods=['POST'])  
def upload_data():
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    selected_columns = request.form.getlist('columns')
    if not selected_columns:
        return jsonify({'error': 'No columns selected'}), 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    plots = []
    for column in selected_columns:
        try:
            plt.figure()
            plt.plot(df[column])
            plt.xlabel('Index')
            plt.ylabel(column)
            plt.title(f'{column} Plot')
            plt.grid(True)

            # Convert plot to base64
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            buffer.seek(0)
            plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plots.append({'column': column, 'plot_data': plot_data})
        except KeyError:
            return jsonify({'error': f'Column "{column}" not found in dataset'}), 400

    return render_template('visualization.html', plots=plots)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
