# Python Data Application Code
# Author: Bedemariam Degef
# Date; February 9, 2019
# Edits a data from an array and print it in a correct format


import pandas as pd
import re

#The data that is going to be manipulated 
data=[
        ['John' , 'Joy', '21801','555-555-5555'],
        ['Jim' , 'Robertson', '223211143','4444444444'],
        ['John' , 'Adams', 'edskd-2134','323232'],
        ['Helen' , 'Cooper', '234511','323-333-2211'],
        ['Franklin' , 'Robert', '33014','BA'],
        ['Liam' , 'Jason', '33511','201-555-3592'],
        ['Noah' , 'Benjamin', '55330','299-911-4321'],
        ['William' , 'Michael', '33311','255-333-5433'],
        ['James' , 'Christopher', '33024','280-932030-2222'],
        ['Oliver' , 'Jason', '33030','277-855-4242'],
        ['' , '', '32211','250-665-4241'],
        ['Benjamin' , 'James', '55021','55234225-555-2342'],
        ['Elijah' , 'Matthew', '43215','2552345555'],
        ['Lucas' , 'Robertson', '20011','301-985-5555'],
        ['Mason' , 'Joshua', '$@#$#$','307-509-5555'],
        ['Loagn' , 'Luke', '$','309-49348-5555'],
        ['Emma' , 'Paul', '','300-432-5555'],
        ['Olivia' , 'John', '%','260-445-5555'],
        ['Ava' , 'Robert', '218032321','2403045555'],
        ['Isabella' , 'Joseph', '2183232301','3303845555'],
        ['Sophia' , 'Daniel', '2133333801','5555555555'],
        ['Charlotte' , 'Brian', '21811101','40055555'],
        ['Mia' , 'Justin', '2312399999','944-555-2386'],
        ['Amelia' , 'William', '90498-0048','5!@#'],
        ['Harper' , 'Ryan', '20032','555AC'],
        ['Evelyn' , 'Nicholas', '10H11','5003489'],
        ['Elizabeth' , 'Eric', '30303',''],
        ['Avery' , 'Andrew', 'sfdfsf','5012938471'],
        ['Ella' , 'Jeremy', 'sdfsfdd','4103934722'],
        ['Madison' , 'Timothy', '30331','404-55555'],
        ['Scarlett' , 'Kevin', '21043','733-555'],
        ['Victoria' , 'Thomas', '21215394827','701234255555'],
        ['Aria' , 'Richard', '44304','330-555-5555'],
        ['Isabella' , 'Jeffrey', '30004','799&'],
        ['Abigail' , 'Steven', '11230','899-555-5555'],
        ['Harper' , 'Mark', '14202','901-555-5555'],
        ]
        
        
        
#A phone pattern of ten digits ##########        
phone_pattern1 = re.compile("^[0-9]{10}$")

#A phone pattern of ten digits with dashes separation ###-###-####   
phone_pattern2 = re.compile("(\d{3})([-])(\d{3})([-])(\d{4})")

#A five digit zipcode with ##### pattern
zipcode_patern1=re.compile("^[0-9]{5}$")

#A nine digit zipcode with #####-#### pattern 
zipcode_patern2=re.compile("(\d{5})([-])(\d{4})")

#A nine digit zipcode with ######### pattern 
zipcode_patern3=re.compile("^[0-9]{9}$")

#A function that will return the right format of phonenumber     
def get_formatted_phone(value):
   
    if(not(phone_pattern1.match(value) or phone_pattern2.match(value)) ):
        return ""
        
    elif(phone_pattern2.match(value)):
        return value
        
    else:
        
        result = re.fullmatch(re.compile("(\d{3})(\d{3})(\d{4})"),   value)
        return '-'.join(result.groups()) if   result else value
        
#A function that will return the right format of zipcode      
def get_formatted_zipcode(value):  
    
    if(zipcode_patern1.match(value) or zipcode_patern2.match(value)):
        return value
        
    elif(zipcode_patern3.match(value)):
    
        result = re.fullmatch(re.compile("(\d{5})(\d{4})"),   value)
        return '-'.join(result.groups()) if   result else result
    else:
        return ""
        
    
    
#Creating the title lable for each columns
df= pd.DataFrame(data, columns=['First Name', 'Last Name', 'Zipcode','Phone'])

#Store the right format of phone number 
formatted_phone = df['Phone'].map(get_formatted_phone)

#Store the right format of zipcode 
formatted_zipcode = df['Zipcode'].map(get_formatted_zipcode)

#Formating the phone column to only print the correct format 
df['Phone']=formatted_phone

#Formating the zipcode column to only print the correct format
df['Zipcode']=formatted_zipcode

#Printing the data frame 
print(df)
 
 