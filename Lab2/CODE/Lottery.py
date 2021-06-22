# Python lottery number generator Code
# Author: Bedemariam Degef
# Date; January 24, 2019
# This file genrates randum lottery numbers 

import sys
import random

print("**** Welcome to the Pick-3, Pick-4 lottery number generator *********")

#A variable that will break out of the loop when it is false 
cont=True

while cont:
    #Prompt the user to choose from the selections 
    print("Select from the following menu:")
    print("1. Generate 3-Digit Lottery number")
    print("2. Generate 4-Digit Lottery number") 
    print("3. Exit the Application")
 
    #Get the user input
    feedback=int(input(""))
 
    #Generates 3 random digits
    if(feedback==1):
        num1, num2, num3 = random.sample(range(0, 9), 3)
        print("You selected 1. The following 3-digit lottery number was generated:")
        print(num1,num2,num3)
    
    #Generates 4 random digits  
    if(feedback==2):
        num1, num2, num3,num4 = random.sample(range(0, 9), 4)
        print("You selected 2. The following 4-digit lottery number was generated:")
        print(num1,num2,num3,num4)
    
     #Breaks out of the loop   
    if(feedback==3):
        print("You selected 3.")
        print("Thanks for trying the Lottery Application.")
        print("*********************************************************")
        cont=False