import numpy as np 
import joblib 



model = joblib.load('model.pkl') 
# trained_model = pickle.load(open('model.pkl', 'rb'),encoding='latin1')
def preprocessdata(Pclass,Age,Sex,SibSp,Fare,Parch,EmbarkedQ,EmbarkedS):
    test_data = [[Pclass,Age,Sex,SibSp,Fare,Parch,EmbarkedQ,EmbarkedS]]  
    prediction = model.predict(test_data) 
    return prediction 


