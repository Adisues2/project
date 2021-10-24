from random import randint


t = ["Rock","paper","scissors"]

computer = t[randint(0,2)]

player = False
while player == False:

    player = input("Rock paper scissors")

    if player == computer:
       print("tie")
    elif player == "Rock":
        if computer == "paper":
            print("you loose", computer ,"covers",playere)
        else:
            print("you win",player,"smashes",computer)
    elif  player == "paper":
        if computer == "scissors":
            print("you lose ",computer,"cut",player)
        else:
            print("you win",player,"covers",computer)

    elif player == "scoissors":

        if computer  == "rock":
            print("you lose...",computer,"smashes",player)

        else:
            print("you win",player,"cut",computer)
    else:
        print("that is not a valid play.chaeck your spelling")
    palyer = False
    computer = t[randint(0,2)]











