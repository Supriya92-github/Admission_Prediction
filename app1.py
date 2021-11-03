import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('Pickle_file_management.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #input_features = [float(x) for x in request.form.values()]
    if request.method == 'POST':
        gre = float(request.form['pregnancies'])
        tofel = float(request.form['glucose'])
        rating = float(request.form['bloodpressure'])
        sop = float(request.form['skinthickness'])
        lor = float(request.form['insulin'])
        cgpa = float(request.form['bmi'])
        research = float(request.form['dpf'])
        #coa = float(request.form['age'])
    features_value = np.array([[gre,tofel,rating,sop,lor,cgpa,research]]) #,coa]])
    
    # features_name = [ "GRE Score","TOEFL Score","University Rating", "SOP", "LOR ",
    #                    "CGPA", "Research", "Chance of Admit"]
    
    # df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(features_value)
        
    if output > 0.5:
        prediction = "Your have good chance of selection. Chance : {}%".format(output*100)
    else:
        prediction = "Your don't have good chance of selection. Chance : {}%".format(output*100)
        

    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get('PORT',5000))
    #app.run(host='0.0.0.0', port=port)
