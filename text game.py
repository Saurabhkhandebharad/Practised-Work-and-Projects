#Name: Alexander Dumbass
#Date: 26 December 2022
# description: TEXT BASED GAME IN PYTHON


import time

def Intro():
    print("Welcome to the Advenuture game - *SKILLIT*! Let's start the action!😎")
    print("You've come out of a long hiding after a zombie outbreak in your city.")
    time.sleep(4)
    print("The reason you came out is because you are out of food as well as toilet paper. You are out of things to wipe your ass with..")
    time.sleep(4)
    print("You are starving, yet you have enough power to run and retalliate if necessary.")
    print("You come out of the basement and see your house for the first time in 15 days.")
    time.sleep(4)
    print("Type your choise: search🧐 the entire house or leave🏃‍♂️ right away?")
    print()
Intro()
print(input("Type your choise: "))    

def scene2():
    time.sleep(2)
    print("You slowly open the door. It's empty. You must have thought there is zombie inside,don't you? How dare you think this game is boring???")
    time.sleep(4)
    print("(A small portal opens up a foot near your face and the creator slaps you through it.")
    time.sleep(4)
    print("now, let's continue with our story..")
    print("You look out for everything you cared for. you find H.C. VERMA's Concepts of Physics vol.1 &2,  a binocular. you put those in your backpack.")
    print("you find that you can still climb down the window and leave the house or go through the front door.")
    print("what do you choose? front door or window?")
    print()
scene2()
print(input(": "))    

def scene3():
    time.sleep(2)
    print("The streets are empty.")


scene3()
print (input(": "))

    

c1= input()
time.sleep(2)
ans ='incorrect'
while (ans=='incorrect'):
    if(c1.upper=="search"):
        print("\n YOu slowly walk toward your bedroom. you can see that its door is closed. you don't remember locking it")
        ans=='correct'
        scene2()    
    elif(c1.upper()=="leave"):
        print("putting your knife in the pocket, you pick up your axe in one hand. Keeping an eye on the street, you quickly run along the bushes")
        ans== 'correct'
        scene3()
    else:
        print("ENTER THE CORRECT CHOICE! search or leave?")
        




       

