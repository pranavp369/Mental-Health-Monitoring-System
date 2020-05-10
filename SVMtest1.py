# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:33:27 2020

@author: pranav
"""
# Support Vector Machine (SVM)
 
# Importing the libraries
import numpy as np
import matplotlib as plt
import pandas as pd
from InferenceEngine import infengine

#Defining parameters
param1=0
param2=0
param3=0
param4=0
param5=0
param6=0
param7=0
param8=0
parameter1= [param1,param2,param3,param4,param5,param6,param7,param8]

#Defining Dictionary for labels
d = {0:'Neutral',1:'Anger',2:'Disgust', 3:'Fear', 4:'Happiness', 5:'Sadness',6:'Surprise'}

#Function definition
def svmtest1(parameter):
    
    # Importing the dataset
    dataset = pd.read_csv('Dataset.csv') 
    X = dataset.iloc[:, [0,1,2,3,4,5,6,7]].values
    y = dataset.iloc[:, 8].values
     
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting SVM to the Training set
    from sklearn.svm import LinearSVC
    classifier = LinearSVC(random_state=0, tol=1e-5, multi_class= 'ovr')
    classifier.fit(X_train, y_train)

    #Getting the input list
    parameter1 = parameter
    parameter_final = np.array(parameter1)
    
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    #from sklearn.metrics import confusion_matrix
   # cm = confusion_matrix(y_test, y_pred)  

    #Displaying Accuracy, Precision,Recall
    from sklearn import metrics
    print("##########################################################################################")
    print("                                      CLASSIFICATION RESULTS                              ")
    print("")
    print("")
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100,"%")
    
    #Predicting for input data
    ypred = classifier.predict(parameter_final.reshape(1, -1))
    x = int(ypred)
    print("The classified label is :",d.get(x))
    print("##########################################################################################")

    
    #Sending Classified data to Inferwence Engine
    infengine(x)
   
   


if __name__ == '__main__':
    svmtest1(parameter1)
