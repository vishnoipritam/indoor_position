

import numpy as np


def position(a,d,i,j):
    l=0
    m=0

    l=round(d*(abs(np.sin(a*3.14/180))))
    m=round(d*(abs(np.cos(a*3.14/180))))
   # print(l,m)
    if(a>=0 and a<=90):
        i=i+m
        j=j-l
    elif(a>90 and a<=180):
        i=i-m
        j=j-l
    elif(a>180 and a<=270):
        i=i-m
        j=j+l
    else:
        i=i+m
        j=j+l
    
    return int(i),int(j)