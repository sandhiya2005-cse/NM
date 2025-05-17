from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

EXCEL_FILE = 'patient_records.xlsx'
CSV_TEMP_FILE = 'patient_records.csv'

def ensure_excel_exists():
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=[
            'Type', 'Name', 'Age', 'Height', 'Weight', 'BMI', 
            'BMI Category', 'Contact', 'Symptoms', 'Date'
        ])
        df.to_excel(EXCEL_FILE, index=False)

@app.route('/')
def home():
    return 'Welcome to the Patient Records API'

@app.route('/api/patients', methods=['GET'])
def get_patients():
    ensure_excel_exists()
    df = pd.read_excel(EXCEL_FILE)
    return jsonify(df.to_dict('records'))

@app.route('/api/patients', methods=['POST'])
def add_patient():
    ensure_excel_exists()
    data = request.json

    required_fields = ['Type', 'Name', 'Age', 'Height', 'Weight', 'BMI', 'BMI Category', 'Contact', 'Symptoms']
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Add current date if not provided
    if 'Date' not in data or not data['Date']:
        data['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    df = pd.read_excel(EXCEL_FILE)
    new_patient = pd.DataFrame([data])
    df = pd.concat([df, new_patient], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

    return jsonify({"message": "Patient added successfully", "data": data})

@app.route('/api/patients/excel', methods=['GET'])
def download_excel():
    ensure_excel_exists()
    return send_file(
        EXCEL_FILE,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='patient_records.xlsx'
    )

@app.route('/api/patients/csv', methods=['GET'])
def download_csv():
    ensure_excel_exists()
    df = pd.read_excel(EXCEL_FILE)
    df.to_csv(CSV_TEMP_FILE, index=False)
    response = send_file(
        CSV_TEMP_FILE,
        mimetype='text/csv',
        as_attachment=True,
        download_name='patient_records.csv'
    )
    # Optional: delete temp CSV after sending
    # os.remove(CSV_TEMP_FILE)
    return response

@app.route('/my-page')
def my_page():
    return 'This is my page'

if __name__ == '__main__':
    app.run(debug=True, port=5000)