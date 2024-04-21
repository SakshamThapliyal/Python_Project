import random

x = int(input("enter the number between 1 to 12\n"))
i=0
while(i!=x):
    com=random.randint(1,12)
    if(x>12):
        print("Invalid input")
        break
    else:
        if(com>x):
            print("oops,wrong to high")
        elif(com<x):
            print("oops,wrong to low")
        elif(com==x):
            print("congrats you guess correctly answer is ",com)
            i =com
