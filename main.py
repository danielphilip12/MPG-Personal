import pickle
from flask import Flask,request,app, jsonify, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model from the pickle file made in the notebook. 
regmodel=pickle.load(open('pkl_file','rb'))


@app.route('/')
def home():
    return render_template("home.html")
# this is the home route to load home.html 

@app.route('/predict_api', methods=['post'])
def predict_api():
    data=request.json['data']
    # gets the data from the post method sent to the app. 
    print(data)
    input=np.array(list(data.values())).reshape(1,-1)
    # converts the data into an array of values and reshapes it to the format the model can understand. 
    output=regmodel.predict(input)
    # this is the result of the model's prediction of the inputs passed into it. 
    print(output[0])
    return jsonify(output[0])
# returns a json output of the model's prediction

@app.route('/predict', methods=['POST'])
def predict():
    input=[float(x) for x in request.form.values()]
    # gets the inputs from the submitted form's values. 
    print(input)
    input_array = np.array(input).reshape(1, -1)
    # reshapes the array of the inputs into a format the model can understand. 
    output=regmodel.predict(input_array)[0]
    # makes the prediction of the inputs passed in with the model. 
    return render_template("home.html", prediction_test="The predicted mpg value  is {}".format(output))
# returns the home.html template with prediction_test value passed in so it displays on the page. 


if __name__=="__main__":
    app.run(debug=True)











# def main():
#     print("Hello from mpg-personal!")


# if __name__ == "__main__":
#     main()
