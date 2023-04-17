import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
#import sklearn
from flask_ngrok import run_with_ngrok
import warnings



warnings.filterwarnings('ignore')

app = Flask(__name__)
run_with_ngrok(app)

model= pickle.load(open('CKD.pkl','rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('home1.html')


@app.route('/', methods=['GET'])
def predict():
    input_values = [float(x) for x in request.form.values()]
    inp_features = [input_values]
    print(inp_features )
    prediction = model.predict(inp_features)
    if prediction == 1:
        return render_template('result.html', prediction_text='OOPS ! You have Chronic Kidney Disease')
    else:
        return render_template('result.html', prediction_text='Well ! Your safe & healthy')


app.run()
