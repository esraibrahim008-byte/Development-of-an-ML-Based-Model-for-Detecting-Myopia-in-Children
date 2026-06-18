from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('myopia_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('myopia_model.pkl')
scaler = joblib.load('scaler.pkl')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction')
def prediction():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['POST'])
def predict():

    age = float(request.form['age'])
    sporthr = float(request.form['sporthr'])
    tvhr = float(request.form['tvhr'])
    mommy = float(request.form['mommy'])
    dadmy = float(request.form['dadmy'])
    spheq = float(request.form['spheq'])

    features = np.array([[age, sporthr, tvhr, mommy, dadmy, spheq]])

    features = scaler.transform(features)

    prediction = model.predict(features)

    result = "Myopia Detected" if prediction[0] == 1 else "No Myopia Detected"

    return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict', methods=['POST'])
def predict():

    age = float(request.form['age'])
    sporthr = float(request.form['sporthr'])
    tvhr = float(request.form['tvhr'])
    mommy = float(request.form['mommy'])
    dadmy = float(request.form['dadmy'])
    spheq = float(request.form['spheq'])

    features = np.array([[age, sporthr, tvhr, mommy, dadmy, spheq]])

    features = scaler.transform(features)

    prediction = model.predict(features)

    result = "Myopia Detected" if prediction[0] == 1 else "No Myopia Detected"

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)