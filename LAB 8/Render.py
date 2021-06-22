from flask import Flask, render_template, redirect, url_for, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pandas as pd ,flask,time,logging,datetime
from ip2geotools.databases.noncommercial import DbIpCity


app = Flask(__name__)

#Limiter object to limit failed logins 
limiter = Limiter(app, key_func=get_remote_address)

#Data frame for username and password logins 
df1=pd.read_csv("/home/ec2-user/environment/Lab8/u_p.csv") 

#Data frame for common used passwords 
df2=pd.read_csv("/home/ec2-user/environment/Lab8/common_passwords.csv") 

#True if commonly used password found
commonly_found_passwords=False

#True if password is < 8
less_than_8=False

#True if password is > 64
greater_than_64=False

#Number of failed logins
num_of_failed_logins=0 

#IP address of over 15 login fail attempts 
login_failed_ip=0

#Session start 
now = time.time()

#Time after five minutes(used if failed logins > 10 in less than 5 minutes)
after_five_minutes = now + 300
 


@app.route('/login', methods=['GET', 'POST'])

#Limit upto 15 login attempt 
@limiter.limit('15 per day') 

#The login page
def login():
    
    #Refering to the global variables 
    global num_of_failed_logins 
    global commonly_found_passwords 
    global less_than_8
    global greater_than_64
    global login_failed_ip
    
    #Error for failed logins 
    login_error = None
    login_failed=False
     
    #Reset at a local level for multiple use 
    less_than_8=False
    greater_than_64=False
    commonly_found_passwords=False
 
    
  
    #When Submit is clicked       
    if request.method == 'POST':
        
        #Get entered username and password
        username=request.form['username']
        password=request.form['password']
        
        #Check if it is in user and password DF and it's not empty string
        u_in_db =df1["username"].str.contains(username).any() and username is not ""
        p_in_db= df1["password"].str.contains(password).any() and password is not ""
      
        #if it is in the user and password DF
        if(u_in_db and p_in_db):
            
            #Find the index of the username, password, if commonpassword
            u=df1.index[df1['username'] == username].tolist()
            p=df1.index[df1['password'] == password].tolist() 
            c=df2.index[df2['CommonPasswords'] == password].tolist()
            
            #If the username and password has the same index(correct login)  
            if(u==p):
                
                
                #If the password is < 8 charactors 
                if(len(password)<8):
                    less_than_8=True
                    
                #If the password is > 64 charactors    
                if(len(password)>64):
                    greater_than_64=True
                    
                #If index found for commonly found password    
                if (len(c)>0):
                    commonly_found_passwords=True
                
                #Proceed to the next page    
                return redirect(url_for('nextPage', id="test"))    
            
            #If indexes didn't match 
            else:
                login_error='login failed try again'
                login_failed=True
                num_of_failed_logins+=1
                
        #If username or password isn't in the dataframe            
        else:
            login_error='login failed try again'
            login_failed=True
            num_of_failed_logins+=1
            
    #To be shared with different functions 
    ip=0
    login_failed_ip=0
    
    #If faild login attempt occurs 
    if(login_failed):
        
        #Enable logging
        logging.disable(logging.NOTSET)
 
        #Create a log
        logging.basicConfig(filename ='/home/ec2-user/environment/Lab8/failed.log',
                    level=logging.INFO,format='%(message)s:%(asctime)s') 
                    
        #Get client ip
        ip=request.environ['REMOTE_ADDR']
        
        #set to failed ip
        login_failed_ip=ip
        
        
                       
         
        #Start logging
        logging.info('Failed login attempt by: {} at '.format(ip) )
        
    
    #Disable logging when signing didn't fail    
    if(not login_failed):
        logging.disable(logging.CRITICAL)
        
        app.logger.disabled = True
        log = logging.getLogger('werkzeug')
        log.disabled = True
         
    
    #Create log analyzer for > 10 login attempts in < 5 minutes   
    if(num_of_failed_logins>5 and (time.time() <after_five_minutes)):
        write_this=""
        response = DbIpCity.get(ip, api_key='free')
        write_this+=str(ip)
        write_this+=str(" had ")
        write_this+=str(num_of_failed_logins)
        write_this+=str(" failed login attempts in at least a 5 minute period on ")
        write_this+=str(datetime.datetime.now().date())
        write_this+=str("\n")
        write_this+=str("\n")
        write_this+=str(ip)
        write_this+=str(" has a Lat/Long of ") 
        write_this+=str(response.latitude)
        write_this+=str("/") 
        write_this+=str(response.longitude) 
    
        with open("/home/ec2-user/environment/Lab8/log_analyzer.txt", 'w') as f: 
        
            f.write(write_this)

            f.close()
            
    #Render the login page        
    return render_template('login.html', login_error=login_error)

#Password update page    
@app.route('/', methods=['GET','POST'])    
def nextPage():
    
    #Different warnings to be displayed if appropriate 
    m1 = None
    m2 = None
    m3 = None
    m4 = None
    
    global num_of_failed_logins
    
    ip_address=request.environ['REMOTE_ADDR']
    
    #Reset the limit after the user successfully signed in
    if (ip_address == login_failed_ip):
      
        limiter.reset()
     
    

    #Display the appropriate warning to the user 
    if request.method == 'GET': 
        
        
        if commonly_found_passwords:
            m1='Your password is common please change it'
            
        if less_than_8:
            m2='Your password is too short please change it'
           
             
            
        if greater_than_64:
            m3='Your password is too long please change it'
     
    #When updating the password   
    elif request.method == 'POST':   
        old_password=None
        new_password=None
         
        #Get user input for the old password   
        old_password=request.form['old_password']
         
        #Get user input for the new password   
        new_password=request.form['new_password']
        
        #Get the index of the old passowrd from DF
        p=df1.index[df1['password'] == old_password].tolist() 
        
        #Get the index in the common password if it exists
        x=df2.CommonPasswords[df2.CommonPasswords == new_password].index.tolist()
         
        #If password change is allowed   
        change=True 

        #Password change denied
        if (len(new_password)<8):
            m2='Your password was not updated because your new password is too short'
            change=False
        
        #Password change denied  
        if (len(new_password)>64):
             m3='Your password was not updated because your new password is too long'
             change=False
             
        #Password change denied     
        if (len(x)>0):
            m1='Your password was not updated because your new password is common'
            change=False
        
        #If password change granted exception 
        if(change): 
            try: 
                print("Before the change.....")
                print(df1)
                x=p[0]    
            
                df1.loc[x,'password']=new_password
        
                m4='Your have successfully updated your password'
                
                print("After the change.....")
                print(df1)
         
            #If the password the user tring to change isn't the correct password 
            except:
                
                m4='Please make sure your password is correct'
        
    print(df1)
    
    #Render the page 
    return render_template('update.html',m1=m1,m2=m2,m3=m3,m4=m4)
    


    

#Run the web app   
app.run(host='0.0.0.0', port= 8080)
