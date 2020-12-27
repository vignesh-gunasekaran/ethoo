from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
import pandas as pd
import xgboost as xg

app = Flask(__name__)



@app.route('/')
@app.route('/Home')
def hello_world():
   return render_template('home.html')

@app.route('/BreastCancerPrediction')
def cancer():
   return render_template('cancer.html')


@app.route('/LiverPrediction')
def liver():
   return render_template('liver.html')

@app.route('/HeartPrediction')
def heart():
   return render_template('heart.html')

@app.route('/About')
def about():
   return render_template('aboutme.html')

   
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
