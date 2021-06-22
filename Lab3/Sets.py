# Python Math Set Application Code
# Author: Bedemariam Degef
# Date; January 29, 2019
# This application Determine the union, intersection and difference of the  
# square and cube of integers ranging from 1 to 100

import sys

print("**** Welcome to a math application using sets*********")

#create a set to store the squared numbers 
square_set = set()

#create a set to store the cubed numbers 
cube_set = set()

#Add squared and cubed numbers from 1 to 100 to both setes
def square_and_cube_sets():
    for y in range(1,100):  
        square_set.add(y**2)
        cube_set.add(y**3)

#Print list of numbers to the power of the number being passed 
def power_function(x):
    for y in range(1,100):
        print(y**x) 

#Sentinel value for the while loop   
cont=True   
         
while  cont:
 try:
    print("\n1. Display the Square and Cube for Integers ranging from 1 to 100")
    print("2. Search the sets for a specific Integer and display the Square",
              "and Cube values")
    print("3. Display the Union of Square and Cube sets")
    print("4. Display the Intersection of Square and Cube sets")
    print("5. Display the Difference of Square and Cube sets")
    print("6. Exit the program")
    
    #Store the userinput  
    user_feedback=int(input(""))  
    
    #If the selection is 1 print the appropriate values
    if(user_feedback==1): 
        print("\nSquare Intergers 1 to 100 \n")
        power_function(2)
        
        print("\nCube Intergers 1 to 100 \n")
        power_function(3)
        
     #If the selection is 2 print the cube and square of the userinput if
     #found in the sets
    if(user_feedback==2):
        print("what is the number you want to search")
        num=int(input(""))
        
        #Add the appropriate numbes to the sets
        square_and_cube_sets()
        
        #check to see if input in the sets 
        if(num in square_set or num in cube_set): 
            print(num," is found in the set")
            print("The square of ",num," is ",num**2 )
            print("The cube of ",num," is ",num**3 )
        else:
            print("\n", num,"is not in either sets\n")
      
    #If the selection is 3  
    if(user_feedback==3):  
        
        #Add the appropriate numbes to the sets
        square_and_cube_sets()
        
        #Print the union of the sets
        print(square_set.union(cube_set))
    
    #If the selection is 4 
    if(user_feedback==4):
        
        #Add the appropriate numbes to the sets
        square_and_cube_sets()
        
        #Print the intersection of the sets
        print(square_set.intersection(cube_set)) 
    
    #If the selection is 5     
    if(user_feedback==5):
        
        #Add the appropriate numbes to the sets
        square_and_cube_sets() 
        
        #Print the diffrence of the sets 
        print(square_set.difference(cube_set)) 
    
    #If the selection is 6      
    if(user_feedback==6):
        cont=False #Ends the loop
        print("Thanks for trying this math Application.")
        print("*********************************************************")
        
    #Throw an exception for a wrong userinput
    if(user_feedback < 1 or user_feedback > 6): 
        raise ValueError() 

 #Catch the exception for invalid inputs        
 except ValueError as err:  
     print("\nPlease enter an integer between 1 and 6 to make your selection")