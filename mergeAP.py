import applescript
import re
import os, sys
from subprocess import Popen, PIPE
import subprocess

import playsound
import speech_recognition as sr
from gtts import gTTS

(current_process, tError) = Popen(['osascript', 'getprocess.applescript'], stdout=PIPE).communicate()
# print(current_process)


def handle_incoming_current_process(current_process):
    # decode bytes to string and string to list
    b2s = current_process.decode()
    s2l = b2s.split(",")
    current_apps = []
    s2l[len(s2l)-1] = s2l[len(s2l)-1].replace("\n",'')
    for item in s2l:
        item = item.strip()
        current_apps.append(item)
    return current_apps


def kill_the_process(kill_process_name):
    args = [kill_process_name]
    p = subprocess.Popen(
            ['osascript', 'killprocess.applescript'] + [str(arg) for arg in args], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if err:
        print(err)
    else:
        print(out)

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def ask():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("mic on")
        audio = r.record(source=mic, duration=10)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Sorry could not recognize your voice")
    return said

def ask_again():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.record(source, duration=4)
        text = r.recognize_google(audio, language = 'en-IN', show_all = True )
        print(text['alternative'][0]['transcript'])



# current_apps = handle_incoming_current_process(current_process)
# print("Your running apps are: ")
# print(current_apps)
# kill_process_name = input("Name the process you want to kill:  ") 
# kill_the_process(kill_process_name)

speak("Hello How are you")
ask_again()











