import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import urllib.request


max_ask=3
Try=0



# GitHub raw URL
url = "https://raw.githubusercontent.com/Horieh1989/lab2/refs/heads/main/datapoints.txt"

# Open and read the file from the internet
with urllib.request.urlopen(url) as response:
    data = response.read().decode("utf-8")  # Convert bytes → string
    print(type(data))
    
lines = data.strip().split("\n")[1:] # i could use [1: ] or after line #https://docs.python.org/3/library/stdtypes.html#str.strip
#lines.pop(0)

data_list = [
    [float(d[0]), float(d[1]), int(d[2])]
    for line in lines
    for d in [line.split(",")]
]

print(data_list)
print(type(data_list))  


print("welcome to pokeman")

    
    
def getnewPokeman():
    while True:
        try: #for number and negative number
            width_number = float(input("Enter the width of the pokeman: "))
            height_number = float(input("Enter the height of the pokeman: "))
            if width_number<=0 and height_number <=0:#for negative number
               print("you should add a positive number")
               continue
               
           
           
            return (width_number, height_number)
            
        except ValueError:#https://docs.python.org/3/tutorial/errors.html#handling-exceptions
            print("Please enter valid positive numbers for width and height.")
    
         
 

sighn={0:"pichu",1:"pikachu"}  

k=15  #how many nearest neighbor

weightandhight_arry=np.array([d[:2]for d in data_list])
labels=np.array([d[2] for d in  data_list])


while max_ask>Try:
  newpokman=getnewPokeman()
  
#https://docs.python.org/3/library/math.html#math.dist
  distances=np.sqrt(np.sum((weightandhight_arry -  newpokman)**2, axis=1))#sum each row axis=1
  nearest= distances.argsort()[:k]
  
  votes={0:0,1:0}
  for idx in nearest :
      votes[labels[idx]]+=1
      
  
  predicted_label = max(votes, key=votes.get)
  print(f"\nNew Pokémon size: {newpokman}")
  print(f"Predicted Pokémon: {sighn[predicted_label]}")
  
  #preper the array for plot
  pichup= weightandhight_arry[labels==0]
  pikachup= weightandhight_arry[labels==1]

  #make the plot nam weight and hight and lable
  plt.scatter(pichup[:,0],pichup[:,1],color="blue", label="pichu")
  plt.scatter(pikachup[:,0],pikachup[:,1], color="red" ,label="pikachu")
  #new pokeman
  plt.scatter(newpokman[0],newpokman[1],color="pink",marker="*",s=100,label="newpokman" )
  plt.title("pokemans and new pokeman")
  plt.xlabel("width")
  plt.ylabel("height")
  plt.show()
  input("Press Enter to exit...")

  Try+=1
  if max_ask>=Try:
      while True:
        askAgain=input("do you want to try again? ").strip().lower()
        if askAgain=="yes":
            print("you must enter the right digit")
            break
        elif askAgain=="no":
           print("you go out of program")
           exit()
        else:
            print("invalid try again: ")
     
else:
    print("you have done 3 try!")
    
    

