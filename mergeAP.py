import applescript
import re
import os, sys
from subprocess import Popen, PIPE
import subprocess

import playsound
import speech_recognition as sr
from gtts import gTTS

import threading

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


def switch_process(switch_process_name):
    args = [switch_process_name]
    p = subprocess.Popen(
            ['osascript', 'switchprocess.applescript'] + [str(arg) for arg in args], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    

def kill_the_process(kill_process_name):
    args = [kill_process_name]
    p = subprocess.Popen(
            ['osascript', 'killprocess.applescript'] + [str(arg) for arg in args], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    

def open_process(open_process_name):
    args = [open_process_name]
    p = subprocess.Popen(
            ['osascript', 'openprocess.applescript'] + [str(arg) for arg in args], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    
def beep():
    p = subprocess.Popen(
            ['osascript', 'beep.applescript'], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()


def speak(text,status):
    if status == "open":
        show_txt = text + " is openned"
    elif status == "general":
        show_txt = text
    elif status == "kill":
        show_txt = text + " is terminated"
    elif status == "switch":
        show_txt = "switched to " + text
    
    tts = gTTS(text = show_txt, lang = "en")
    filename = "command.mp3"
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

def handle_init(cmd, status):
    lst = cmd.split()
    process = lst[len(lst)-1]
    process_cap = process.capitalize()
    if status == "kill":
        kill_thread = threading.Thread(target=kill_the_process,args=[process_cap])
        sp_thread = threading.Thread(target=speak,args=[process_cap,"kill"])
        kill_thread.start()
        sp_thread.start()
    elif status == "open":
        op_thread = threading.Thread(target=open_process,args=[process_cap])
        sp_thread = threading.Thread(target=speak,args=[process_cap,"open"])
        op_thread.start()
        sp_thread.start()
    elif status == "switch":
        swtch_thread = threading.Thread(target=switch_process,args=[process_cap])
        sp_thread = threading.Thread(target=speak,args=[process_cap,"switch"])
        swtch_thread.start()
        sp_thread.start()


# global commads
wake_word = "program"
to_end_process = ["stop","finish","terminate","shut down","exit"]
to_open_process = ["open","turn on","launch"]
to_switch_process = ["go to","switch to", "go" ,"switch"]
exit_self = "self"


def brain():
    while True:
        get_qs = ask()
        print(get_qs)
        if get_qs.count(wake_word) > 0:
            beep()
            cmd = ask()
            if any(x in cmd for x in to_end_process):
                if exit_self in cmd:
                    exit()
                else:
                    print(cmd)
                    handle_init(cmd, "kill")
            if any(x in cmd for x in to_open_process):
                print(cmd)
                handle_init(cmd, "open")
            if any(x in cmd for x in to_switch_process):
                print(cmd)
                handle_init(cmd, "switch")


if __name__ == "__main__":
    bt = threading.Thread(target=brain)
    bt.start()
    
    














