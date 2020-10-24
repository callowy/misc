# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:42:23 2020

@author: Colin Moore

Resources Used: https://scikit-learn.org/
                stackoverflow.com
                https://pandas.pydata.org/
                https://www.pythonforengineers.com/python-for-scientists-and-engineers/
"""
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
pd.options.mode.chained_assignment = None

def convertDate(imported_set, col_name):
    """
    Parameters
    ----------
    imported_set : DataFrame        
    
    col_name : String
        Name of the column that you want to convert dates from. Use quotes, ie: "col_name"

    Returns
    -------
    Converts a row with conventional date formal into an ordinal value
    """
    imported_set[col_name] = imported_set[col_name].astype('datetime64[ns]')
    for index in range(imported_set[col_name].size):
        imported_set[col_name][index] = imported_set[col_name][index].toordinal()

# Training Set Data
movie_data = pd.read_csv("merged_movies.csv")

train_input = movie_data[["Opening Date", "Gross Opening", "Theaters Opening", "Theaters Widest",
                          "1st Week Percentage", "Per Theater Attendance"]]
convertDate(train_input, "Opening Date")

train_ID, train_dist = pd.factorize(movie_data["Distributor"])
train_input.insert(len(train_input.columns), "Distributor", train_ID)


train_output = movie_data[["Gross Total"]]


# Validation Data
validation = pd.read_csv("validate_D_data.csv")

test_input = validation[["Opening Date", "Gross Opening", "Theaters Opening", "Theaters Widest",
                          "1st Week Percentage", "Per Theater Attendance"]]
convertDate(test_input, "Opening Date")

test_ID, test_dist = pd.factorize(validation["Distributor"])
test_input.insert(len(test_input.columns), "Distributor", test_ID)

test_output = validation[["Gross Total"]]


rf = RandomForestRegressor(n_estimators=100)
rf.fit(train_input, np.ravel(train_output))

predictions = rf.predict(test_input)
accuracy = rf.score(test_input, test_output)
print("Model Accuracy: ", accuracy)

