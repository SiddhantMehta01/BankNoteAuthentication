from flask import Flask,request
import pickle
import pandas as pd

app = Flask(__name__) #start the application from this point

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)


@app.route('/') #this is the home page
def home():
    return "Welcome to the home page"

@app.route('/predict',methods=['GET'])
def predict_note_authentication():
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
   df_test = pd.read_csv(request.files.get("file"))
   prediction = classifier.predict(df_test)
   return "The predicted value for csv file is " + str(list(prediction))
if __name__ == '__main__':
    app.run(debug=True)
    
#Sample search:
#http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1