# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:25:41 2016

@author: nick
"""

#string approach
#brute force approach

t = int(input())
a=[]
b=[]
for i in range(0,t):
    a.append(int(input()))
for i in a:
    i+=1
    while(True):
        l=0  
        k=i
        s=str(i)
        while(k!=0):
            k=k/10
            l+=1
        if(l%2==0):
            org=s[l/2:]
        else:
            org=s[l/2+1:]
        l=(l/2)-1
        if(org==s[l::-1]):
            b.append(i)
            break
        i=i+1
print ("Palindromes: ")
for i in b:
    print(i)