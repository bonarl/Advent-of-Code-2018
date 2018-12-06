# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:49:36 2018

@author: bonar
"""

def distance(p1,p2):
    d = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    return(d)

file = open('6input.txt','r')
data1 = file.readlines()
data = []
for i,c in enumerate(data1):
    c = c.split(',')
    data.append([int(c[0]),int(c[1]),i])
    
xtra = 200
min_x = data[0][0]-xtra
max_x = data[-1][0]+xtra
data.sort(key = lambda d: d[1])
min_y = data[0][1]-xtra
max_y = data[-1][1]+xtra

max_d  = 10000
region_size = 0
for x in range(min_x,max_x):
    for y in range(min_y,max_y):
        p1 = (x,y)
        d = 0
        for p2 in data:
            p2 = p2[0:2]
            d += distance(p1,p2)
        if d < max_d:
            region_size += 1
    
print("size of largest region containing all locations with total distance to all given coordinates less than 10000 is "+str(region_size))
file.close()