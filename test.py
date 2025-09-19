
path=r"C:\Users\horie\OneDrive\Desktop\IT Höskolan projects\projects instructions\lab2\datapoints.txt"
with open(path, "r") as file: #https://docs.python.org/3/library/functions.html#open
    data=file.read()
    print(type(data))
    
    
lines = data.strip().split("\n")[1:] # i could use [1: ] or after line
#lines.pop(0)

data_list = [
    [float(d[0]), float(d[1]), int(d[2])]
    for line in lines
    for d in [line.split(",")]
]

print(data_list)
print(type(data_list))  