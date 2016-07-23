# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:25:41 2016

@author: nick
"""

t = int(input())
a=[]
b=[]
for i in range(0,t):
    a.append(int(input()))
l=[]
for i in a:
    l1=0
    while(i!=0):
        i=i/10
        l1+=1
    l.append(l1)
for i in range(0,t):
    x=""
    y=""
    m=""
    z=str(a[i])
    if(l[i]%2==0):
        x=z[0:l[i]/2]
        y=z[l[i]/2:]
        xr=x[::-1]
        x1=int(xr)
        x2=int(x)
        y1=int(y)
        if(x1>y1):
            b.append(x+xr)
        elif(x1==y1):
            if(x=='9'*(l[i]/2)):
                x2+=1
                x2=x2/10
                x=str(x2)
                xr=x[::-1]
                b.append(x+'0'+xr)
            else:
                x2+=1
                x=str(x2)
                y=x[::-1]            
                b.append(x+y)
        else:
            x2+=1
            x=str(x2)
            xr=x[::-1]
            b.append(x+xr)
    else:
        x=z[0:l[i]/2]
        m=z[l[i]/2:(l[i]/2)+1]
        y=z[(l[i]/2)+1:]
        xr=x[::-1]
        x1=int(xr)
        x2=int(x)
        y1=int(y)
        if(x1>y1):
            b.append(x+m+xr)
        elif(x1==y1):
            if(x=='9'*(l[i]/2)):
                x2+=1
                x=str(x2)
                xr=x[::-1]
                b.append(x+xr)
            else:    
                x2=int(m)+1
                m=str(x2)            
                b.append(x+m+y)
        else:
            x2=int(m)+1

            b.append(x+m+xr)

for i in b:
    print i,