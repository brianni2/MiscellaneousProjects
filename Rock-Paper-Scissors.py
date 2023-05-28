from random import randint

# Create a list of play options
base_list = ["rock", "paper", "scissors"]
advanced_list = ["rock", "paper", "scissors", "lizard", "spock"]

def base_game():
    # Assign a random play
    computer = base_list[randint(0, 2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors? ").lower()
        if player == computer:
            print("Tie!")
            return 0
        elif player == "rock":
            if computer == "paper":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "paper":
            if computer == "scissors":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "scissors":
            if computer == "rock":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "quit":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input! Try again.")
            player = False
    return 0

def advanced_game():
    # Assign a random play
    computer = advanced_list[randint(0, 4)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors, Lizard, Spock? ").lower()
        if player == computer:
            print("Tie!")
            return 0
        elif player == "rock":
            if computer == "paper":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "spock":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "lizard":
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "paper":
            if computer == "scissors":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "lizard":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "rock":
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "scissors":
            if computer == "rock":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "spock":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "paper":
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "lizard":
            if computer == "rock":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "scissors":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "paper":
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "spock":
            if computer == "paper":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "lizard":
                print(f"You lose! {computer.capitalize()} beats {player}")
                return -1
            elif computer == "rock":
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
            else:
                print(f"You win! {player.capitalize()} beats {computer}")
                return 1
        elif player == "quit":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input! Try again.")
            player = False
    return 0

def game_end(player_score, computer_score, game_type):
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    if(player_score == 3):
        print("You win!")
    else:
        print("You lose!")
    print("Would you like to continue playing or start a new game?")
    choice = False
    while choice == False:
        choice = input("'continue', 'new', or 'quit': ").lower()
        if choice == "continue":
            print("You may type 'quit' at any time to exit the game.")
            while choice == "continue":
                if game_type == "base":
                    result = base_game()
                else:
                    result = advanced_game()
                if result == 1:
                    player_score += 1
                elif result == -1:
                    computer_score += 1
                print(f"Player score: {player_score}")
                print(f"Computer score: {computer_score}")
        elif choice == "new":
            main()
        elif choice == "quit":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input! Try again.")
            choice = False

def main():
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Would you like to play the base game or the advanced game?")
    print("Base game: Rock, Paper, Scissors")
    print("Advanced game: Rock, Paper, Scissors, Lizard, Spock")
    game_type = False
    while game_type == False:
        game_type = input("Enter 'base' or 'advanced': ").lower()
        if game_type == "base":
            while player_score < 3 and computer_score < 3:
                result = base_game()
                if result == 1:
                    player_score += 1
                elif result == -1:
                    computer_score += 1
                print(f"Player score: {player_score}")
                print(f"Computer score: {computer_score}")
            game_end(player_score, computer_score, game_type)
        elif game_type == "advanced":
            while player_score < 3 and computer_score < 3:
                result = advanced_game()
                if result == 1:
                    player_score += 1
                elif result == -1:
                    computer_score += 1
                print(f"Player score: {player_score}")
                print(f"Computer score: {computer_score}")
            game_end(player_score, computer_score, game_type)
        else:
            print("Invalid input! Try again.")
            game_type = False
        
main()