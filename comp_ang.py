

import numpy as np

def comp_angle(x,y,z):
    ang=(np.arctan(x/y))*180/3.14
    
    if(y>0):
        k=90-ang-90
        if(k<0):
            k=360+k
        return k
    elif(y<0):
        k=270-ang-90
        if(k<0):
            k=360+k
        return k
    elif(y==0 and x<0):
        k=90.0
        return k
    else:
        k=270.0
        return k
    
