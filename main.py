#Importing Libraries
from DataUpload import dataupload
import time


#Defining the main function
def main():   
    #Setting iup a timer function
    def timerfunc(t):
        b=4
        while t:
            mins, secs = divmod(t, 60)
            time.sleep(1)
            t -= 1
            a = ((t+1)-b)*20
            b=b-2
            print(a,"%", end='\r')
    
    #Starting the System
    print("Starting the psychAItrist System...")
    timerfunc(5)
    
    #Running the Regression Algorithm
    
    
    #Calling the UploadData to Firebase function
    print("Uploading the data to the Firebase Database...")
    timerfunc(5)
    dataupload()




if __name__ == '__main__':
    main()