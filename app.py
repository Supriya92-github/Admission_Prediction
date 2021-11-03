#import numpy as np
#import pandas as pd
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)
#model = pickle.load(open('Pickle_file_management.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
