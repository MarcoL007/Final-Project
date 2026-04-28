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
    # The code that will keep track of the number and the guesses