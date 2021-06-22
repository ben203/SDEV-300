# Python Calculator Application Code
# Author: Bedemariam Degef
# Date; January 19, 2019
# This file calculates numbers entered by the user

import sys

print("Welcome to the Python Calculator Application. \n")                       
print("What calculation do you want to perform? \n")

#Print the options
print("1) Addition (+)")
print("2) Subtraction (-)")
print("3) Division (/)")
print("4) Multiplication (*)")
print("5) Modulus (%)")

#Prompt the user to enter the selection 
selection=int(input("Enter 1,2,3,4 or 5 indicating your selection.\n"))

#Inform the user the selected option 
if (selection==1):

    print("\nAddition selected\n")
    
if (selection==2):

    print("\nSubtraction selected\n")
    
if(selection==3):

    print("\nDivision selected\n")
    
if(selection==4):

    print("\nMultiplication selected\n")
 
if(selection==5):

    print("\nModulus selected\n")
    
    
#Get the first integer
num1=input("Enter your first integer: \n")

#Get the second integer
num2=input("Enter your second integer: \n")

#Addition performed
if (selection==1): 
    
    print("\nThe addition of ",num1," and ",num2," is ",int(num1)+int(num2),"\n")
    
#Substraction performed    
if (selection)==2:
    
    print("\nThe difference of ",num1," and ",num2," is ",int(num1)-int(num2),"\n")
    
#Division performed  
if (selection)==3 and int(num2)!=0:
    
    print("\nThe division of ",num1," over ",num2," is " ,int(num1)/int(num2),"\n")
      
#Tell the user they can't divide by zero
if (selection)==3 and int(num2)==0:
    
    print("\ndivision by zero is not allowed \n")
    
#Multiplication performed     
if (selection)==4:
    
   print("\nThe multiplication of ",num1," and ",num2," is ",int(num1)*int(num2),"\n")
   
#Substraction performed  
if (selection)==5:
    
    print("\nThe modulus of ",num1," mod ",num2," is ",int(num1)%int(num2),"\n")

 

print("Thanks for trying the Python calculator \n")
print("**********************************************************************")

#End of the program 