# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:29:34 2018

@author: 2077969R
"""


file = open('3input.txt','r')
data = file.readlines()

def interp(item,grid):
    item = item.split(' ')
    
    i_d = list(item[0])
    del i_d[0]
    i_d = int(''.join(i_d))

    coords = item[2].split(',')
    coords[1],coords[0] =int(coords[1].split(':')[0]),int(coords[0])
    
    dims = item[3].split('x')
    dims[0],dims[1] = int(dims[0]),int(dims[1])
    
    x0 = coords[0]
    y0 = coords[1]
    xd = dims[0]
    yd = dims[1]
    

    for x in range(x0,x0+xd):
        for y in range(y0,y0+yd):
            grid[x][y].append(i_d)
    return(grid)

grid = []
for i in range(1000):
    grid.append([])
    for j in range(1000):
        grid[i].append([])
        
        
for item in data:
    grid = interp(item,grid)

count = 0
for i in range(1000):
    for j in range(1000):
        if len(grid[i][j])>1:
            count +=1
            
claimed = []
candidates = []
for i in range(1000):
    for j in range(1000):
        if len(grid[i][j])==1:
            if candidates.count(grid[i][j][0])==0:
                candidates.append(grid[i][j][0])
        if len(grid[i][j])>1:
            for item in grid[i][j]:
                if claimed.count(item)==0:
                    claimed.append(item)
                
for candidate in candidates:
    if claimed.count(candidate) ==0:
        print(candidate)
file.close()