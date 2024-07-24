from flask import Flask, render_template, request
from model import predict_heart_disease

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [
        float(request.form['age']),
        float(request.form['sex']),
        float(request.form['cp']),
        float(request.form['trestbps']),
        float(request.form['chol']),
        float(request.form['fbs']),
        float(request.form['restecg']),
        float(request.form['thalach']),
        float(request.form['exang']),
        float(request.form['oldpeak']),
        float(request.form['slope']),
        float(request.form['ca']),
        float(request.form['thal'])
    ]

    prediction = predict_heart_disease(input_data)
    
    if prediction == 0:
        result = 'The Person does not have a Heart Disease'
    else:
        result = 'The Person has Heart Disease'
    
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
