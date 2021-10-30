from tkinter import *
from tkinter.font import Font 
from PIL import Image, ImageTk  # extrenal
import time
import serial # extrenal
import threading # extrenal
import pyautogui # extrenal
import continuous_threading 
import pyttsx3 # extrenal  
import speak
import call
import joke
import sms

# ser = serial.Serial('COM6')
# ser.baudrate = '9600'

# def readSerial():
#     h1 = ser.readline()
#     if h1:
#         ss = int(h1.decode('utf-8'))
#         if ss == 4: 
#             pyautogui.press('tab')
#             print("Tab Press")
#         if ss == 5 :
#             pyautogui.press('Enter')
#             print("Enter Press")

# t1 = continuous_threading.PeriodicThread(0.1, readSerial)



root =  Tk()
root.configure(background='#C4C4C4') # Changing the Background Color of Root 
width = root.winfo_screenwidth()  # Detect the Width 
print(width) # 1280
height = root.winfo_screenheight() # Detect the Height 720
print(height)
root.geometry("%dx%d" % (width, height))
root.title("Goggles-Assist") 

font_Head_lable_property = Font(
    family = "Comic Sans MS" ,
    size = 18,
    weight = "bold" 
)
 
font_Button_property = Font(
    family = "Comic Sans MS" ,
    size = 10,
    weight = "bold" 
)

font_Instruction_property = Font(
    family = "Comic Sans MS" ,
    size = 10,
    weight = "bold"
    
)

# All Frame 
Main_frame = LabelFrame(root , padx = 100 , pady = 7 , borderwidth=3, relief= "raised") # inside padding 
Main_frame.grid( row = 0 , column = 1 , padx = 20, pady = 60) # outside pading 

Display_frame = LabelFrame(root , padx= 55 , pady = 10 ,borderwidth=3, relief= "raised") # inside padding 
Display_frame.grid( row  = 0, column = 0 , padx = 150 , pady = 10 ,) # outside pading 

Instruction_frame = LabelFrame(root , padx= 30, pady = 4 , borderwidth=3, relief= "raised") # inside padding 
Instruction_frame.grid( row  = 0, column = 2, padx = 80, pady = 1) # outside pading 


# Display_frame Widget

lable_Display = Label(Display_frame , text = "Display Emotion" , font = ("Comic Sans MS" , 14 , "bold" ) , bg = "#C4C4C4" )
lable_Display.grid(row= 0,  column= 0 ,padx = 20 ,  pady = 10)

Display_Image = ImageTk.PhotoImage(Image.open("Image/Background.png"))
Default_Label = Label(Display_frame ,image = Display_Image)
Default_Label.grid(row = 1 , column = 0 , pady = 20)




# Label Funtion to all Button 

def food_label() :
    lable_Display.config(text = "I Wanna Eat Food")

def send_label() :
    lable_Display.config(text = "Message Sending") 

def happy_label() :
    lable_Display.config(text = "I'm Happy Today")

def joke_label() :
    lable_Display.config(text = "listening jokes")

def toilet_label() :
    lable_Display.config(text = "I Wanna Go to Toilet")

def doctor_label() :
    lable_Display.config(text = "Call Doctor")




# Function of all Button 



def Send(event) :
    img_send = ImageTk.PhotoImage(Image.open("Image/send.jpg"))
    Default_Label.configure(image=img_send)
    Default_Label.image = img_send
    send_label()
    speak.speak("Send SMS")
    sms.sms("Please Come, Help me")
   
    
    
    

    

def Joke(event) :
    img_Joke = ImageTk.PhotoImage(Image.open("Image/Joke.png"))
    Default_Label.configure(image=img_Joke)
    Default_Label.image = img_Joke
    joke_label()
    speak.speak("Joke Sir!")
    joke.joke()
    



def Doctor(event) :
    img_Doctor = ImageTk.PhotoImage(Image.open("Image/Doctor.png"))
    Default_Label.configure(image=img_Doctor)
    Default_Label.image = img_Doctor
    doctor_label()
    speak.speak("Call Doctor")
    call.call()
    

# Main_Frame Widget 

Head_lable = Label(Main_frame , text = "Goggles-Assist" , font = font_Head_lable_property , bg = "#C4C4C4")
Head_lable.grid(row = 0 ,column = 0 )




button_2 = Button(Main_frame , text = "Send Message", font = font_Button_property , bg = "#C4C4C4" , pady=20 , padx = 55 , borderwidth= 3, relief=SOLID,command = Send)
button_2.bind("<Return>", Send)
button_2.grid(row = 2 ,column = 0 , pady = 10)







button_4 = Button(Main_frame , text = "Tell Me a Joke Assistant", font = font_Button_property , bg = "#C4C4C4" , pady=20 , padx = 10, borderwidth= 3, relief=SOLID,command = Joke)
button_4.bind("<Return>", Joke)
button_4.grid(row = 4 ,column = 0 , pady = 10)




button_6 = Button(Main_frame , text = "Call Doctor", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Doctor)
button_6.bind("<Return>", Doctor)
button_6.grid(row = 6 ,column = 0 , pady = 10)


# Instruction_frame Widget

Var_Instruction_One = "➜ Blink Right Eye for Select the Button"
Var_Instruction_Two = "➜ Blink Left Eye for Click the Button\t"
Instruction_label_Head= Label(Instruction_frame , text = "Instruction",font =("Comic Sans MS" , 14, "bold" ), bg ="#C4C4C4")
Instruction_label_One = Label(Instruction_frame , text = Var_Instruction_One, font = font_Instruction_property , fg = "red")
Instruction_label_Two = Label(Instruction_frame , text = Var_Instruction_Two, font = font_Instruction_property ,fg = "red")

Instruction_label_Head.grid(row= 0,column= 0 )
Instruction_label_One.grid(row = 1,column = 0 , padx = 0 , pady = 5)
Instruction_label_Two.grid(row = 2 , column = 0 ,padx = 0, pady = 5)




# t1.start() # Strat the threading
root.mainloop()
