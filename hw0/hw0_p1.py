# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:08:24 2021

@author: miffy
"""
#(2*x^2y+3*yz)(4*xy^2z^2)
a=[]
n = input('plz enter the polynomials : ')
s=''
m=0
for i in n:
    if i == '(' :
        m=m+1
        s=''
    elif i == ')' :
        print(s)
        a.append(s)
    else:
        s+=i        
print(a)
 
s1=''
cof=''
cofint=1
pw=1
temp=''
tempvar=''
pn=1 #判斷存+或-，預設存+
time=0
result=[[]for i in range(m)]
for i in range(len(a)) :
    time=0
    #判斷第一個是不是負號
    if a[i][0] == '-':
        pn=0
    
    for j in a[i]:
        if j == '+':
            if pn==1:
                result[i].append((s1,cofint))
            elif pn==0:
                result[i].append((s1,-cofint))
            s1=''
            cof=''
            cofint=1
            tempvar=''
            pw=1
            pn=1
        elif j == '-' and time != 0:
            if pn==1 :
                result[i].append((s1,cofint))
            elif pn==0:
                result[i].append((s1,-cofint))
            s1=''
            cof=''
            cofint=1
            tempvar=''
            pw=1
            pn=0
        elif j =='-' and time == 0:
            print()
        elif j == '*':
            cofint=int(cof)
        elif j == '^':
            print()
        elif j.isdigit():
            if (temp=='^'):
                pw=int(j)-1
                for k in range(pw):
                    s1+=tempvar
            else:
                cof+=j
        else:                   #for variables
            s1+=j
            tempvar=j
        temp=j
        time+=1
        
    if pn==1:
        result[i].append((s1,cofint))
    elif pn==0:
        result[i].append((s1,-cofint))
    s1=''
    cof=''
    cofint=1
    tempvar=''
    pw=1
    pn=1
print(result)   
        
    



