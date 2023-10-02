from Brain.palm import ReplyBrain
from Brain.Qna import QnAReplyBrain
from Body.Listen import MicExecution
import speech_recognition as sr

print(">> Starting The Jarvis : Wait for some seconds.")

from Body.Speech import Speak
# from Features.clap import Tester

def List():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        query = r.recognize_google(audio, language='en')
        
    except:
        return ""
        
    query = str(query).lower()
    return query




def MainEx():
    Speak("Hello Sir, I am Jarvis. I'm Ready To Assist You Sir.")
    while True:
       Data = MicExecution()
       Data = str(Data).lower()
       if int(Data)<=3:
           pass
       elif "what is" in Data or "where" in Data or "question" in Data or "answer" in Data or "How is" in Data:
           reply = QnAReplyBrain(Data)
           Speak(reply)
       else: 
           reply = ReplyBrain(Data)
           Speak(reply)


def Detect():
    query = List().lower()
    print(query)
    if "wake up" in query:
        print(">> Wakeup Detected")
        MainEx()
    else:
        pass

Detect()

        
   