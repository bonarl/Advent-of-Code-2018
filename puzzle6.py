# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:08:50 2018

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

data.sort()
min_x = data[0][0]
max_x = data[-1][0]
data.sort(key = lambda d: d[1])
min_y = data[0][1]
max_y = data[-1][1]

sizes = []
for i in range(50):
    sizes.append(0)
grid = []
for x in range(min_x,max_x):
    for y in range(min_y,max_y):
        p1 = (x,y)
        ds = []
        for loc in data:
            p2 = (loc[0],loc[1])
            i_d = loc[2]
            ds.append([distance(p1,p2),i_d])
        ds.sort()
        if ds[0][0] != ds[1][0]:
            closest_id = ds[0][1]
            sizes[closest_id] += 1
            grid.append([x,y,closest_id])
        else:
            grid.append([x,y,'.'])

size_ids = []
for i_d, size in enumerate(sizes):
    size_ids.append([size,i_d])
size_ids.sort(reverse=True)

for i,size1 in enumerate(size_ids):   
    size = size1[0]
    i_d = size1[1]
    ok = 0
    for point in grid:
        x = point[0]
        y = point[1]
        i_dc = point[2]
        if i_dc == i_d:
            if x == min_x or x == max_x or y == min_y or y == max_y:
                ok = 1
    if ok == 0:
        print("largest finite area is "+str(size))
        break
                

file.close()