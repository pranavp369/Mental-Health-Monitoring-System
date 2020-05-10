# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:19:20 2020

@author: pranav
"""

#Importing Libraries
from Regression import regression
import time

#Data Acquisition function
def dataacq(result1):
    #Defining a Timer Function
    def timerfunc(t):
        b=4
        while t:
            mins, secs = divmod(t, 60)
            time.sleep(1)
            t -= 1
            a = ((t+1)-b)*20
            b=b-2
            print(a,"%", end='\r')
            
    #Acquiring the ECG and GSR data from the Firebase Database
    print("Acquiring the ECG and GSR values from the Firebase Database")
    timerfunc(5)
    
    #Assigning the name of the live data
    for key,value in result1.items():
        name=value
    
    #Creating a String literal to the Firebase address    
    res = "/"+name
    
    #Importing Firebase Library
    from firebase import firebase
    
    #Defining the object to interface with the forebase database
    firebase = firebase.FirebaseApplication('https://mental-health-eaf75.firebaseio.com/', None) 
    
    #Creating a concatenated String literal for the firebase address
    result = firebase.get(res, '')  
    #print(result)  
    
    #Creating the List derived from the database
    temp = []
    result_list = []
    for key , value in result.items():
        temp = [key, value]
        result_list.append(temp[1])
        
    #print(result_list)
        
    
    
    print("IMPLEMENTATING REGRESSION ALGORITHM")
    parameter = result_list
    
    #Calling the Regression Script
    regression(parameter)
    
    
    
    
    
