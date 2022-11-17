from flask import Flask,  request, jsonify, render_template, render_template_string
import pickle
import numpy as np
import pandas as pd
from sklearn import metrics
import warnings
import pickle
import inputscript
import os
from bs4 import BeautifulSoup


app = Flask(__name__)
model = pickle.load(open('FLASK_APP/Phishing_website_Model.pkl', 'rb'))



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')



@app.route("/predict")
def predict():
    return render_template('final.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    url = request.form['url']
    checkprediction = inputscript.main(url)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    print(output)
    if output == 1:
        pred="You are Safe! This is a Legitimate Website"
        print("Hello")
        #print(render_template_string('The Answer is {{ pred }}'))
        #return pred
    else:
        pred="You are not Safe! This is not Legitimate Website"
        print("Hai")
        #render_template_string('The Answer is {{ pred }}')
        
        #return render_template('final.html')
    return render_template('final.html', prediction_text=pred)

def predict_api():
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
 

@app.route("/")
def demo():
    return render_template("index.html")

@app.route("/register")
def demo1():
    return render_template("register.html")

#@app.route("/login", methods = ['POST'])
#def login():



