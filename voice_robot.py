import datetime
import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer =sr.Recognizer()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def audio_record():
    with sr.Microphone() as source:
        print("Listening.....")
        audio=recognizer.listen(source)
    return audio



def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning sir")
    elif 12 <= hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am your assistant")
    speak("how can i help you")



def speech_recognition(audio):
    
    try:
        text = recognizer.recognize_google(audio, language ='en-in')
        print(f"you said {text}")
        if "open youtube" in text.lower():
            web_url="https://www.youtube.com/watch?v=xvFZjo5PgG0"
            webbrowser.open(web_url)
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
    except sr.RequestError as e:
        print(f"Error processing your request: {e}")



if __name__=="__main__":
     wishme()
     audio=audio_record()
     speech_recognition(audio)
            

    