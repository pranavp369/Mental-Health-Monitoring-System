# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:08:02 2020

@author: pranav
"""

#Importing the Libraries
import xlrd
import time
from DataAcquisition import dataacq

def dataupload():
    #Initializing the necessary lists
    parameter = {}
    ctr=1
    
    #Setting iup a timer function
    def timerfunc(t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            #print(timeformat, end='\r')
            time.sleep(1)
            t -= 1
            #Calling excelread function
            #if t == 0:
               # excelread(ctr+1)
    
    #Defining the excelread function to read the relay vallues
    def excelread(ctr):
        
        #Reading the Live Relay values from the Excel file
        #Locating the Excel file
        loc = ("D:\Main Project -Emotion Analysis using Physiological Signals\Dataset\Live-Data-Relay.xlsx") 
    
        #Opening the Workbook
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0)
    
        #Copying the values onto the variables
        j=ctr+1
        ecg1 = sheet.cell_value(j, 1)
        ecg2 = sheet.cell_value(j, 2)
        gsr =  sheet.cell_value(j, 3)
        
        #Creating a dictionary to store the values
        parameter = {'ECGL':ecg1, 'ECGR':ecg2, 'GSR':gsr}
            
        #print(parameter)
        
        
        #Calling the FirebaseUpload function
        uploadtofirebase(parameter)
        
        #Emptying the parameter
        parameter.clear()
     
    
    #Defining the function to upload data to firebase
    def uploadtofirebase(parameter):
        #Importing firebase library
        from firebase import firebase  
        
        #Defining the object to interface with the forebase database
        firebase = firebase.FirebaseApplication('https://mental-health-eaf75.firebaseio.com/', None)  
       
        #Uploading the Values to the Firebase database
        result = firebase.post('/',parameter)  
        #print(result)
        
        #Calling the Data Acquisitiion function
        dataacq(result)
        
        #Calling the Timer Function
        timerfunc(30)



    #Calling the excelread function initially
    excelread(ctr)  





if __name__ == '__main__':
    dataupload()
