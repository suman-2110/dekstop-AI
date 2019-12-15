import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("goodmorning..!")
    elif hour>=12 and hour<=18:
        speak("goodafternoon..!")
    else :
        speak ("good evening")
    speak("hey this is aarv ! how may i help you sir")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print('say it again please.....')
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("rr9002575@gmail.com",'*******')
    server.sendmail("rr9002575@gmail.com",to,content)
    server.close()
    

if __name__ == "__main__":
#speak("hey guys...!this is python freak.........plz do follow")
    WishMe()
    while True:
#speak("yeah")
        query = takecommand().lower()
#logic for executing task 
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
            break
            
        elif 'open youtube' in query :
            webbrowser.open('youtube.com')
            break
        elif 'open google' in query :
            webbrowser.open('google.com')
            break
        elif 'stackoverflow' in query :
            webbrowser.open('stackoverflow.com')
            break
        elif 'open gmail' in query :
            webbrowser.open('gmail.com')
            break
        elif 'open gaana' in query :
            webbrowser.open('gaana.com')
            break
        elif 'open spotify' in query :
            webbrowser.open('spotify.com')
            break
        elif 'who are you' in query:
            print("i am aarv..!how may i help you sir")
            speak('i am aarv..!how may i help you sir')
            break
        elif 'play song' in query :
            music_dir='C:\\Users\\rr900\\Music\\New folder'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            break
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is : {strTime}") 
            break 
        elif 'open code' in query:
            codePath="C:\\Users\\rr900\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  
            break
        elif 'email to rahul' in query:
            try:
                speak("what should i say ?")
                print("what should i say ?")
                content=takecommand()
                to =('rr9002575@gmail.com')
                sendEmail(to,content)
                print("email has been sent")
                speak("email has been sent")
                
            except Exception as e:
                print(e)
                speak("fail to sent")
        break
