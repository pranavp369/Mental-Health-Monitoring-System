# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:08:46 2020

@author: pranav
"""
#Importing the necessary python libraries
import numpy as np
import matplotlib as plt
import pandas as pd
from SVMtest1 import svmtest1

#Defining parameters
param1=0
param2=0
param3=0
parameter1= [param1,param2,param3]


#Defining the function

def regression(parameter):
    
    #Reading the Dataset.
    dataset = pd.read_csv('Dataset.csv')
    dataset.head()
    
    #Seperating the independant variables from the dependant variables.
    independant_variable = dataset.iloc[:,:-6].values
    
    
    print('-------------------------------------VALENCE-------------------------------')
    ###########################################################################
    
    #PERFORMING REGRESSION FOR THE FIRST INDEPENDANT VARIABLE(VALENCE)
    
    #Selecting the first independant variable
    v = dataset.iloc[:, 3].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(independant_variable, v, test_size = 0.25, random_state = 0)
    
    #Scaling the input data
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)    
    
    #Fitting Simple Linear Regression into Training Set
    from sklearn.linear_model import LinearRegression
    regression = LinearRegression()
    regression.fit(X_train,y_train)
    
    #Getting the input list
    parameter1 = parameter
    parameter = np.array(parameter1)    
    
    
    #Predicting Test Set results
    y_pred_1 = regression.predict(parameter.reshape(1,-1))
    
    #Buildind optimal model using Backward Elimination
    import statsmodels.formula.api as sm
    X = np.append(arr = np.ones((363571,1)).astype(int), values = independant_variable, axis = 1)
    x_opt = X[:, [0,1,2,3]]
    regressor_OLS = sm.OLS(endog =v, exog = x_opt).fit()
    a = regressor_OLS.summary()
    print(a)
    
    
    ###########################################################################
    print('###############################################################################')
    print('-------------------------------------AROUSAL-------------------------------')
    print('###############################################################################')    
    ###########################################################################
    
    #PERFORMING REGRESSION FOR THE SECOND INDEPENDANT VARIABLE(AROUSAL)
    
    #Selecting the first independant variable
    w = dataset.iloc[:, 4].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(independant_variable, w, test_size = 0.25, random_state = 0)
    
    #Scaling the input data
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)    
    
    #Fitting Simple Linear Regression into Training Set
    from sklearn.linear_model import LinearRegression
    regression = LinearRegression()
    regression.fit(X_train,y_train)
    
    #Predicting Test Set results
    y_pred_2 = regression.predict(parameter.reshape(1,-1))
    
    #Buildind optimal model using Backward Elimination
    import statsmodels.formula.api as sm
    X = np.append(arr = np.ones((363571,1)).astype(int), values = independant_variable, axis = 1)
    x_opt = X[:, [0,1,2,3]]
    regressor_OLS = sm.OLS(endog =w, exog = x_opt).fit()
    a = regressor_OLS.summary()
    print(a)
    
    
    ###########################################################################
    print('###############################################################################')
    print('-------------------------------------DOMINANCE--------------------------------')
    print('###############################################################################')    
    ###########################################################################
    
    #PERFORMING REGRESSION FOR THE THIRD INDEPENDANT VARIABLE(DOMINANCE)
    
    #Selecting the first independant variable
    x = dataset.iloc[:, 5].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(independant_variable, x, test_size = 0.25, random_state = 0)
    
    #Scaling the input data
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)    
    
    #Fitting Simple Linear Regression into Training Set
    from sklearn.linear_model import LinearRegression
    regression = LinearRegression()
    regression.fit(X_train,y_train)
    
    #Predicting Test Set results
    y_pred_3 = regression.predict(parameter.reshape(1,-1))
    
    #Buildind optimal model using Backward Elimination
    import statsmodels.formula.api as sm
    X = np.append(arr = np.ones((363571,1)).astype(int), values = independant_variable, axis = 1)
    x_opt = X[:, [0,1,2,3]]
    regressor_OLS = sm.OLS(endog =x, exog = x_opt).fit()
    a = regressor_OLS.summary()
    print(a)
    
    
    ###########################################################################
    print('###############################################################################')
    print('-----------------------------------FAMILIARITY-----------------------------')
    print('###############################################################################')    
    ###########################################################################
    
    #PERFORMING REGRESSION FOR THE FOURTH INDEPENDANT VARIABLE(FAMILIARITY)
    
    #Selecting the first independant variable
    y = dataset.iloc[:, 6].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(independant_variable, y, test_size = 0.25, random_state = 0)
    
    #Scaling the input data
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)    
    
    #Fitting Simple Linear Regression into Training Set
    from sklearn.linear_model import LinearRegression
    regression = LinearRegression()
    regression.fit(X_train,y_train)
    
    #Predicting Test Set results
    y_pred_4 = regression.predict(parameter.reshape(1,-1))
    
    #Buildind optimal model using Backward Elimination
    import statsmodels.formula.api as sm
    X = np.append(arr = np.ones((363571,1)).astype(int), values = independant_variable, axis = 1)
    x_opt = X[:, [0,1,2,3]]
    regressor_OLS = sm.OLS(endog =y, exog = x_opt).fit()
    a = regressor_OLS.summary()
    print(a)
    
    
    ###########################################################################
    print('###############################################################################')
    print('-------------------------------------LIKING-------------------------------')
    print('###############################################################################')    
    ###########################################################################
    
    #PERFORMING REGRESSION FOR THE FIFTH INDEPENDANT VARIABLE(LIKING)
    
    #Selecting the first independant variable
    z = dataset.iloc[:, 7].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(independant_variable, z, test_size = 0.25, random_state = 0)
    
    #Scaling the input data
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)    
    
    #Fitting Simple Linear Regression into Training Set
    from sklearn.linear_model import LinearRegression
    regression = LinearRegression()
    regression.fit(X_train,y_train)
    
    #Predicting Test Set results
    y_pred_5 = regression.predict(parameter.reshape(1,-1))
    
    #Buildind optimal model using Backward Elimination
    import statsmodels.formula.api as sm
    X = np.append(arr = np.ones((363571,1)).astype(int), values = independant_variable, axis = 1)
    x_opt = X[:, [0,1,2,3]]
    regressor_OLS = sm.OLS(endog =z, exog = x_opt).fit()
    a = regressor_OLS.summary()
    print(a)
     
    ###########################################################################    
    
    #Unwrapping the ECG and GSR values
    p1 = parameter[0]
    p2 = parameter[1]
    p3 = parameter[2]
    
    #Storing the Valence, Arousal , Dominance, Familiarity and Liking
    master_parameter = [p1, p2, p3, y_pred_1, y_pred_2, y_pred_3, y_pred_4, y_pred_5]
    
    print(master_parameter)
    
    #Calling the Classsification function with the derived parameters
    svmtest1(master_parameter)
    
    
    
    
    




    
if __name__ == '__main__':
    regression(parameter1)