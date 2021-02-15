# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:01:36 2020

@author: jorge
"""


def numlet(n,c):
    n=str(n)
    n+=' '
    cont=0
    newstr=''
    ini=n[0]
    for i in n:
        
        if i==ini:
            cont+=1
            continue
        
        cont=str(cont)
        newstr+=cont
        cont=int(cont)
        newstr+=ini
        cont=1
        ini=i
    print(newstr)
    if c > 0:
        c-=1
        numlet(newstr,c)
     
s='1'
print(1)
numlet(s,15)