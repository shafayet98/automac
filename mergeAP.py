import applescript
import re
import os, sys
from subprocess import Popen, PIPE
import subprocess

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



current_apps = handle_incoming_current_process(current_process)
print("Your running apps are: ")
print(current_apps)
kill_process_name = input("Name the process you want to kill:  ") 
kill_the_process(kill_process_name)