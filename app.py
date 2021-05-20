from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
app = Flask(__name__)
  
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,6)
    loaded_model = pickle.load(open("kmeansclusterassignment.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result


@app.route("/")
def index():
    return render_template("index.html"); 
@app.route('/result',  methods =["GET", "POST"])
def result():
    if request.method == "POST":
       Fresh= request.form.get("Fresh")  
       Milk= request.form.get("Milk")
       Grocery= request.form.get("Grocery")
       Frozen= request.form.get("Frozen")
       Detergents_Paper= request.form.get("Detergents_Paper")
       Delicassen= request.form.get("Delicassen")
       
       sc_X = StandardScaler()
       
       loaded_model = pickle.load(open("kmeansclusterassignment.pkl", "rb"))
       predict= loaded_model.predict(sc_X.fit_transform([[Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen]]))
       
    return render_template("result.html",Age=predict)
   
  
if __name__ == '__main__':
   app.run(debug = True)