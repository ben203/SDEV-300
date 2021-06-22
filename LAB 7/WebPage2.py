from flask import Flask, request
from time import gmtime, strftime
 

app = Flask(__name__,static_folder='/home/ec2-user/environment/Lab7')



@app.route('/mysecondwebsight')
def mainIndex():
    result=pop_head()
    result+=display_time_and_date()
    result+=pop_title_header()
    
    
    
    result+=pop_h("Bugatti",2)
    result+="<img src='../Lab7/Buggatti.png'height='100'width='150' align='right'/>"
    result+=get_bugatti_parag()
    result+=bugatti_unordered_list()
    result+=get_external_link("http://bugatti.com/models/veyron-models/")
    
     

    result+=pop_h("Lamborghini",3)
    result+="<img src='../Lab7/Lambo.png'height='100'width='150' align='right'/>"
    result+= lamborghini_ordered_list()
    result+=get_external_link("http://lamborghini.com/en-en")
     
    
    result+=pop_h("Ferrari",4)
    result+="<img src='../Lab7/Ferrari.png'height='100'width='150' align='right'/>"
    result+= get_ferrari_parag()
    result+= ferrari_ordered_list()
    result+=get_external_link("http://ferrari.com/en-US")
     
    
    result+=pop_h("Porsche",5)
    result+="<img src='../Lab7/Porsche.png'height='100'width='150' align='right'/>"
    result+=get_porsche_parag() 
    result+=porsche_ordered_list()
    result+=get_external_link("http://porsche.com/usa/")
     
    
    result+=pop_h("Rolls-Royce",6)
    result+="<img src='../Lab7/Rolls_Royce.png'height='100'width='150' align='right'/>"
    result+=get_rolls_royce_parag() 
    result+=rolls_royce_table_data()
    result+=get_external_link("http://rolls-roycemotorcars.com")
     
    result+=user_interaction()
    
  
    
    result+=popEnd()
 
    return result
    
#Disply current time and date 
def display_time_and_date(): 
   
    time_and_date="<p align='right'> <b>Current Time and Date</b> </p>"
    time_and_date+="<p align='right'>"+strftime("%m-%d-%y %H:%M:%S", gmtime())
    time_and_date+="</p>"  
    return time_and_date
    
#Create html header tags    
def pop_h(my_string,x):
    new_string="<!-- html header-->"
    new_string+="<font size='5'>" 
    new_string+= '<b><hx>' + my_string + '</font></b></hx>'
    return new_string
    
#Set the title and background of the page     
def pop_head():
    head_data = "<!DOCTYPE html> "
    head_data +="<head> "
    head_data +="<title>My second Website</title>"
    head_data +="</head>"
    head_data+="<body bgcolor='#FFFAF0'>"
    return head_data
    
#The first hearder with serves as the title of the page     
def pop_title_header():
    result="<!--Title page header-->"
    result+="<center><b>"
    result+="<font size='20'>" 
    result+="Luxury Car Brands</font></b></center>"
    return result

#Unordered list of production models from 2005 to 2015   
def bugatti_unordered_list():
    unord_list="<!--unordered list with default numrators-->"
    unord_list+="<p><i><b> Production models from 2005 to 2015 </b> </i>"
    unord_list+= "<li>2005–2011 (Veyron 16.4)</li>"
    unord_list+="<li>2009–2015 (Grand Sport)</li>"
    unord_list+="<li>2010–2011 (Super Sport)</li>"
    unord_list+="<li>2012–2015 (Grand Sport Vitesse)</li></p>"
    return unord_list

#Ordered list of car sales from 2010 to 2019      
def lamborghini_ordered_list():
    ord_list="<!--ordered list with default numrators-->"
    ord_list+="<p> <i><b>New car sells between 2015 to 2019</i></b>"
    ord_list+="<ol> <pre>"
    ord_list+="<b> Year    sales</b>" 
    ord_list+="<li>2010     1,302</li>"
    ord_list+="<li>2011     1,602</li>"
    ord_list+="<li>2012     2,083</li>"
    ord_list+="<li>2013     2,121</li>"
    ord_list+="<li>2014     2,530</li>"
    ord_list+="<li>2015     3,245</li>"
    ord_list+="<li>2016     3,457</li>"
    ord_list+="<li>2017     3,815</li>"
    ord_list+="<li>2018     5,750</li>"
    ord_list+="<li>2019     8,205</li>" 
    ord_list+="</pre></ol></p>"
    ord_list+= "</ul></p>"
    return ord_list
    
#Ordered list of current modles    
def ferrari_ordered_list():
    ord_list="<!--ordered list with roman numrators-->"
    ord_list+="<p> <i><b>Current models</i></b>"
    ord_list+="<ol type = 'I'>"
    ord_list+= "<li>GTC4Lusso</li>"
    ord_list+="<li>F8 Tributo</li>"
    ord_list+= "<li>Portofino</li>"
    ord_list+= "<li>812 Superfast</li>"
    ord_list+= "<li>SF90 Stradale</li>"
    ord_list+= "</ul></ol></p>"
    return ord_list
    
#Unordered list of revenues     
def porsche_ordered_list():
    unord_list="<!--unordered list in a table-->"
    unord_list+="<p> <table border='3'>"
    unord_list+="<tr> <td><b>Year</b></td> <td><b>Revenue</b></td> </tr>"
    unord_list+="<tr><td>2011</td> <td>€10.9b</td> </tr>"
    unord_list+="<tr><td>2012</td> <td>€13.9b</td> </tr>"
    unord_list+="<tr><td>2013</td> <td>€14.3b</td> </tr>"
    unord_list+="<tr><td>2014</td> <td>€17.2b</td> </tr>"
    unord_list+="<tr><td>2015</td> <td>€21.5b</td> </tr>"
    unord_list+="</table></p>"
    return unord_list
 
    
#Paragraph text    
def get_bugatti_parag():
    p="<font color='red'>" 
    p+="<p> The Bugatti Veyron is a mid-engine sports car, designed and developed" 
    p+="in Germany by the Volkswagen Group and manufactured in Molsheim, France,"
    p+="by French automobile manufacturer Bugatti. It was named after the racing"
    p+="driver Pierre Veyron.The original version has a top speed of 407 km/h"
    p+="(253 mph). It was named Car of the Decade and best car award (2000–2009)" 
    p+="by the BBC television programme Top Gear. The standard Bugatti Veyron"
    p+="also won Top Gear's Best Car Driven All Year award in 2005."
    p+="The Super Sport version of the Veyron is recognised by Guinness World" 
    p+="Records as the fastest street-legal production car in the world, with a" 
    p+="top speed of 431.072 km/h (267.856 mph). The Veyron Grand Sport Vitesse"
    p+="was the fastest roadster in the world, reaching an averaged top speed of"
    p+="408.84 km/h (254.04 mph) in a test on 6 April 2013.</p></font>"
    
    return p
 
#Paragraph text      
def get_lamborghini_parag():
    p="<font color='blue'>" 
    p+="<p> Automobili Lamborghini S.p.A. (Italian pronunciation: [lamborˈɡiːni])"
    p+="is an Italian brand and manufacturer of luxury sports cars and SUVs based"
    p+="in Sant'Agata Bolognese. The company is owned by the Volkswagen Group"
    p+="through its subsidiary Audi.Ferruccio Lamborghini, an Italian manufacturing"
    p+="magnate, founded Automobili Ferruccio Lamborghini S.p.A. in 1963 to compete"
    p+="with established marques, including Ferrari. The company was noted for using"
    p+="a rear mid-engine, rear-wheel drive. Lamborghini grew rapidly during its"
    p+="first decade, but sales plunged in the wake of the 1973 worldwide financial"
    p+="downturn and the oil crisis. The firm's ownership changed three times after"
    p+="1973, including a bankruptcy in 1978. American Chrysler Corporation took"
    p+="control of Lamborghini in 1987 and sold it to Malaysian investment group"
    p+="Mycom Setdco and Indonesian group V'Power Corporation in 1994. In 1998,"
    p+="Mycom Setdco and V'Power sold Lamborghini to the Volkswagen Group where"
    p+="it was placed under the control of the group's Audi division.</p></font>"
    
    return p
    
#Paragraph text  
def get_ferrari_parag():
    p="<p> Ferrari ( Italian: [ferˈraːri]) is an Italian luxury sports car"
    p+="manufacturer based in Maranello. Founded by Enzo Ferrari in 1939 out of"
    p+="Alfa Romeo's race division as Auto Avio Costruzioni, the company built"
    p+="its first car in 1940. However, the company's inception as an auto"
    p+="manufacturer is usually recognized in 1947, when the first Ferrari-badged"
    p+="car was completed. In 2014 Ferrari was rated the world's most powerful"
    p+="brand by Brand Finance. In June 2018, the 1964 250 GTO became the most"
    p+="expensive car in history, setting an all-time record selling price of"
    p+="$70 million.</p>"
    
    return p
    
#Paragraph text  
def get_porsche_parag():
    p="<font color='green'>" 
    p+="<p>Porsche AG, usually shortened to Porsche AG (German pronunciation:"
    p+="[ˈpɔɐ̯ʃə] (About this soundlisten); see below), is a German automobile"
    p+="manufacturer specializing in high-performance sports cars, SUVs and sedans."
    p+="The headquarters for Porsche AG is in Stuttgart, and is owned by" 
    p+="Volkswagen AG, which itself is majority owned by Porsche Automobil"
    p+="Holding SE. Porsche's current lineup includes the 718 Boxster/Cayman,"
    p+="911, Panamera, Macan, Cayenne and Taycan.</p></font>"
    
    return p
    
#Paragraph text  
def get_rolls_royce_parag():
    p="<font color='purple'>" 
    p+="<p>Rolls-Royce Motor Cars Limited is a British luxury automobile maker."
    p+="A wholly owned subsidiary of German group BMW, it was established in 1998"
    p+="after BMW was licensed the rights to the Rolls-Royce brand name and logo"
    p+="from Rolls-Royce plc and acquired the rights to the Spirit of Ecstasy and" 
    p+="Rolls-Royce grill shape trademarks from Volkswagen AG. Rolls-Royce Motor" 
    p+="Cars Limited operates from purpose-built administrative and production" 
    p+="facilities opened in 2003 across from the historic Goodwood Circuit in" 
    p+="Goodwood, West Sussex, England, United Kingdom. Rolls-Royce Motors Cars" 
    p+=" Limited is the exclusive manufacturer of Rolls-Royce branded motor" 
    p+="cars since 2003.</p></font>"

    return p
    
#Table 7x5
def rolls_royce_table_data():
    table="<!--Table with rolls-royce data-->"
    table+="<style> table, th, td {"
    table+="border: 1px solid black;} </style>"
    table+="<p> <table border='1'>"
    table+="<table bgcolor='#00FFFF'>"
    
    table+="<tr> <td><b>Year</b></td> <td><b>Total Sales</b></td>"
    table+="<td><b>US</b></td> <td><b>Europe</b></td>"
    table+="<td><b>China</b></td></tr>"
    
    table+="<tr><td>2012</td> <td>3,575</td> <td>20%</td>" 
    table+="<td>23%</td> <td>15%</td></tr>"
    
    table+="<tr><td>2013</td> <td>3,630</td> <td>22%</td>"
    table+="<td>25%</td> <td>19%</td></tr>"
    
    table+="<tr><td>2014</td> <td>4,063</td> <td>19%</td>"
    table+="<td>20%</td> <td>20%</td></tr>"
    
    table+="<tr><td>2015</td> <td>3,785</td> <td>15%</td>"
    table+="<td>19%</td> <td>35%</td></tr>"
    
    table+="<tr><td>2016</td> <td>4,011</td> <td>20%</td>"
    table+="<td>18%</td> <td>39%</td></tr>"
    
    table+="<tr><td>2017</td> <td>3,362</td><td>23%</td>"
    table+="<td>13%</td> <td>45%</td></tr>"
    
    table+="<tr><td>2018</td> <td>4,107</td> <td>19%</td>"
    table+="<td>15%</td> <td>49%</td></tr>"
    table+="</table></p>"
    
    return table
    
#External link maker
def get_external_link(url):
    link="<p><b>Click below to visit their website</b></p>"
    link+="<p><a href="+url+ "> Car Website </p></a>"

    return link
 
#Adds the two textfields and writes to the file user input 
@app.route("/Lab7/output.txt", methods=[ "POST"])
def user_interaction(): 
 
    ui="<form >"
    ui+="<p><b>Which one is your dream car</b><br />"
    ui+="<select name='choice'>"
    ui+="<option value=''></option>"
    ui+="<option value='Bugatti'>Bugatti</option>"
    ui+="<option value='Lamborghini'>Lamborghini</option>"
    ui+="<option value='Ferrari'>Ferrari</option>"
    ui+="<option value='Porsche'>Porsche</option>"
    ui+="<option value='Rolls-Royce'>Rolls-Royce</option>"
    ui+="</select><br />"
    ui+="<b>Tell us why </b><br /> <textarea cols=40 rows=10"
    ui+="<select name='reason'> </textarea><br />"
    ui+="<input type='submit' value='Submit'>"
    ui+="<input type='reset' value='Reset'></p></form>"
     
    in_put = ""    
    in_put+=str("My luxury car brand choice: ")
    in_put+=str(request.values.get('choice'))
    in_put+=str("\n")
    in_put+=str("\nThe reason: ")
    in_put+=str(request.values.get('reason'))
   
    with open('output.txt', 'w') as f:
 
        f.write(in_put)

        f.close()
        
    return ui

 
 
 
#End of the page    
def popEnd():
    endData = "</body>"
    endData += "</html>"
    return endData
    
app.run(host='0.0.0.0', port= 8080)