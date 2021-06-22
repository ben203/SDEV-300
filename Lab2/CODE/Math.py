# Python Math application 
# Author: Bedemariam Degef
# Date; January 24, 2019
# This file genrates x and f(x) values

import math 
 
#A custom function that can create a range with float values  
def range(start,end,jump):
    while start <= end:
         yield start
         start+=jump
        

#Generate x and sin(x) for x values between (-2PI,2PI) with PI/64 increments       
def sin():
    
    #Generate x values
    x_vals=range(-2*(math.pi),2*(math.pi),(math.pi)/64)
    
    #prints x and sin(x) values
    for x in x_vals:
        print(x, "              ", math.sin(x))
        
#Generate x and cos(x) for x values between (-2PI,2PI) with PI/64 increments         
def cos():
    
    #Generate x values
    x_vals=range(-2*(math.pi),2*(math.pi),(math.pi)/64)
    
    #prints x and sin(x) values
    for x in x_vals:
        print(x, "             ", math.cos(x))
        
#Generate x and sqrt(x) for x values between (0,200) with 0.5 increments 
def sqrt():
    
    #Generate x values
    x_vals=range(0,200,0.5)
    
    #prints the x and sqrt(x) values
    for x in x_vals:
        print(x, "             ",math.sqrt(x))
        
#Generate x and log10(x) for x values between (1,200) with 0.5 increments         
def log10():
    
    #Generate x values that starts from 1 since log10(0) is undefined 
    x_vals=range(1,200,0.5)
    
    #prints the x and log10(x) values
    for x in x_vals:
        print(x, "             ",math.log10(x))
         
print("sin(X) function between (-2pi,2pi) increment by pi/64")   
sin()

print("\n\n\n cos(X) function between (-2pi,2pi) increment by pi/64")  
cos()
  
print("\n\n\nsqrt(x) function between (0,200) increment by 0.5")  
sqrt()

print("\n\n\nlog10(x) function between (0,200) increment by 0.5")  
log10()
     
       
  
 