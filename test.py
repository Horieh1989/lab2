
import numpy as np
import random


#read afile but file is a string
path = r"C:\Users\horie\OneDrive\Desktop\IT Höskolan projects\projects instructions\lab2\datapoints.txt"
with open(path,"r") as file:
    data=file.read()
    print(type(data))
    
    
#seperate the lines and delet the first line    
lines=data.strip().split("\n")[1:]

# line change to array or list better to array from numpy
data=np.array([list(map(float, line.split(","))) for line in lines] ) 

# last index to in
data[:,2]=data[:,2].astype(int)
print(data)
print(type(data))

#seperate last index to picho or pikachu
pichu=[d for d in data if d[2]==0]
pikachu=[d for d in data if d[2]==1]


traindata=pichu[:50]+pikachu[:50]
testdata=pichu[50:75]+pikachu[50:75]

random.shuffle(traindata)# to mix orders shuffel
random.shuffle(testdata)

print (len(traindata))
print(len(testdata))

##### calculate accuracy

k=5
lable={0:"pichu", 1:pikachu }

