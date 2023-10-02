import speech_recognition as sr
from googletrans import Translator


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        
    except:
        return ""
        
    query = str(query).lower()
    return query

def TranslateHinToEng(Text):
    line = str(Text)
    translator = Translator()
    result = translator.translate(line, dest='en')
    data = result.text
    print(f"You: {data}.")
    return data

def MicExecution():
    query = Listen()
    if query == "":
        return ""
    else:
        return TranslateHinToEng(query)
    

