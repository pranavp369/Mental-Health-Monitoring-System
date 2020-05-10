# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:26:34 2020

@author: pranav
"""

import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#from DataUpload import dataupload

#initializing the parameter
parameter = 0
sample_space =[]
day = []
possibility = []
anxiety_list = []
anxiety_week = []
possibility_week =[]
parameter = []
result = []

#Defining the Baysian Inference Function
def infengine(parameter):
    print("Bayesian Inference Engine Running...")    
    
    #Defining a function for probability
    def prob(A,B):
        probability = (A/B)
        if probability == 0 :
            probability = 0.001
            
        return round(probability,3)    
    
    #Inference Rules
    #Defining rule function
    def rules(parameter):
        n = parameter[0] #Parameter for Neutral Probability
        a = parameter[1] #Parameter for Anger Probability
        d = parameter[2] #Parameter for Disgust Probability
        f = parameter[3] #Parameter for Fear Probability
        h = parameter[4] #Parameter for Happiness Probability
        x = parameter[5] #Parameter for Sadness Probability
        s = parameter[6] #Parameter for surprise Probability
        #Defining rulea
        def rulea(p):
            if p>=0.125:
                return 0
            else:
                return 1
        #Defining ruleb
        def ruleb(p,q):
            if (p+q)>=0.200:
                return 0
            else:
                return 1


        #Rule1 anger>0.125 -> Maybe Possible
        result.append(rulea(a))
        #Rule2 fear>0.125 -> Maybe Possible
        result.append(rulea(f))
        #Rule3 disgust>0.125 -> Maybe Possible
        result.append(rulea(d))
        #Rule4 sadness>0.125 -> Maybe Possible
        result.append(rulea(x))
        #rule5 surprise>0.125 -> Maybe Possible
        result.append(rulea(s))
        #rule6 surprise+fear>0.333 -> Maybe Possible
        result.append(ruleb(s,f))
        #rule7 fear+anger>0.333 -> Maybe Possible
        result.append(ruleb(f,a))
        #rule8 disgust+anger>0.333 -> Maybe Possible
        result.append(ruleb(d,a))
        #rule9 sadness+fear>0.333 -> Maybe Possible
        result.append(ruleb(x,f))
        
        #Calculating possibility of mental disorder
        possibility_result = prob(result.count(0),len(result))
        print(result)
        
        return possibility_result

    #Defining the Process function
    def processday(day,i):
        #Calculating the Probabilities
        p_neutral = prob(day.count(0), len(day))
        p_anger = prob(day.count(1), len(day))
        p_disgust = prob(day.count(2), len(day))
        p_fear = prob(day.count(3), len(day))
        p_joy = prob(day.count(4), len(day))
        p_sadness = prob(day.count(5), len(day))
        p_surprise = prob(day.count(6),len(day))
        
        #Storing the probabilities in a list
        param = [p_neutral,p_anger,p_disgust,p_fear,p_joy,p_sadness,p_surprise]
        print(param)
        #Calling the visual representation function
        print(i)
        if i != 7:
            pie(param)
        #Calling the rule function given the parameter of probabilities
        return rules(param)
    
    #Defining the Anxiety Parameter
    def anxiety(day):
        #Calculating the Probabilities
        p_neutral = prob(day.count(0), len(day))
        p_anger = prob(day.count(1), len(day))
        p_disgust = prob(day.count(2), len(day))
        p_fear = prob(day.count(3), len(day))
        p_joy = prob(day.count(4), len(day))
        p_sadness = prob(day.count(5), len(day))
        p_surprise = prob(day.count(6),len(day))
        
        #Calculating the anxiety parameter of the daily data
        AP = ((3*p_anger)*(8*p_fear)*(5*p_surprise))
        
        return round(AP,2)

    #Defining the function to calculate the parameters for a week
    def week(anxiety_week,possibility_week):
        #Calling the visualisation function for bar graphs for Anxiety
        bar(anxiety_week,'Anxiety')
        #Calling the visualisation function for bar graphs for Possibility
        bar(possibility_week,'Possibility of Mental Health Problems')
        
        
    #Visualizing the Data
    #Pie Chart
    def pie(para):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Neutral', 'Anger', 'Disgust', 'Fear','Happiness','Sadness','Surprise'
        sizes = [para[0]*100,para[1]*100,para[2]*100, para[3]*100,para[4]*100,para[5]*100,para[6]*100]
        
        
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Daily Report")
        plt.show()
        
    #Bar Graph
    def bar(par,name):
        objects = ('Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6','Day7')
        y_pos = np.arange(len(objects))
        #par = []
        #for i in param.items():
            #par.append(i) 
        performance = [par[0],par[1],par[2],par[3],par[4],par[5],par[6]]
        print()
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel(name)
        plt.title('Weekly Statistics')
        
        plt.show()
    
    #Starting Function  
    def start(parameter):
        #Appending the parameter into the sample space
        sample_space.append(parameter)
        
        #Seperating the data per day
        if len(sample_space)%48 == 0 :
            day.append(sample_space)
            i = int(len(sample_space)/48)-1
            #print(day)
            #Calling the Anxiety parameter function
            anxiety_list.append(anxiety(day[i])) #Updating the Anxiety parameter list
            
            #Calling the posssibility calculation function
            possibility.append(processday(day[i],len(anxiety_list)))
            #print(anxiety_list)
            #print(possibility)
            
            #Calling the week function
            if len(anxiety_list)%7 == 0 :
                anxiety_week.append(anxiety_list)
                possibility_week.append(possibility)
                #print(anxiety_week)
                #print(possibility_week)
                week(anxiety_list,possibility)
                   
        
    
    
    start(parameter)
    dataupload()
    
    
if __name__ == '__main__':
    infengine(parameter)
    
