# Author LukaszG

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import date

# all files
## create new dir
## .env with env variables #moved to AWS lambda setup
## pip install twilio -t . #install dependecies locally
## add naming convenrion: lambda_function.lambda_handler
## aws_pkg_priv % zip -r ../aws_pkg_priv.zip . #create zip pkg
## upload to AWS
# 

def lambda_handler(event, context):
        
    # EVENTS
    # f_date = date(2022, 4, 30) #Domek
    f_date2 = date(2024, 8, 16) #Wisla
    # f_date3 = date(2024, 7, 5) #WWa
    # f_date4 = date(2024, 5, 27) #Gory Stolowe


    # CURRENT DATE
    c_date = date.today()

    # DELTA
    # delta = f_date - c_date
    delta2 = f_date2 - c_date
    # delta3 = f_date3 - c_date
    # delta4 = f_date4 - c_date

    # TEXT
    # bodyT = "Domek za "+str(delta.days)+" dni \nBulgaria za "+str(delta3.days)+" dni \nColdpay za "+str(delta2.days)+" dni"
    # bodyT = "Urodziny za "+str(delta4.days)+" dni"
    bodyT = "Wisla za "+str(delta2.days)+" dni\nDo zobaczenia :)"

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token) 


    phones = ["+48501202ABC", "+48888998ABC", "+48796669ABC"]
    #phones = ["+48501202928"]

    for xp in phones:
        message = client.messages.create(  
                                    messaging_service_sid='MGc7075f5bd91e948b8aff9ed1762cbABC', 
                                    body=bodyT,      
                                    to=xp 
                                ) 
    
    print("done sms")
