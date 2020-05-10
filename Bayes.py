# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:52:52 2020

@author: pranav
"""

import numpy as np
import matplotlib as plt

#initializing the parameter
parameter = 0
sample_space = []
#Defining the Baysian Inference Function
def bayes(parameter):
    print("Bayesian Inference Engine Running...")    
    
    #Appending the parameter into the sample space
     sample_space.append(parameter)
    
    #Defining a function for probability
    def prob(A,B):
        probability = (A/B)*100
        
        return round(probability,1)
    
    
    
    
    
if __name__ == '__main__':
    bayes(parameter)
    