import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,0,-1])
userinput=input("Enter your Choice: ")
userdict={"s":1,"w":-1,"g":0}
newdict={1:"snake",-1:"water",0:"gun"}
you=userdict[userinput]
# By now we have 2 variables, you and computer
print(f"You choose {newdict[you]}. \nComputer choose {newdict[computer]}.")
if computer == you :
    print("It is a draw")
else:
    if computer == 1 and you == -1 :
        print("You Lose!")
    elif computer == 1 and you == 0 :
        print("You Win! ")
    elif computer == -1 and you == 0 :
        print("You Lose! ")
    elif computer == -1 and you == 1 :
        print("You win! ")
    elif computer == 0 and you == 1 :
        print("You lose! ")
    elif computer == 0 and you == -1 :
        print("You win! ")
    else:
        print("Something went wrong.")
