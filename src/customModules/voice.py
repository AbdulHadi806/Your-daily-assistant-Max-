import pyttsx3
import speech_recognition as sr

def aiVoice(text):
    engine = pyttsx3.init()
    current_rate = engine.getProperty('rate') 
    engine.setProperty('rate', current_rate - 50)
    engine.say(text)
    engine.runAndWait()
    
def userVoice():
    r = sr.Recognizer() 
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText, 'voice in function')
            return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError as e:
        print("unknown error occurred", e)
