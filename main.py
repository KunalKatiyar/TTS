import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r=sr.Recognizer()
r.energy_threshold = 4000

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            kundalini_speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            kundalini_speak("Sorry, I didn't get that")
        except sr.RequestError:
            kundalini_speak("Sorry, my speech service is not working at the moment")
        return voice_data

def kundalini_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r=random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        kundalini_speak("My name is Kunal")
    if 'what time is it' in voice_data:
        kundalini_speak(ctime())
    if 'search' in voice_data:
        search =record_audio('What do you want to search for?')
        url ='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        kundalini_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        kundalini_speak('Here is the location of '+ location)
    if 'exit' in voice_data:
        exit()
    
time.sleep(1)
kundalini_speak('Lets go!')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)