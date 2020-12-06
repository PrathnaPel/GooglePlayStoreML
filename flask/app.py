from flask import Flask
from flask import render_template

import numpy as np
from flask import request, jsonify
import pickle

model = pickle.load(open('pickle_model.pkl', 'rb'))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    data = request.form
    prediction = model.predict([[data['type'],
    data['content-rating'],
    data['category'],
    data['genres'],
    data['reviews'],
    data['size'],
    data['installs'],
    data['price'],
    data['android-ver']]])
    output=prediction[0]
    return str(output)

if __name__ == "__main__":
    app.run()
