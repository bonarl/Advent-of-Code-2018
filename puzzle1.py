# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

file = open('1input.txt','r')
data = file.readlines()

def check(data):
    f = 0
    f_pos_index = []
    f_minus_index = []
    loop = 0
    while True:
        loop +=1
        for item in data:
            f += int(item)
            if f < 0:
                if len(f_minus_index)<(-f):
                    for i in range((-f)-len(f_minus_index)):
                        f_minus_index.append(0)
                if f_minus_index[-f-1]==1:
                    return(f,loop)
                f_minus_index[-f-1] = 1
            if f >= 0:
                if len(f_pos_index)<f+1:
                    for i in range(f-len(f_pos_index)+1):
                        f_pos_index.append(0)
                if f_pos_index[f]==1:
                    return(f,loop)
                f_pos_index[f] = 1
file.close()
print(check(data))