# Python Data Analysis Code
# Author: Bedemariam Degef
# Date; February 15, 2020
# Allows a user to load one of two CSV files and perform data analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 

#Read the csv file for population change 
file1=pd.read_csv(os.path.join(os.path.dirname(__file__), "../Lab5/PopChange.csv"))

#Store the population data in the dataframe
df1= pd.DataFrame(file1)

#Read the csv file for housing
file2=pd.read_csv(os.path.join(os.path.dirname(__file__), "../Lab5/Housing.csv"))

#Store the housing data in the dataframe
df2= pd.DataFrame(file2)


#A class to get column data of April's population from Popchange.cvs 
class PopAprilOne:
    
    def count(self):
        return df1.shape[0]
        
    def mean(self):
        return np.mean(df1['Pop Apr 1'])
        
    def standard_deviation(self):
        return np.std(df1['Pop Apr 1'])
    
    def minimum(self):
        return np.min((df1['Pop Apr 1']))
        
    def maximum(self):
        return np.max((df1['Pop Apr 1']))

#A class to get column data of July's population from Popchange.cvs        
class PopJulyOne:
    
    def count(self):
        return df1.shape[0]
        
    def mean(self):
        return np.mean(df1['Pop Jul 1'])
        
    def standard_deviation(self):
        return np.std(df1['Pop Jul 1'])
    
    def minimum(self):
        return np.min((df1['Pop Jul 1']))
        
    def maximum(self):
        return np.max((df1['Pop Jul 1']))

#A class to get column data of change in population from Popchange.cvs         
class ChangePop:
    
    def count(self):
        return df1.shape[0]
        
    def mean(self):
        return np.mean(df1['Change Pop'])
        
    def standard_deviation(self):
        return np.std(df1['Change Pop'])
    
    def minimum(self):
        return np.min((df1['Change Pop']))
        
    def maximum(self):
        return np.max((df1['Change Pop']))

#A class to get column data of AGE from Housing.cvs        
class Age:
    
    def count(self):
        return df2.shape[0]
        
    def mean(self):
        return np.mean(df2['AGE'])
        
    def standard_deviation(self):
        return np.std(df2['AGE'])
    
    def minimum(self):
        return np.min((df2['AGE']))
        
    def maximum(self):
        return np.max((df2['AGE']))

#A class to get BEDRMS data of AGE from Housing.cvs        
class Bedrms:
    
    def count(self):
        return df2.shape[0]
        
    def mean(self):
        return np.mean(df2['BEDRMS'])
        
    def standard_deviation(self):
        return np.std(df2['BEDRMS'])
    
    def minimum(self):
        return np.min((df2['BEDRMS']))
        
    def maximum(self):
        return np.max((df2['BEDRMS']))

#A class to get column data of BUILT from Housing.cvs        
class Built:
    
    def count(self):
        return df2.shape[0]
        
    def mean(self):
        return np.mean(df2['BUILT'])
        
    def standard_deviation(self):
        return np.std(df2['BUILT'])
    
    def minimum(self):
        return np.min((df2['BUILT']))
        
    def maximum(self):
        return np.max((df2['BUILT']))

#A class to get column data of ROOMS from Housing.cvs        
class Rooms:
    
    def count(self):
        return df2.shape[0]
        
    def mean(self):
        return np.mean(df2['ROOMS'])
        
    def standard_deviation(self):
        return np.std(df2['ROOMS'])
    
    def minimum(self):
        return np.min((df2['ROOMS']))
        
    def maximum(self):
        return np.max((df2['ROOMS']))

#A class to get column data of UTILITY from Housing.cvs        
class Utility:
    
    def count(self):
        return df2.shape[0]
        
    def mean(self):
        return np.mean(df2['UTILITY'])
        
    def standard_deviation(self):
        return np.std(df2['UTILITY'])
    
    def minimum(self):
        return np.min((df2['UTILITY']))
        
    def maximum(self):
        return np.max((df2['UTILITY']))
        
        
 
   
 
print("***************** Welcome to the Python Data Analysis App**********\n")

#Sentinel value for the outer while loop  
cont=True
 
#The start of the outer while loop 
while(cont):

    print("Select the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")
    
    #User input to select a file or exit the program
    user_slection=input()
    
    #If Population Data selected
    if (user_slection=="1"):
        print("You have entered Population Data.\n")
        print("Select the Column you want to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")
        
        #Sentinel value for the inner while loop
        keep_looping=True
        
        #The start of the inner while loop
        while(keep_looping):
            
            #User input to select or exit the column
            user_input=input()
     
            #If Pop Apr 1 is selected
            if(user_input=="a"):
                
                #Creating an object from the column class   
                p=PopAprilOne()
                
                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",p.count())
                print("Mean = ", np.around(p.mean(),2))
                print("Standard Deviation = ",np.around(p.standard_deviation(),2))   
                print("Min = ",p.minimum())
                print("Max = ",p.maximum())
                
                #Graph title
                plt.title('Pop Apr 1')

                #Build the histogram  
                plt.hist(df1['Pop Apr 1'],10,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig1=plt
                # Save Figure for Download 
                fig1.savefig('Pop Apr 1.svg')
                            
                 
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")
                print("a. Pop Apr 1")
                print("b. Pop Jul 1")
                print("c. Change Pop")
                print("d. Exit Column\n")
                
            #Else if Pop Jul 1 selected    
            elif(user_input=="b"):
                
                #Creating an object from the column class  
                p=PopJulyOne()
                
                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("\nCount = ",p.count())
                print("Mean = ", np.around(p.mean(),2))
                print("Standard Deviation = ",np.around(p.standard_deviation(),2))   
                print("Min = ",p.minimum())
                print("Max = ",p.maximum())
                
                #Graph title
                plt.title('Pop Jul 1')
                
                #Graph labels
                plt.xlabel('Column Data')
                plt.ylabel('Column Count')
                plt.title('Pop Jul 1')

                #Build the histogram  
                plt.hist(df1['Pop Jul 1'],10,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig2=plt
                # Save Figure for Download 
                fig2.savefig('Pop Jul 1.svg')
                
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")
                print("a. Pop Apr 1")
                print("b. Pop Jul 1")
                print("c. Change Pop")
                print("d. Exit Column")
            
            #Else if Change Pop is selected
            elif(user_input=="c"):
                 
                #Creating an object from the column class   
                p=ChangePop()

                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",p.count())
                print("Mean = ", np.around(p.mean(),2))
                print("Standard Deviation = ",np.around(p.standard_deviation(),2))   
                print("Min = ",p.minimum())
                print("Max = ",p.maximum())
                
                #Graph title
                plt.title('Change Pop')
                
                #Build the histogram  
                plt.hist(df1['Change Pop'],10,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig3=plt
                # Save Figure for Download 
                fig3.savefig('Change Pop.svg')
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")
                print("a. Pop Apr 1")
                print("b. Pop Jul 1")
                print("c. Change Pop")
                print("d. Exit Column")
            
            #Else if Exit Column is selected
            elif(user_input=="d"):
                print("You selected to exit the column menu")
                keep_looping=False
            
            #Otherwise give the user a chance until a valid input is entered 
            else:
                print("\nPlease enter between a-d to make your selection\n")
                print("Select the Column you want to analyze:")
                print("a. Pop Apr 1")
                print("b. Pop Jul 1")
                print("c. Change Pop")
                print("d. Exit Column")
        

    #Else if Housing Data selected 
    elif(user_slection=="2"):
        print("You have entered Housing Data.\n")
        print("Select the Column you want to analyze:")     
        print("a. AGE ")
        print("b. BEDRMS ")
        print("c. BUILT ")
        print("d. ROOMS ")
        print("e. UTILITY ")
        print("f. Exit Column")
        
        #Sentinel value for the inner while loop
        keep_iteraing=True
        
        #Start the inner loop
        while(keep_iteraing):
            
            #User input to select or exit the column
            u_input=input()
            
            #if AGE selected 
            if(u_input=="a"):
                
                #Creating an object from the column class  
                h=Age()

                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",h.count())
                print("Mean = ", np.around(h.mean(),2))
                print("Standard Deviation = ",np.around(h.standard_deviation(),2))  
                print("Min = ",h.minimum())
                print("Max = ",h.maximum())
                
                #Graph title
                plt.title('AGE')
                
                #Build the histogram  
                plt.hist(df2['AGE'],50,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig4=plt
                # Save Figure for Download 
                fig4.savefig('AGE.svg')
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")     
                print("a. AGE ")
                print("b. BEDRMS ")
                print("c. BUILT ")
                print("d. ROOMS ")
                print("e. UTILITY ")
                print("f. Exit Column")
                
            #Else if BEDRMS selected     
            elif(u_input=="b"):
                
                #Creating an object from the column class  
                h=Bedrms()
                
                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",h.count())
                print("Mean = ", np.around(h.mean(),2))
                print("Standard Deviation = ",np.around(h.standard_deviation(),2))  
                print("Min = ",h.minimum())
                print("Max = ",h.maximum())
                
                #Graph title
                plt.title('BEDRMS')
                
                #Build the histogram  
                plt.hist(df2['BEDRMS'],20,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig5=plt
                # Save Figure for Download 
                fig5.savefig('BEDRMS.svg')
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")     
                print("a. AGE ")
                print("b. BEDRMS ")
                print("c. BUILT ")
                print("d. ROOMS ")
                print("e. UTILITY ")
                print("f. Exit Column")
                
            #Else if BUILT selected     
            elif(u_input=="c"):
                
                #Creating an object from the column class  
                h=Built()

                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",h.count())
                print("Mean = ", np.around(h.mean(),2))
                print("Standard Deviation = ",np.around(h.standard_deviation(),2))  
                print("Min = ",h.minimum())
                print("Max = ",h.maximum())
                
                #Graph title
                plt.title('BUILT')
                
                #Build the histogram  
                plt.hist(df2['BUILT'],20,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig6=plt
                # Save Figure for Download 
                fig6.savefig('BUILT.svg')
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")     
                print("a. AGE ")
                print("b. BEDRMS ")
                print("c. BUILT ")
                print("d. ROOMS ")
                print("e. UTILITY ")
                print("f. Exit Column")
            
            #Else if ROOMS selected    
            elif(u_input=="d"):
                
                #Creating an object from the column class  
                h=Rooms()
            
                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",h.count())
                print("Mean = ", np.around(h.mean(),2))
                print("Standard Deviation = ",np.around(h.standard_deviation(),2))   
                print("Min = ",h.minimum())
                print("Max = ",h.maximum())
                
                #Graph title
                plt.title('ROOMS')
                
                #Build the histogram  
                plt.hist(df2['ROOMS'],20,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig7=plt
                # Save Figure for Download 
                fig7.savefig('ROOMS.svg')
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")     
                print("a. AGE ")
                print("b. BEDRMS ")
                print("c. BUILT ")
                print("d. ROOMS ")
                print("e. UTILITY ")
                print("f. Exit Column")
                
            #Else if UTILITY selected     
            elif(u_input=="e"):
                
                #Creating an object from the column class  
                h=Utility()
                
                #Generating Count, Mean, Standard, Deviation, Min, Max data from the column
                print("Count = ",h.count())
                print("Mean = ", np.around(h.mean(),2))
                print("Standard Deviation = ",np.around(h.standard_deviation(),2))  
                print("Min = ",h.minimum())
                print("Max = ",np.around(h.maximum(),2))
                
                #Graph title
                plt.title('UTILITY')
                
                #Build the histogram  
                plt.hist(df2['UTILITY'],50,color=['blue'])
                plt.grid(True)
                #Assign to a figure 
                fig8=plt 
                # Save Figure for Download 
                fig8.savefig('UTILITY.svg')
                
                
                print("\nThe Histogram of this column can be downloaded now.\n")
                
                print("Select the Column you want to analyze:")     
                print("a. AGE ")
                print("b. BEDRMS ")
                print("c. BUILT ")
                print("d. ROOMS ")
                print("e. UTILITY ")
                print("f. Exit Column")
            
            #Else if Exit Column is selected Exit Column      
            elif(u_input=="f"):
                
                keep_iteraing=False
                print("You selected to exit the column menu")
            
            #Otherwise give the user a chance until a valid input is entered     
            else:
                print("\nPlease enter between a-f to make your selection\n")
                print("Select the Column you want to analyze:")     
                print("a. AGE ")
                print("b. BEDRMS ")
                print("c. BUILT ")
                print("d. ROOMS ")
                print("e. UTILITY ")
                print("f. Exit Column ")
                
    #Else if Exit the Program is selected            
    elif (user_slection=="3"):
        cont=False
        
        print("***************Thanks for using the Data Analysis App**********")
        
    #Otherwise give the user a chance until a valid input is entered     
    else:
        print("\nPlease enter between 1-3 to make your selection\n")