## Titanic Survival Prediction---Supervised Learning/Decision Tree
# import libraries
import numpy as np 
import pandas as pd 
# allow use of display
from IPython.display import display
# import supplementary visualizations code
import visuals as vs 
# pretty display for notebooks
%matplotlib inline

# load dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)
# print first few entries
display (full_data.head())

# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)
# Show the new dataset with 'Survived' removed
display(data.head())

def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):         
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"
    
# Test the 'accuracy_score' function
predictions = pd.Series(np.ones(5, dtype = int))
print accuracy_score(outcomes[:5], predictions)

							'''Prediction 0'''
def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """
    predictions = []
    for passenger in data.iterrows():        
        # Predict the survival of 'passenger'
        predictions.append(0)    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_0(data)

#check the accuracy
print accuracy_score(outcomes, predictions)

						'''visual a feature'''
# Visual the possible factors(dataframe, target, field, [condition])
vs.survival_stats(data, outcomes, 'Sex')
						'''prediction 1'''
def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    predictions = []
    for passenger in data.iterrows():
        if passenger[1]['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)
    # Return our predictions
    return pd.Series(predictions)
# Make the predictions
predictions = predictions_1(data)

print accuracy_score(outcomes, predictions)
		
					'''vs 2'''
vs.survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])
					'''prediction 2'''
def predictions_2(data):
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """    
    predictions = []
    for passenger in data.iterrows():
        if passenger[1]['Age']<10 and passenger[1]['Sex']=='male':
            predictions.append(1)
        elif passenger[1]['Sex']=='female':
            predictions.append(1)
        else:
            predictions.append(0)
    # Return our predictions
    return pd.Series(predictions)
# Make the predictions
predictions = predictions_2(data)

print accuracy_score(outcomes, predictions)

					'''vs 3'''
vs.survival_stats(data, outcomes, 'SibSp', ["Sex == 'female'"])
					'''prediction 3'''
def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for passenger in data.iterrows():
        if passenger[1]['Fare'] > 300:
            predictions.append(1)
        elif passenger[1]['Age']<10 and passenger[1]['Sex']=='male':
            predictions.append(1)
        elif passenger[1]['Sex']== 'female' and passenger[1]['SibSp']<5:
            predictions.append(1)
        else:
            predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_3(data)

print accuracy_score(outcomes, predictions)