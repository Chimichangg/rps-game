from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose, moveComp

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\nWelcome to Virtual Rock Paper Scissors")
print("\nGame Objective: Destroy All Boss Lives Before You Died\n")
input("Enter Anything To Start:")


while gameVars.player_choice is False:
    print("\n--------------------------------------------------------------------")
    print("\n>> Round",gameVars.round_number,"<<")
    print("\nScore:")
    print("Boss Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Your Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("\nPick Your Move") 
    gameVars.player_choice = input("Please type - rock, paper, scissors, or surrender:")

    if gameVars.player_choice == "surrender":
        print("\nGoodbye Quitter.\n")
        print("--------------------------------------------------------------------")
        exit()
    elif gameVars.player_choice == "paper" or gameVars.player_choice == "rock" or gameVars.player_choice == "scissors":     
        gameVars.computer_choice = gameVars.choices[randint(0, 2)]
        moveComp.moveComp(gameVars.player_choice,gameVars.computer_choice)
        gameVars.round_number += 1

    else:
        print("Invalid choice, try again")
        gameVars.player_choice = False

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("won")
    else:
        gameVars.player_choice = False
