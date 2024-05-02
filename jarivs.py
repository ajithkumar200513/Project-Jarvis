from imaplib import Commands
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import pyautogui
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      r.adjust_for_ambient_noise(source ,duration=1)
      audio = r.listen(source)
        
    try:
         print("Wait for Few Moments...")
         query = r.recognize_google(audio, language='en-in')
         print(f"You just said: {query}\n")
   
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query="none"       
    return query 

def wishings():   
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
         print("Good Morning Boss")
         speak("Good Morning Boss")
    elif hour>=12 and hour<17:
         print("Good Afternoon Boss")
         speak("Good Afternoon Boss")
    elif hour>=17 and hour>21:
         print("Good Evening Boss")
         speak("Good Evening Boss") 
    else:
         print("Good night Boss")
         speak("Good Night Boss") 
         
def wakeUpCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is Slepping...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        query="none"
    return query  

 
   

  




if __name__ =="__main__":
            
        while True:
            query =wakeUpCommands().lower()
            if "wake up" in query:
             wishings()
             speak("Yes Boss What can I do for you")
             if 'wikipedia'in query:
                     speak("Searching in wikipedia")
                     try:
                         query=query.replace()
                         results = wikipedia.summary(query, sentences=30)
                         speak("According to wikipedia...")
                         print(results)
                         speak(results)
                     except:
                         print("No results Found sir...")
                         speak("No results found")
                         
            elif 'play' in query :
                       playquery=query.replace('play','')
                       speak("playing " + playquery) 
                       pywhatkit.playonyt(playquery)         
                
            if 'time' in query:
                   strTime = datetime.datetime.now().strftime("%H:%M:%S")
                   speak("Sir, The time is: " + strTime)
                   print(strTime) 
                   
            elif "mute" in query:
                     speak("I'm Muting Sir...")
                     break
                 
            elif 'exit program' in query or 'exit the program' in query:
                     speak("I'm Leaving Sir, Byeee...")
                     quit()
                     
            elif "open google" in query:
                     speak("Opening Google Chrome Sir")
                     os.startfile("Your chrome file path")
                     while True:
                         chromequery=Commands().lower()
                         if "search" in chromequery:
                             youtubequery=chromequery
                             youtubequery=youtubequery.replace("search", "")
                             pyautogui.write(youtubequery)
                             speak('searching...')
                             
                         elif "close chrome" in chromequery or "exit chrome" in chromequery or "exit google" in chromequery:
                             pyautogui.hotkey('ctrl','w')
                             speak("closing Google chrome sir...")
                             break
            elif "what can you do for me" in query:
                     speak('Yes Sir,Nice question')
                     speak('As per my program, Iam a bot which can perform tasks through your voice commands')
            elif"cool" in query or "nice" in query or "awsome" in query or "thank you" in query:
                     speak("yes sir, That's my pleasure")
            elif "minimize" in query or "minimise" in query:
                     speak("Minimizing Sir")
                     pyautogui.hotkey('win','down','down')
            elif "maximize" in query or "maxmise" in query:
                     speak('Maxmizing Sir')
                     pyautogui.hotkey('win', 'up','up')
            elif "close the window" in query or "close the application" in query:
                     speak('closing sir')
                     pyautogui.hotkey('ctrl','w')
            elif "screenshot" in query:
                     speak("Taking screenshot sir...")
                     pyautogui.press('prtsc')
            elif "open paint" in query:
                     speak("opening paint Application sir...")
                     os.startfile('your paint file path')
                     while True:
                         paintquery= Commands().lower()
                         if "close" in paintquery:
                             speak("closing the application sir")
                             pyautogui.leftClick(x=1344, y=11)
                             break
                         elif "paste" in paintquery:
                             pyautogui.hotkey('ctrl','v')
                             speak("Done Sir!")
                         elif "save" in paintquery:
                             pyautogui.hotkey('ctrl','s')
                             speak("saving sir!")
                               
                         elif 'type' in query:
                            speak("Please tell me what should i write")
                         while True:
                             typequery = Commands().lower()
                             if typequery == "exit typing":
                              speak("Done Sir")
                             break
                         else:
                           pyautogui.write(typequery)
            elif 'joke' in query:
                  jarvisJoke = pyjokes.getjoke()
                  print(jarvisJoke)
                  speak(jarvisJoke)    
                    
       
        
  
   
            
    
    
  
                
                