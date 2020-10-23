import os 
import subprocess
import psutil


data = subprocess.Popen(['ps','aux'], stdout=subprocess.PIPE).stdout.readlines() 
print(data[0])
print()

b2s = [] # bytes to string
s2l = [] # string to list
pids = []
pnames = []

for i in range(1,10):
    b2s.append(data[i].decode())

for s in b2s:
    s2l.append(s.split())

for item in s2l:
    pids.append(item[1])
    pnames.append(psutil.Process(int(item[1])).name)


print(pids)
print()
print(pnames)
print()
print(type(pnames[0]))





