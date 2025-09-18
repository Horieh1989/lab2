import numpy as np
import matplotlib.pyplot as plt
import math as mas


path=r"C:\Users\horie\OneDrive\Desktop\IT Höskolan projects\projects instructions\lab2\datapoints.txt"
with open(path, "r") as file: #https://docs.python.org/3/library/functions.html#open
    data=file.read()
    print(type(data))
    
    
lines = data.strip().split("\n")[1:]  

data_list = [
    [float(d[0]), float(d[1]), int(d[2])]
    for line in lines
    for d in [line.split(",")]
]

print(data_list)
print(type(data_list))  



def getnewPokeman():
    width=float(input("Enter the width of the pokeman: "))
    height=float(input("Enter the height of the pokeman: "))
    return(width,height)

def distance(p, q): #https://docs.python.org/3/library/math.html#math.dist
    return mas.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

    

sighn={0:"pichu",1:"pikachu"}  
newpokman=getnewPokeman()


# Now calculate the closest point to the new Pokémon
closestto = min(data_list, key=lambda d: distance(d[:2], newpokman))

print(newpokman)
print(sighn[closestto[2]])