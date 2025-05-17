🏥 AI Healthcare Diagnostic System This project is a web-based healthcare diagnostic system that allows patient registration, stores their medical details, and provides downloadable reports in Excel and CSV formats. It also includes a chatbot-style assistant for basic healthcare interactions.

📁 Project Structure bash Copy Edit ├── index.htm # Frontend HTML for patient input and chatbot ├── styles.css # Styling (assumed external) ├── script.js # Frontend interactivity (assumed external) ├── python.py # Flask backend API ├── patient_records.xlsx # Auto-generated Excel record of patients 🚀 Features Patient registration form with details like name, age, height, weight, and symptoms.

BMI calculation and categorization.

Data persistence via Excel file.

Download patient records in Excel and CSV format.

A simple healthcare chatbot interface.

REST API built using Flask.

🔧 Requirements Python 3.x

Flask

Flask-CORS

Pandas

openpyxl (for Excel support)

Install dependencies:

bash Copy Edit pip install flask flask-cors pandas openpyxl ▶️ How to Run Start the Backend

bash Copy Edit python python.py Open the Frontend

Open index.htm in your browser (double-click or use a simple HTTP server like live-server).

🧠 API Endpoints GET /api/patients – Returns all patient records.

POST /api/patients – Adds a new patient record (expects JSON body).

GET /api/patients/excel – Download patient data in Excel format.

GET /api/patients/csv – Download patient data in CSV format.

📦 Data Format (POST /api/patients) json Copy Edit { "Type": "new", "Name": "John Doe", "Age": 30, "Height": 180, "Weight": 75, "BMI": 23.1, "BMI Category": "Normal", "Contact": "1234567890", "Symptoms": "Fever, cough" } 📌 Notes Ensure the backend server is running before using the form or download buttons.

Excel file (patient_records.xlsx) is created automatically if it doesn’t exist.
