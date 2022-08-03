
import datetime
import pyttsx3
import smtplib
import os
import wikipedia
import webbrowser
import speech_recognition as sr


print(" Initializing Elexa")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()



date = datetime.datetime.now().date()
hour = datetime.datetime.now().hour

def wishme( hour):
   if hour < 12:
        engine.say("good morning master")

   elif hour == 12:
        engine.say("GOOD AFTERNOON MASTER")

   else:
       engine.say("good evening master")


speak(date)
wishme(hour)
speak(" I AM ELEXA ")
speak(" how can i help you")
speak(" please say something ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        speak(f"You Said : {query}")

    except Exception as e:
        print('exception : ', e)
        speak("Sorry, I didn't hear that, Say that again Please")
        return "None"

    return query


if __name__ == '__main__':
    query= takecommand().lower()

    print("The Test got in program is : " + query)



if 'wikipedia'in query:

    print("searching wikipedia")
    query = query.replace('wikipedia','')
    result= wikipedia.summary(query,sentences=2)
    print(result)
    speak(result)


elif 'youtube' in query:
     webbrowser.open("youtube.com")



elif'insta'in query:
    webbrowser.open("instagram.com")

elif 'facebook' in query:
    webbrowser.open("facebook.com")


elif ' vlive' in query:
    webbrowser.open("vlive.com")

elif 'whatsapp'in query:
    webbrowser.open("whatsapp.com")