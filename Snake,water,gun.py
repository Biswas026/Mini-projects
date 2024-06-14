import random

def Game(list):
    print("Enter your desired choice")
    a = int(input("1.Snake      2.Water       3.Gun"))
    Computer=random.randint(1,3)
    l=[0,"Snake","Water","Gun"]
    print(f"Computer choose {l[Computer]}")
    if(list[a-1][Computer]=="w"):
        print("Player Win")
        global Player_score
        Player_score=Player_score + 1

    elif(list[a-1][Computer]=="d"):
        print("Draw")

    else:
        print("Computer Win")
        global Computer_score
        Computer_score=Computer_score + 1
    print(" Do you want to?  \n  1.PLAY   2.QUIT \n")




Player_score=0
Computer_score=0
print("Welcome, to Snake Water Gun game")
print("1.PLAY   2.QUIT")
list=[[0,"d","w","l"],[0,"l","d","w"],[0,"w","l","d"]]
while(True):
    choice=int(input("Enter your choice \n"))
    if choice==1:
        Game(list)
    elif choice==2:
        break
    else:
        raise ValueError("Please Enter Correct value")

print(f"Score of Player is {Player_score} and the Score of Computer is {Computer_score}")








