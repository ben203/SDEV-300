# Python State Capital and Bird List Application Code
# Author: Bedemariam Degef
# Date; January 29, 2019
# This file generates  states' capital, flowers and birds name

import sys

print("**** Welcome to states' information generator *********")
 
#A list with all the states and their approprate information labled 

states=[ ["STATE:Alabama", "CAPITAL:Montgomery", "FLOWER:Camellia", 
          "BIRD:Northern flicker"],
         ["STATE:Alaska", "CAPITAL:Juneau", "FLOWER:Scorpion grasses", 
          "BIRD:Willow ptarmigan"],
         ["STATE:Arizona", "CAPITAL:Phoenix", "FLOWER:Saguaro", 
          "BIRD:Cactus wren"],
         ["STATE:Arkansas", "CAPITAL:Little Rock", "FLOWER:Apple Blossom", 
          "BIRD:Northern mockingbird"],
         ["STATE:California", "CAPITAL:Sacramento", "FLOWER:California poppy", 
         "BIRD:California quail"],
         ["STATE:Colorado", "CAPITAL:Denver", "FLOWER:Colorado blue columbine", 
         "BIRD:Lark bunting"],
         ["STATE:Connecticut", "CAPITAL:Hartford", "FLOWER:Mountain-laurel", 
         "BIRD:American robin"],
         ["STATE:Delaware", "CAPITAL:Dover", "FLOWER:Peach Blossom",
         "BIRD:Delaware Blue Hen"],
         ["STATE:Florida", "CAPITAL:Tallahassee", "FLOWER:Orange blossom", 
         "BIRD:Northern mockingbird"],
         ["STATE:Georgia", "CAPITAL:Atlanta", "FLOWER:Rosa laevigata", 
         "BIRD:Brown thrasher"],
         ["STATE:Hawaii", "CAPITAL:Honolulu", "FLOWER:Yellow hibiscus", 
         "BIRD:Nene"],
         ["STATE:Idaho", "CAPITAL:Boise", "FLOWER:Syringa", 
         "BIRD:Delaware Blue Mountain bluebird"],
         ["STATE:Illinois", "CAPITAL:Springfield", "FLOWER:Viola", 
         "BIRD:Northern cardinal"],
         ["STATE:Indiana", "CAPITAL:Indianapolis", "FLOWER:Peony", 
         "BIRD:Cardinal"],
         ["STATE:Iowa", "CAPITAL:Des MoinToes", "FLOWER:Prairie rose", 
         "BIRD:American robin"],
         ["STATE:Kansas", "CAPITAL:Topeka", "FLOWER:Wild Sunflower", 
         "BIRD:Western meadowlark"],
         ["STATE:Kentucky", "CAPITAL:Frankfort", "FLOWER:Solidago", 
         "BIRD:American Goldfinch"],
         ["STATE:Louisiana", "CAPITAL:Baton Rouge", "FLOWER:Magnolia", 
         "BIRD:Brown pelican"],
         ["STATE:Maine", "CAPITAL:Augusta", "FLOWER:White Pine Cone", 
         "BIRD:Black-capped chickadee"],
         ["STATE:Maryland", "CAPITAL:Annapolis", "FLOWER:Black-eyed Susan", 
         "BIRD:Baltimore oriole"],
         ["STATE:Massachusetts", "CAPITAL:Boston", "FLOWER:Trailing arbutus", 
         "BIRD:WBlack-capped chickadee"],
         ["STATE:Michigan", "CAPITAL:Lansing", "FLOWER:Apple Blossom",
         "BIRD:American robin"],
         ["STATE:Minnesota", "CAPITAL:Saint Paul", "FLOWER:Showy lady's slippers",
         "BIRD:Common loon"],
         ["STATE:Mississippi", "CAPITAL:Jackson", "FLOWER:Magnolia", 
         "BIRD:Wood duck"],
         ["STATE:Missouri", "CAPITAL:Jefferson City", "FLOWER:Crataegus punctata", 
         "BIRD:Eastern bluebird"],
         ["STATE:Montana", "CAPITAL:Helena", "FLOWER:Bitterroot", 
         "BIRD:Western meadowlark"],
         ["STATE:Nebraska", "CAPITAL:Lincoln", "FLOWER:Solidago", 
         "BIRD:Western meadowlark"],
         ["STATE:Nevada", "CAPITAL:Big sagebrush", "FLOWER:Yellow hibiscus", 
         "BIRD:Mountain bluebird"],
         ["STATE:New Hampshire", "CAPITAL:Concord", "FLOWER:Purple lilac", 
         "BIRD:Purple finch"],
         ["STATE:New Jersey", "CAPITAL:Trenton", "FLOWER:Common blue violet", 
         "BIRD:American Goldfinch"],
         ["STATE:New Mexico", "CAPITAL:Santa Fe", "FLOWER:Yucca flower", 
         "BIRD:Greater roadrunner"],
         ["STATE:New York", "CAPITAL:Albany", "FLOWER:Rose", 
         "BIRD:Eastern bluebird"],
         ["STATE:North Carolina", "CAPITAL:Raleigh", "FLOWER:Flowering dogwood", 
         "BIRD:Cardinal"],
         ["STATE:North Dakota ", "CAPITAL:Bismarck", "FLOWER:Prairie rose", 
         "BIRD:Western meadowlark"],
         ["STATE:Ohio", "CAPITAL:Columbus", "FLOWER:Carnation",
         "BIRD:Northern cardinal"],
         ["STATE:Oklahoma", "CAPITAL:Oklahoma City", "FLOWER:Rosa 'Oklahoma'", 
         "BIRD:Scissor-tailed flycatcher"],
         ["STATE:Oregon", "CAPITAL:Salem", "FLOWER:Oregon Grape", 
         "BIRD:Western meadowlark"],
         ["STATE:Pennsylvania", "CAPITAL:Harrisburg", "FLOWER:Mountain-laurel", 
         "BIRD:Ruffed grouse"],
         ["STATE:Rhode Island", "CAPITAL:Common blue violet", "FLOWER:Magnolia", 
         "BIRD:Rhode Island Red"],
         ["STATE:South Carolina", "CAPITAL:Columbia", "FLOWER:Yellow jessamine", 
         "BIRD:Carolina wren"],
         ["STATE:South Dakota", "CAPITAL:Pierre", "FLOWER:American Pasque flower", 
         "BIRD:Ring-necked Pheasant"],
         ["STATE:Tennessee", "CAPITAL:Nashville", "FLOWER:Irises", 
         "BIRD:Northern mockingbird"],
         ["STATE:Texas", "CAPITAL:Austin", "FLOWER:Bluebonnet", 
         "BIRD:Northern mockingbird"],
         ["STATE:Utah", "CAPITAL:Salt Lake City", "FLOWER:Sego lily", 
         "BIRD:California gull"],
         ["STATE:Vermont", "CAPITAL:Montpelier", "FLOWER:Red Clover", 
         "BIRD:Hermit thrush"],
         ["STATE:Virginia", "CAPITAL:Richmond", "FLOWER:Flowering dogwood", 
         "BIRD:Cardinal"],
         ["STATE:Washington", "CAPITAL:Olympia", "FLOWER:Pacific rhododendron", 
         "BIRD:American Goldfinch"],
         ["STATE:West Virginia", "CAPITAL:Charleston", "FLOWER:Rhododendron", 
         "BIRD:Northern cardinal"],
         ["STATE:Wisconsin", "CAPITAL:Madison", "FLOWER:Common blue violet", 
         "BIRD:American robin"],
         ["STATE:Wyoming", "CAPITAL:Cheyenne", "FLOWER:Wyoming Indian paintbrush", 
         "BIRD:Western meadowlark"],
         
         ]
         
         
#Sentinel value for the while loop  
cont=True       
         
while  cont:
 try:
    print("\n1.Display all U.S. States in Alphabetical order", 
                            " along with Capital and Flower")

    print("2.Search for a specific state and display", 
                            "the appropriate Capital and Bird")
 
    print("3.Update a Bird for a specific state") 

    print("4. Exit the program") 
    
    #Store the userinput  
    user_feedback=int(input(""))
    
    #If the selection is 1 
    if(user_feedback==1):
        #sort the list 
        states.sort()
        
        #For each loop to print all 50 states with their capital and flower name
        for i in range(0, 50):
            for j in range(0, 3):
                print(states[i][j], end=" ")
            print()  
            print() 
            
     #If the selection is 2        
    if(user_feedback==2):
        print("what is the state you want to display the capital and bird name") 
        
        #Store the userinput
        state_to_find=input("")
        
        #Lower case every thing and capitalize the first letters to match the list 
        state_to_find=state_to_find.lower()
        state_to_find=state_to_find.title()
        
        
        found=False    
                      
        for i in range(0, 50):
            
            #If user input matches a name of a state print the capital 
            #and bird name
            if(states[i][0]=="STATE:"+state_to_find):  
               print(states[i][1],states[i][3])
               
               #Change found to true
               found=True
               
        #Display the appropriate message if userinput doesn't match any state       
        if(found==False):
            print(state_to_find," is not a state")
     
    #If the selection is 3        
    if(user_feedback==3):
        
        print("which state's bird do you want to update") 
        
        #Store user input
        state_to_update=input("")

        
        found=False 
               
        for i in range(0, 50):
            
            #If a name of a state matches user input update the bird name
            if(states[i][0]=="STATE:"+state_to_update):  
              
                
                #Change found to true
                found=True 
                
                print("what do you want to name it") 
        
                #Store user input
                bird_name=input("")
                
                #Update the name of the bird
                states[i][3]="BIRD:"+bird_name
                
                print("The name has been changed now it reads ",states[i][3])
                
        #Display the appropriate message if userinput doesn't match any state       
        if(found==False):
             print(state_to_update," is not a state")
     
     #If user input is 4    
    if(user_feedback==4):    
        cont=False #Ends the loop
        
        print("Thanks for trying states' information generator Application.")
        print("*********************************************************")
        
    #Throw an exception for a wrong userinput
    if(user_feedback < 1 or user_feedback > 6): 
        raise ValueError() 

 #Catch the exception for invalid inputs        
 except ValueError as err:  
     print("\nPlease enter an integer between 1 and 6 to make your selection") 
 