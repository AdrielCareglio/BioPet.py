
"""
Welcome Menu.
This is the second element that the users encounters after the logo, with which they can interact.
This menu presents various options, including entering the game and exiting the program.
"""

def main_menu():

        print("Welcome to the 'BioPet' game. This is the main menu:")


        active_selection = True
        active_game = False

        while active_selection and not active_game:
            try:
                print("1. Game start\n2. What is this?\n3. Instructions\n4. Exit")
                menuInput = int(input("Type your option and press 'Enter'"))

                match menuInput:
                    case 1:
                        print("\nLet´s start this adventure!\n")
                        active_game = True
                        active_selection = False
                        return True

                    case 2:
                        print("\n What is this?\nIn this video game, you will experience firsthand the daily mischief of cats, playing as one of them.\nThe mini-games you will find are based on the behaviors of my two cats, Ragnar and Hecate\n")
                        active_selection = True
                        active_game = False
                    case 3:
                        print("\nInstructions:\nThe gameplay is simple. To interact with the console, you must follow the instructions on the screen and press 'Enter' to execute.\n")
                        active_selection = True
                        active_game = False
                    case 4:
                        print("\nSee you soon! Bye!\n")
                        active_game = False
                        active_selection = False


            except ValueError:
                print("Error, please type a number between 1 and 4 and press 'Enter'.")
                active_selection = True
                active_game = False





