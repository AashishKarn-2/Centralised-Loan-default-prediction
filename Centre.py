import data
import pickle
import os
df = data.load_data()

#Explore data by uncommenting the following lines

# print(df.head())
# print(df.describe())
# print(df.columns)
# print(df['Defaulted?'].value_counts())

features = df.drop('Defaulted?', axis=1)
target = df['Defaulted?']

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Import the model we are using
from sklearn.ensemble import RandomForestClassifier


# Check if the model file exists
if os.path.isfile('model.pkl'):
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

else:
    # Instantiate model with 1000 decision trees
    rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
    # Train the model on training data
    rf.fit(X_train, y_train)
    print("Model Trained Successfully")
    accuracy = rf.score(X_test, y_test)
    print("Accuracy: ", accuracy)

    # Save the model
    with open('model.pkl', 'wb') as f:
        pickle.dump(rf, f)
        loaded_model = rf
# Use the model for prediction

predictions = loaded_model.predict(X_test)
print(predictions)