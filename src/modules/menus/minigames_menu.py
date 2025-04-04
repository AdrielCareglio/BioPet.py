"""Class for choosing the minigame to participate in according to the chosen room or action"""
from src.modules.colors_and_formats import RESET, RED, YELLOW
from src.modules.mini_games.recliner_scratcher import scratcher_game
from src.modules.shared.state import state

def games_menu(chosen_cat, op_cat, m_cat_color, op_cat_color):

    active_menu = True

    while active_menu:

        try:
            print(f"1. Living Room\n2. Hallway\n3. Bedroom\n4. Treasures Chest\n5. Go back to human body")
            action_input = int(input(f"{YELLOW}Type the number and press enter:{RESET} "))

            match action_input:
                case 1:
                    state.lives_left = scratcher_game(chosen_cat, op_cat, m_cat_color, op_cat_color)
                    active_menu = False
                case 2:
                    print("Hallway")
                    active_menu = False
                case 3:
                    print("Bedroom")
                    active_menu = False
                case 4:
                    print("Treasures Chest")
                    active_menu = False
                case 5:
                    print("You are back to your human body")
                    active_menu = False
                case _:
                    print(f"¨{RED}Choose a number from 1 to 5:{RESET} ")

        except ValueError:
            print(f"{RED}Invalid. Please, type a number between 1 and 5 and press Enter{RESET}")
            active_menu = True



