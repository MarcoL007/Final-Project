import random
    # Starting by creating the settings first
def get_game_setttings():
    settings = {"Easy": {"limit": 10, "attempts": 5},
                "Medium": {"limit": 50, "attempts": 6},
                "Hard": {"limit": 100, "attempts": 6}   }
            #Creating a Dictionary for the levels and attempts

    print("---Select Difficulty---")
    for lvl in settings:
        print(f"- {lvl}")
    difficulty = input("Enter Choice: ").capitalize()

    # Checking for invalid inputs when selecting the level
    if difficulty not in settings:
        print("Invalid Input, Defalting to Easy.")
        return settings["Easy"]
    return settings[difficulty]

def run_guessing_session():
    # The code that will keep track of the number and the guesses.
    config = get_game_setttings()
    target_num = random.randint(1, config["limit"])
    max_attempts = config['attempts']
    attempts = 0
    win = False
    # This gets the random number, starts attempt count and gets the setting that will be used.

    print(f"\n I'm thinking of a number between 1 and {config['limit']}.")
    print(f"You have {max_attempts} attempts! Can you guess correctly?")

    # This loop will continue till the user runs out of attempts or guesses correctly
    while attempts < max_attempts and not win:
        user_guess = input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter guess: ")
        if user_guess.isdigit():
            guess = int(user_guess)
            attempts += 1
            if guess < target_num:
                print("Too Low")
            elif guess > target_num:
                print("Too High")
            else:
                win = True
        else:
            print("Invalid input. Enter a whole number")
    if win == True:
        print(f"COngratulations! You got it in {attempts}")
    else:
        print(f"Better luck next time the correct number was {target_num}")
    # the loop checks if the guess is higher and lower and if out of attempts ends the game

def main():
    #creating the ability to replay and start the game 
    print("---Welcome to Guess The Number---")
    print(' How well is your intuition ready to find out??')
    playing = True
    #So while playing is True that will mean you are playing the game which will make the session run.
    while playing:
        run_guessing_session()
        repeat = input("\nWould you like to play again? (Yes/No): ").capitalize()
        if repeat != "Yes":
            playing = False
        
    print("Thank You For Playing!")
    print("Guess The Number 2... coming soon")

if __name__ == "__main__":
    main()

    