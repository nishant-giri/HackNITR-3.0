from twilio.rest import Client
import speak
def call() :
    client = Client("uiid",
                "token")
    call= client.calls.create(twiml='<Response><Say>Please Come Help me</Say></Response>',to = "+91",  from_ = "+13512072081" )
    print("done")  
    speak.speak("Successfully Called to Doctor Sir!")  

