# Python Matrix Application Code
# Author: Bedemariam Degef
# Date; February 9, 2019
# This file performs applications on  3x3 matrices 

import numpy as np
import re

print("************** Welcome to the Python Matrix Application***********")

 
#A helper function to add two matrices        
def matrix_adder(m1,m2):
    return np.add(m1,m2)
    
#A helper function to add subtract two matrices            
def matrix_subtractor(m1,m2):
    return np.subtract(m1,m2)

#A helper function to multiply two matrices         
def matrix_multiplier(m1,m2):
    return np.matmul(m1,m2)
    
#A helper function to multiply by elements of two matrices 
def matrix_multi_by_elem(m1,m2):
    return np.multiply(m1,m2)
 
    
#Sentinel value for the while loop  
cont=True  

#While is cont is true 
while  cont:
 try: 
    print("Do you want to play the Matrix Game?")
    print("Enter Y for Yes or N for No:")
    
    #Get the user response 
    user_feedback=input("")
    
    #Check for invalid input 
    if(user_feedback is not "Y" and user_feedback is not "N"):
        print("Please enter only Y to play or N to quit no other input is valid")
        user_feedback=input("")
    
    #Check if the user wants to end the game    
    if(user_feedback is  "N"):
        cont=False
        print("*************** Thanks for playing the Matrix Game **********")
    
    #If the user wants to play    
    if(user_feedback=="Y"):
     
        print("Enter your first 3x3 matrix:")
        
        #Get the matrix inputs, exception is caught for invalid inputs
        a,b,c=map(float,input().split())
        e,f,g=map(float,input().split())
        h,i,j=map(float,input().split())
         
        #Convert and store the matrix inputs 
        matrix1=np.array([[a,b,c],[e,f,g],[h,i,j]])  
  
        print("Your first 3x3 matrix is:")
        print(matrix1)
  
        print("Enter your second 3x3 matrix:")
         
        #Get the matrix inputs, exception is caught for invalid inputs 
        a,b,c=map(float,input().split())
        e,f,g=map(float,input().split())
        h,i,j=map(float,input().split())
            
        #Convert and store the matrix inputs     
        matrix2=np.array([[a,b,c],[e,f,g],[h,i,j]])  
  
        print("Your second 3x3 matrix is:")
        print(matrix2)
  
        print("Select a Matrix Operation from the list below:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Matrix Multiplication")
        print("d. Element by element multiplication")
        
        user_slection=input("")
         
        #If Addition is selected 
        if (user_slection=="a"):
            
            #Add the two matrices and store it in m
            m=matrix_adder(matrix1,matrix2)
            
            print("You selected Addition. The results are:")
            print(m)
    
            print("The Transpose is:")
            print(m.T)
            
            print("The row and column mean values of the results are:")
            
            #Get the row mean value and store it in r to print 
            r=np.mean(m, axis = 1)
            print("Row: ",r[0]," , ",r[1]," , ",r[2])
   
            #Get the column mean value and store it in r to print 
            c=np.mean(m, axis = 0)
            print("Column: ",c[0]," , ",c[1]," , ",c[2])
   
        #If subtraction is selected 
        if (user_slection=="b"):
         
            #Subtract the two matrices and store it in m
            m=matrix_subtractor(matrix1,matrix2)
            print("You selected Subtraction. The results are:")
            print(m)
   
            print("The Transpose is:")
            print(m.T)
            
            print("The row and column mean values of the results are:")
            
            #Get the row mean value and store it in r to print 
            r=np.mean(m, axis = 1)
            print("Row: ",r[0]," , ",r[1]," , ",r[2])
            
            #Get the column mean value and store it in r to print 
            c=np.mean(m, axis = 0)
            print("Column: ",c[0]," , ",c[1]," , ",c[2])
        
        #If multiplication is selected
        if (user_slection=="c"):
         
            #Multiply the two matrices and store it in m
            m=matrix_multiplier(matrix1,matrix2)
            
            print("You selected Matrix Multiplication. The results are:")
            print(m)
   
            print("The Transpose is:")
            print(m.T)
            
            print("The row and column mean values of the results are:")
            
            #Get the row mean value and store it in r to print 
            r=np.mean(m, axis = 1)
            print("Row: ",r[0]," , ",r[1]," , ",r[2])
            
            #Get the column mean value and store it in r to print 
            c=np.mean(m, axis = 0)
            print("Column: ",c[0]," , ",c[1]," , ",c[2])
        
        #If multiplication by elements is selected
        if (user_slection=="d"):
            
            #Multiply the two matrices by elements and store it in m
            m=matrix_multi_by_elem(matrix1,matrix2)
            
            print("You selected Element by element multiplication. The results are:")
            print(m)
   
            print("The Transpose is:")
            print(m.T)
            
            print("The row and column mean values of the results are:")
            
            #Get the row mean value and store it in r to print 
            r=np.mean(m, axis = 1)
            print("Row: ",r[0]," , ",r[1]," , ",r[2])
            
            #Get the column mean value and store it in r to print 
            c=np.mean(m, axis = 0)
            print("Column: ",c[0]," , ",c[1]," , ",c[2])
        
        #Create a patern to a-d   
        pattern = re.compile('[a-d]+')
        
        #If user didn't enter a-d to make selection 
        if (not(pattern.match(user_slection))):
         
            print("Please make sure to make your selection", 
                     "by entering lower case a-d letters")
 
 #The except block   
 except ValueError as err:
      
     #Prints why an error occurred 
     print(err, "\n")
     
     #Tells the user to enter valid inputs
     print("Please enter a valid integer value")
  
  