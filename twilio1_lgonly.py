# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import date


f_date = date(2022, 4, 30) #Domek
f_date2 = date(2022, 7, 8) #Coldplay
f_date3 = date (2022, 6, 10) #Bulgaria
f_date4 = date (2022,10,16) #urodziny
c_date = date.today()
delta = f_date - c_date
delta2 = f_date2 - c_date
delta3 = f_date3 - c_date
delta4 = f_date4 - c_date
#bodyT = "Domek za "+str(delta.days)+" dni \nBulgaria za "+str(delta3.days)+" dni \nColdpay za "+str(delta2.days)+" dni"
bodyT = "Urodziny za "+str(delta4.days)+" dni"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token) 

phones = ["+48501202928"]

for xp in phones:
    message = client.messages.create(  
                                messaging_service_sid='MG9676c538c2a75469a425c09884c9a947', 
                                body=bodyT,      
                                to=xp 
                            ) 
 
print("done sms")
