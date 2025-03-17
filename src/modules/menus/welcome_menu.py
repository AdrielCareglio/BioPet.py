"""
Welcome Menu.
This is the second element that the user encounters after the logo, with which they can interact.
This menu presents various options, including entering the game and exiting the program.
"""

from src.modules.colors_and_formats import YELLOW, RESET

def main_menu():
    print("Welcome to the 'BioPet' game. This is the main menu:")

    active_selection = True
    active_game = False
    start_game = True

    while active_selection:
        try:
            print("\n1. Game start\n2. What is this?\n3. Instructions\n4. Exit")
            menu_input = int(input("Type your option and press 'Enter': "))

            match menu_input:
                case 1:
                    print(f"\n{YELLOW}Let's start this adventure!\n{RESET}")
                    active_game = True
                    active_selection = False  # Exit menu and start the game

                case 2:
                    print(f"\n{YELLOW}In this video game, you will experience firsthand the daily mischief of cats, playing as one of them.\n"
                          f"The mini-games you will find are based on the behaviors of my two cats, Ragnar and Hecate.{RESET}")
                    active_selection = True

                case 3:
                    print(f"\n{YELLOW}The gameplay is simple.\n"
                          f"To interact with the console, you must follow the instructions on the screen and press 'Enter' to execute.{RESET}")
                    active_selection = True

                case 4:
                    print(f"\n{YELLOW}See you soon! Bye!{RESET}")
                    active_game = False
                    active_selection = False

                case _:
                    print(f"\n{YELLOW}Invalid option! Please choose a number between 1 and 4.{RESET}")

        except ValueError:
            print(f"\n{YELLOW}Invalid input! Please enter a number between 1 and 4.{RESET}")

    if (active_game == True) and (active_selection == False):
        return start_game


