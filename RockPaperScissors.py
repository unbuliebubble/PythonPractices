## Make a game of Rock Paper and Scissors
## Of A Player versus the Bot

import sys
import random

botChoice = ['Rock','Paper','Scissors']                                     #Listing the move the Bot can make
wCount = 0                                                                  #Counting Wins for the Player
lCount = 0                                                                  #Counting Loses for the Player
dCount = 0                                                                  #Counting Draws for the Player

input("Let's Play a game of Rock Paper and Scissors (enter to continue)")
while True:
    num = random.randint(0, 2)                                              #Making the Bot choose their move first
    move = botChoice[num]                                                   #Assigning the Bot move

    print("The Bot has played it's hand, which one do you choose ?")
    plChoice = int(input("  type '1' for 'Rock'\n"
                         "  type '2' for 'Paper'\n"
                         "  type '3' for 'Scissors'\n"
                         "player choice : "))
    if plChoice == 1:
        plChoice = "Rock"
    elif plChoice == 2:
        plChoice = "Paper"
    elif plChoice == 3:
        plChoice = "Scissors"
    else:
        print("Error")

    print("You have choosen ", plChoice, " while the bot has choose ", move,".")

    if plChoice == "Rock" and move == "Rock":
        print("Both are {}, therefore it is a draw".format(plChoice))
        dCount += 1
    elif plChoice == "Rock" and move == "Paper":
        print("{} beats {}, you lost this round".format(move, plChoice))
        lCount += 1
    elif plChoice == "Rock" and move == "Scissors":
        print("{} beats {}, you win this round".format(plChoice, move))
        wCount += 1
    elif plChoice == "Paper" and move == "Rock":
        print("{} beats {}, you win this round".format(plChoice, move))
        wCount += 1
    elif plChoice == "Paper" and move == "Paper":
        print("Both are {}, therefore it is a draw".format(plChoice))
        dCount += 1
    elif plChoice == "Paper" and move == "Scissors":
        print("{} beats {}, you lost this round".format(move, plChoice))
        lCount += 1
    elif plChoice == "Scissors" and move == "Rock":
        print("{} beats {}, your lost this round".format(move, plChoice))
        lCount += 1
    elif plChoice == "Scissors" and move == "Paper":
        print("{} beats {}, you win this round".format(plChoice, move))
        wCount += 1
    elif plChoice == "Scissors" and move == "Scissors":
        print("Both are {}, therefore it is a draw".format(plChoice))
        dCount += 1
    else:
        print("error")

    #print("Bot List : ", botChoice)                                        #To see if the botChoice list shuffled

    cont = input("Do you want to play again ? (y/n) ")
    if cont == "y" and "Y":
        print("\n Let's begin again! \n")
        random.shuffle(botChoice)
        continue
    elif cont == "n" and "N":
        print("\n Thank you for playing! \n")
        break
    else:
        sys.exit()

print("Your Wins: ",wCount)
print("Your Draws: ",dCount)
print("Your Loses: ",lCount)