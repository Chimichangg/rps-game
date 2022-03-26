from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose

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
        print("\nGoodbye Quitter\n")
        print("--------------------------------------------------------------------")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    if gameVars.computer_choice == gameVars.player_choice:
        print("You move was the same with the Boss, try again")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("\nOuch!\nBoss' Rock ---Destroyed--- Your Scissors")
        else:
            print("\nNice!\nYour Paper ---Beat--- Boss' Rock")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("\nOuch!\nBoss' Paper ---Demolished--- Your Rock")
        else:
            print("\nNice!\nYour Scissors ---Beat--- Boss' Paper")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("\nOuch!\nBoss' Scissors ---Dismeantled--- Your Paper\n")
        else:
            print("\nNice!\nYour Rock ---Beat--- Boss' Scissors\n")
            gameVars.computer_lives -= 1

    gameVars.round_number += 1

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("won")
    else:
        gameVars.player_choice = False
