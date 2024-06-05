import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
heart_data = pd.read_csv("C:\\Users\\tanmayee patil\\Desktop\\HeartAttackFinal\\heart.csv")
feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
heart_data.columns = feature_names + ['target']
X = heart_data.drop('target', axis=1)
Y = heart_data['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data : ', training_data_accuracy*100)
# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy*100)
input_data = (63, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#input_data =(52,1,0,125,212,0,1,168	,0	,1	,2	,2	,3)

# #change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)
# # reshape the numpy array as we are predicting for only on instance YouTube Content Creator
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
    print('The Person does not have a Heart Disease')
else:
    print('The Person has Heart Disease')
