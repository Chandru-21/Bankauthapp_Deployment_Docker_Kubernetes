# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:50:38 2021

@author: Chandramouli
"""

import pandas as pd
import numpy as np

df=pd.read_csv('BankNote_Authentication.csv')


### Independent and Dependent features
X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X.head()

### Train Test Split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

### Implement Random Forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

## Prediction
y_pred=classifier.predict(X_test)

### Check Accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)


### Create a Pickle file using serialization 
import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

import numpy as np
classifier.predict([[2,3,4,1]])