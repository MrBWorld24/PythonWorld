from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('linear_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='House Price: $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)