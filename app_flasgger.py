# -*- coding: utf-8 -*-
"""
Created on Sat May 20 01:41:07 2023

@author: siddhant
"""

from flask import Flask,request
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
#Swagger automatically generates UI

app = Flask(__name__) #start the application from this point
Swagger(app) #indication to flask app to generate UI path


pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)


@app.route('/') #this is the home page
def home():
    return "Welcome to the home page"

@app.route('/predict',methods=['GET'])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
   This is using docstrings for specifications.
   ---
   parameters:  
     - name: variance
       in: query
       type: number
       required: true
     - name: skewness
       in: query
       type: number
       required: true
     - name: curtosis
       in: query
       type: number
       required: true
     - name: entropy
       in: query
       type: number
       required: true
   responses:
       200:
           description: The output values
       
   """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])

    if prediction == 1:
        return "The predicted value is " + str(prediction) + " and the note is authentic"
    else:
        return "The predicted value is " + str(prediction) + " and the note is not authentic"

@app.route('/predict_file',methods=['POST'])
def prediction_note_authentication():
    """ Let's authenticate bank note
    This is using  docstrings for specifications
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    responses:
        200:
            description: The output values
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The predicted value for csv file is " + str(list(prediction))
if __name__ == '__main__':
    app.run(debug=True)
    
#Sample search:
#http://127.0.0.1:5000/apidocs/