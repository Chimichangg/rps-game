from gameComponents import gameVars, winLose

def moveComp(player,boss):
    if boss == player:
        print("You move was the same with the Boss, try again")
    elif boss == "rock":
        if player == "scissors":
            gameVars.player_lives -= 1
            print("\nOuch!\nBoss' Rock ---Destroyed--- Your Scissors")
        else:
            print("\nNice!\nYour Paper ---Beat--- Boss' Rock")
            gameVars.computer_lives -= 1
    elif boss == "paper":
        if player == "rock":
            gameVars.player_lives -= 1
            print("\nOuch!\nBoss' Paper ---Demolished--- Your Rock")
        else:
            print("\nNice!\nYour Scissors ---Beat--- Boss' Paper")
            gameVars.computer_lives -= 1
    elif boss == "scissors":
        if player == "paper":
            gameVars.player_lives -= 1
            print("\nOuch!\nBoss' Scissors ---Dismeantled--- Your Paper\n")
        else:
            print("\nNice!\nYour Rock ---Beat--- Boss' Scissors\n")
            gameVars.computer_lives -= 1