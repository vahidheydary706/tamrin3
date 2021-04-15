import random
 
p= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

computar = random.choice(p) 

print("numbers of 1 till 30")

for i in range(5):
    user = int(input())

    if computar == user:
        print("Equal")

    elif computar > user:
        print("Small")

    elif computar < user:
        print("big")
