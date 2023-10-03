from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 


app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 
@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        Pclass = request.form.get('Pclass')
        Sex = request.form.get('Sex')
        Age = request.form.get('Age')
        SibSp = request.form.get('SibSp')  
        Parch = request.form.get('Parch')  
        Fare = request.form.get('Fare') 
        EmbarkedQ = request.form.get('EmbarkedQ')   
        EmbarkedS = request.form.get('EmbarkedS')     

        prediction = utils.preprocessdata(Pclass,Sex,Age,SibSp,Parch,Fare,EmbarkedQ,EmbarkedS)

    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__': 
    app.run(debug=True) 
