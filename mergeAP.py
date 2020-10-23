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
        speak(kill_process_name+ " terminated")
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
        print("Listening..")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Sorry could not recognize your voice")
    return said


def handle_kill(cmd):
    lst = cmd.split()
    process = lst[len(lst)-1]
    kill_the_process(process.capitalize())







# current_apps = handle_incoming_current_process(current_process)
# print("Your running apps are: ")
# print(current_apps)
# kill_process_name = input("Name the process you want to kill:  ") 
# kill_the_process(kill_process_name)

# global commads
wake_word = "program"
to_end_process = ["stop","finish","terminate","shut down"]

while True:
    get_qs = ask()
    print(get_qs)
    if get_qs.count(wake_word) > 0:
        # speak("What do you want me to do?")
        print("What do you want me to do?")
        cmd = ask()
        if any(x in cmd for x in to_end_process):
            print(cmd)
            handle_kill(cmd)











