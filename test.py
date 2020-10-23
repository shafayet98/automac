import applescript
import re
import os, sys
from subprocess import Popen, PIPE
import subprocess

import playsound
import speech_recognition as sr
from gtts import gTTS


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

s = "stop spotify"
lst = s.split()
word = lst[len(lst)-1]
print(word.capitalize())


