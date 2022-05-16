import pickle
import flask
import sklearn
import pandas as pd
import streamlit as st
import os


# Load our model with pickle 
model = pickle.load(open('lgbm_home_risk_model.pkl', 'rb'))
# Load data test sample 
df_test_sample = pd.read_csv('test_sample_data_home_risk.csv', index_col = 0)
# Drop predict last column predict proba of our dataframe not used here
df_test_sample.drop(columns = 'TARGET_PROB', inplace = True)
# Define the treshold of our application
treshold = 0.49
# defining flask pages
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# definig home page
@app.route('/', methods=['GET'])
def home():
    return "<h1>Home credit risk  API</h1><p>This site is a prototype API \
    for model scoring project 7 of OpenClassRooms DataScientist .</p>"
# defining page for the results of a prediction via index
@app.route('/scores', methods=['GET'])
def predict():
    # get the index from a request
    data_index = flask.request.args.get('index')
    # get inputs features from the data with index.
    input = df_test_sample.loc[int(data_index), :]
    # predict probability score. 
    model_prediction = model.predict_proba(input.values.reshape(1,-1))
    # create a dictionnary to janosify. We get the probability to be positive and evaluate if the credit is accepted (1) or denied (0)!
    dict_result = {'ID_loan':int(data_index), 'Credit_score': model_prediction[:,1][0], 'Answer': int(model_prediction[:,1][0] < treshold)}
    return flask.jsonify(dict_result)

# add command for running the application with Heroku on cloud
if __name__ == "__main__":
    app.run()
