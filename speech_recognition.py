import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(a):
    print(a)
    tts = gTTS(text=a, lang='en')
    tts.save("voice.mp3")
    os.system("voice.mp3")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
	print("request error")
    return data


def record_audio(data):
    if "how are you" in data:
        speak("I am fine")

    if "what is your job?" in data:
        speak("To recognize your speech and do that action")

time.sleep(1)
speak("Hi Phani, I am your voice assistant")
while 1:
    dat=recordAudio()
    record_audio(dat)
