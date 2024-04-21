import random

def game(x):
    guess = random.randint(1,x)
    i = 0
    while(i!=guess):
        print("enter any number between 1 to",x)
        y = int(input())
        if(y>x):
            print("Invalid input")
            break
        else:
            if(y>guess):
                print("oops ,wrong to high ")
            elif(y<guess):
                print("oops,wrong to low")
            elif(y==guess):
                print("congrats you guess correctly answer is ",y)
                i = y
                break
z = game(20)