# MIVI Desktop Assistant

# importing of modules 

from urllib.request import ProxyBasicAuthHandler
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def  wishMe():   # greeting the function
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour > 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hii My name Is Mivi , How may I help you ?")


def takeCommand():
    # it takes microphone input and gives the string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio , language="en-in")
        print(f'User Said : {query}\n')

    except Exception as e :
        print("Say That again please.....")

        return "None"

    return query

def sendEmail (to , content):    # Email sending Function
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login("email of the account" , "passwords")
    server.sendmail("email of the acc" ,to , content)
    server.close()






if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'stackover flow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\User\\Desktop\\som\\Gaurav\\M"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir , songs[random.randint(0 , 50)]))
            
        elif "time" in query:
            strrtime = datetime.datetime.now().strftime("%H:%M:%S")
            strdate = datetime.datetime.now().strftime("%d , %B , %Y")
            speak(f"The Time is {strrtime}")
            speak(f"Date is {strdate}")

        elif "code" in query:
            code_path = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "pycharm" in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif "chrome" in query:
            code_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code_path)

        elif "email" in query:
            try :
                speak("What should i say")
                content  = takeCommand()
                to = "gauravptl023@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent ..")
            except Exception as e:
                print(e)
                speak("Sorry Not able to send the email")
