# Python MinMax Application Code
# Author: Bedemariam Degef
# Date; January 19, 2019
# This file calculates the minimum and maximum numbers from a userinput 

import sys  

print("***********************************************************************")

 
print("Welcome to the Python MinMax Application!")
print("This application calculates the minimum and maximum of 5 integer", 
       "values entered by a user. \n")

#Prompt the user to enter the five integers
num1=input("Enter your first integer:")
num2=input("Enter your second integer:")
num3=input("Enter your third integer:")
num4=input("Enter your fouth integer:")
num5=input("Enter your fifth integer:")

#Get the minimum value
minimum=min(int(num1),int(num2),int(num3),int(num4),int(num5))

#Get the maximum value
maximum=max(int(num1),int(num2),int(num3),int(num4),int(num5))

#Print the minimum value
print("\nThe minimum integer entered was ", int(minimum))

#Print the minimum value
print("The maximum integer entered was ", int(maximum))

print("\nThanks for trying the Python MinMax application.")

print("***********************************************************************")

#End of the program 