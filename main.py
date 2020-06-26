
import numpy as np
import pandas as pd
from har import validate
from comp_ang import comp_angle
from position import position
from location_map import location_map
from location_map import map_value

df=pd.read_csv("C:/Users/DEEPAK GUPTA/Desktop/testdata.csv")
df.drop(df.columns[[0]], axis = 1, inplace = True)
column_names = ["activity","loc_i", "loc_j", "loc_k","loc_name"]

output = pd.DataFrame(columns = column_names)

rows,cols = (100,12)
u=0
d=0
e=0
f=0
act_dict = {0:'dws',1:'jog',2:'sit',3:'std',4:'ups',5:'wlk'}
for i in range(0,1100,100):
    arr = np.zeros([rows, cols], dtype = float)

    for j in range(0,100):
        t=0
        for k in df:
            arr[j][t] = df[k][i+j]
            t=t+1
    out=np.mean(arr,axis=0)
    
    arn=arr[:, :-3]
    
    arn = arn[np.newaxis,:,:]

    act=validate(arn)
    #print(act)
    
    if(act==2 or act==3):
        new_row = {"activity" :act_dict[act],"loc_i" : d, "loc_j" : e, "loc_k" : f ,"loc_name": location_map(d,e,f) }
        output = output.append(new_row, ignore_index=True)
        continue
    elif(act==0 and map_value(d,e,f)==9):
        if(d==1):
            d=d-1
            #print("downstairing",d,e,f)
            new_row = {"activity" :act_dict[act],"loc_i" : d, "loc_j" : e, "loc_k" : f ,"loc_name": location_map(d,e,f) }
            output = output.append(new_row, ignore_index=True)
            continue
           
    elif(act==4 and  map_value(d,e,f)==9):
        if(d==0):
            d=d+1
            #print("upstairing")
            new_row = {"activity" :act_dict[act],"loc_i" : d, "loc_j" : e, "loc_k" : f ,"loc_name": location_map(d,e,f) }
            output = output.append(new_row, ignore_index=True)
            continue 
    
    ang=comp_angle(out[9],out[10],out[11])
    
    acc=round(float(np.sqrt(out[6]*out[6]+out[7]*out[7]+out[8]*out[8])),4)
    if(out[7]<0):
        acc=-acc
    v=abs(round(u+acc*2,4))
    s=abs(round((v*v-u*u)/(2*acc),4))
    print("last position",d,e,f)
    e,f=position(ang,s,e,f)
    u=v
    #print(ang,acc,v,s,d,e,f)
    #print(location_map(d,e,f))
    new_row = {"activity" :act_dict[act],"loc_i" : d, "loc_j" : e, "loc_k" : f ,"loc_name": location_map(d,e,f) }
    output = output.append(new_row, ignore_index=True)
print(output)
