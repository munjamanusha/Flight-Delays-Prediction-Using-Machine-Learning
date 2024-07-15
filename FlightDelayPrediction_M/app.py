from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("E:/FlightDelayPrediction_M/flight.pkl", 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['POST'])
def prediction():
    #number=int(request.form['enter the flight number'])
    month = int(request.form['month'])
    dayofmonth = int(request.form['dayofmonth'])
    dayofweek = int(request.form['dayofweek'])
    
    origin = request.form['origin']
    if origin == "msp":
        origin = 1
    elif origin == "dtw":
        origin = 2
    elif origin == "jfk":
        origin = 3
    elif origin == "sea":
        origin = 4
    elif origin == "alt":
        origin = 5

    destination = request.form['destination']
    if destination == "msp":
        destination = 1
    elif destination == "dtw":
         destination = 2
    elif destination == "jfk":
        destination = 3
    elif destination == "sea":
        destination = 4
    elif destination == "alt":
        destination = 5

    dept = int(request.form['dept'])
    arrtime = int(request.form['arrtime'])
    actdept = int(request.form['actdept'])
    dept15 = dept - actdept
    
    total = np.array([[month, dayofmonth, dayofweek, origin, destination, dept, arrtime, dept15]])
    
    y_pred = model.predict(total)

    ans = 'The Flight will be on time' if y_pred[0] == 0 else 'The Flight will be delayed'

    return render_template("predict.html", showcase=ans)

if __name__ == '__main__':
    app.run(debug=True)
