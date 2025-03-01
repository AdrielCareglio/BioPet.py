"""
Welcome Menu.
This is the second element that the user encounters after the logo, with which they can interact.
This menu presents various options, including entering the game and exiting the program.
"""

def main_menu():
    print("Welcome to the 'BioPet' game. This is the main menu:")

    active_selection = True
    active_game = False

    while active_selection:
        try:
            print("\n1. Game start\n2. What is this?\n3. Instructions\n4. Exit")
            menu_input = int(input("Type your option and press 'Enter': "))

            match menu_input:
                case 1:
                    print("\nLet's start this adventure!\n")
                    active_game = True
                    active_selection = False  # Exit menu and start the game

                case 2:
                    print("\nIn this video game, you will experience firsthand the daily mischief of cats, playing as one of them.\n"
                          "The mini-games you will find are based on the behaviors of my two cats, Ragnar and Hecate.")
                    active_selection = True

                case 3:
                    print("\nThe gameplay is simple.\n"
                          "To interact with the console, you must follow the instructions on the screen and press 'Enter' to execute.")
                    active_selection = True

                case 4:
                    print("\nSee you soon! Bye!")
                    active_game = False
                    active_selection = False

                case _:
                    print("\nInvalid option! Please choose a number between 1 and 4.")

        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 4.")
