import random

pc_wins = 0
player_wins = 0
games_played = 0

options = ['rock', 'paper', 'scissors']

while True:
    print("Type rock, paper or scissors to play, or q to quit: ")
    player_choice = input().lower()
    if player_choice == 'q':
        break
    
    games_played += 1
    
    if player_choice not in options:
        print("That's not a valid input.")
        continue

    pc_pick = options[random.randint(0, 2)]         # random index pick from options
    print("Computer picked", pc_pick + ".")
    if player_choice == pc_pick:
        print("it's a tie!")

    elif player_choice == 'rock' and pc_pick == 'scissors':
        print("You won!")
        player_wins += 1

    elif player_choice == 'paper' and pc_pick == 'rock':
        print("You won!" )
        player_wins += 1

    elif player_choice == 'scissors' and pc_pick == 'paper':
        print("You won!" )
        player_wins += 1

    else:
        print("You lost!" )
        pc_wins += 1
    

print("You played", games_played, "games.")
print("You won", player_wins, "times, and lost", pc_wins, "times.")
print("Goodbye!")
