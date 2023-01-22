# Centralised-Loan-default-prediction
Loan default is defined as the condition when a customer **give up** giving loan to the banks they took. 
In this repository I am going to do this prediction using **RandomForestclassifier** with ensemble of 1000 trees .
Centralized Loan default prediction is done here. This is also going to be implemented in decentralized manner i,e. When data set is dispersed.


## Algorithm

The algorithm used here is RandomForestClassifier with ensemble of 1000 trees. The algorithm is implemented in python using sklearn library. The algorithm is implemented in the following steps:

1. Importing the libraries
2. Importing the dataset
3. Splitting the dataset into the Training set and Test set
4. Training the Random Forest Classification model on the Training set
5. Predicting the Test set results
6. Saving the model using python in built **pickle** library

## Steps to run the code

1. Clone the repository using `git clone https://github.com/Aashish-compo/Centralised-Loan-default-prediction.git`
2. Install the required libraries sunch as sklearn, numpy, pandas, pickle
4. Run the code in the terminal using `python3 Centre.py`
5. It will create a pickle file named `model.pkl` which is the trained model in first run.
6. Run the code again then it will load the model from the pickle file and predict the result.








