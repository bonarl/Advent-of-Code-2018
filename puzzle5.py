# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 08:22:01 2018

@author: bonar
"""

file = open('5input.txt','r')
data1 = list(file.readlines()[0])
letters = list(set(data1))
letters.sort()
lens = []
for cell in letters[0:26]:
    data = []
    for l in data1:
        if l != cell and l!= cell.lower():
            data.append(l)
    x=0
    data2=[]
    while x==0:
        react = 0
        dels = []
        data2=[]
        for i,one in enumerate(data[0:-1]):
            two = data[i+1]
            if one.capitalize() == one:
                onecase = 2
            else:
                onecase = 1
            if two.capitalize() == two:
                twocase = 2
            else:
                twocase = 1
            if one.lower() == two.lower() and onecase != twocase and i not in dels:
                dels.append(i)
                dels.append(i+1)
                react +=1       
        for j,letter in enumerate(data):
            if j not in dels:
                data2.append(letter)
        data = data2
        if react == 0:
            x=1
    print(cell,len(data))
    lens.append([len(data),cell])
lens.sort()
print(lens)
file.close()