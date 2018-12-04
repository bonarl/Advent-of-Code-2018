# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:37:21 2018

@author: bonar
"""
from datetime import datetime, timedelta

file = open('4input.txt','r')
data = file.readlines()

data_d = []
for i in range(len(data)):
    d = {}
    item = data[i]
    timestamp = datetime.strptime(item[1:17],"%Y-%m-%d %H:%M")
    d["timestamp"] = timestamp
    d["item"] = item.split(']')[1][1:]
    data_d.append(d)

data_d.sort(key=lambda d : d['timestamp'])
for d in data_d:
    item = d["item"].split(" ")
    if len(item) > 2:
        guard = int(item[1].split("#")[1])
    d["guard"] = guard
    d["minute"] = d["timestamp"].minute    

biggest_boy = max(data_d, key = lambda d : d["guard"])["guard"]
sleepys = []
for i in range(biggest_boy+1):
    sleepys.append([])
    
for d in data_d:
    guard = d["guard"]
    event = d["item"][0][0]
    minute = d["minute"]
    if event is 'f':
        sleepys[guard].append(d["minute"])
    if event is 'w':
        sleepys[guard].append(d["minute"])
for i in range(len(sleepys)):
    sleeps = sleepys[i]
    sleepys[i]=[]
    if len(sleeps)>0:
        for j in range(0,len(sleeps),2):
            sleep = sleeps[j]
            wake = sleeps[j+1]
            for k in range(sleep,wake):
                sleepys[i].append(k)

sleepiest = max(sleepys, key = lambda l : len(l))
sleepy_boy = sleepys.index(sleepiest)
sleepy_minute = max(set(sleepiest),key = sleepiest.count)
print("the sleepiest guard was guard #"+str(sleepy_boy)+" who slept on minute "+str(sleepy_minute)+" the most\nso answer 1 is "+str(sleepy_boy*sleepy_minute))
most_sleepy_minute = []
def ml(l):
    if len(l)>0:
        return(l[1])
    else:
        return(0)
for sleeps in sleepys:
    if len(sleeps)>0:
        most_sleepy = max(set(sleeps),key=sleeps.count)
        most_sleepy_sleeps = sleeps.count(most_sleepy)
        most_sleepy_minute.append([most_sleepy,most_sleepy_sleeps])
    else:
        most_sleepy_minute.append([])

minute_and_no = max(most_sleepy_minute,key= lambda l: ml(l))
guard = most_sleepy_minute.index(minute_and_no)       

print("the guard asleep on the same minute the most was guard #"+str(guard)+" on minute "+str(minute_and_no[0])+", (sleeping "+str(minute_and_no[1])+" times).\nso answer 2 is "+str(guard*minute_and_no[0])) 
    
file.close()