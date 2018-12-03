# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:53:33 2018

@author: 2077969R
"""

file = open('2input.txt','r')
data = file.readlines()

def checksum(item):
    uniques = []
    for letter in item:
        if uniques.count(letter)==0:
            uniques.append(letter)
    counts = []
    for letter1 in uniques:
        count = 0
        for letter2 in item:
            if letter1 == letter2:
                count +=1
        counts.append(count)
    twos = 0
    threes = 0
    for count in counts:
        if count == 2:
            twos =1
        if count == 3:
            threes = 1
    return(twos,threes)
    
twos = 0
threes = 0
for item in data:
    check = checksum(item)
    twos += check[0]
    threes += check[1]
for item1 in data:
    for item2 in data:
        if item1 != item2:
            for i in range(len(item1)):
                item11 = list(item1)
                del item11[i]
                for j in range(len(item2)):
                    item22 = list(item2)
                    del item22[j]
                    if item11 == item22:
                        print(''.join(item11))
                        break
                
file.close()