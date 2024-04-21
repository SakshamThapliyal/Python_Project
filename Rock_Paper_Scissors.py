import random

def play():
    user = input("'r' for rock ,'p' for paper ,'s' for sisser\n")
    computer = random.choice(['r','p','s'])
    if(user==computer):
        print("its a tie")
    elif(user=='r' and computer=='s')or(user=='p' and computer=='r')or(user=='s' and computer=='p'):
        print("you win")
    else:
        print("you lose")

play()
