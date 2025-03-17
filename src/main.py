"""
Main class
It runs the game flow, coordinates user interaction, narrative, and minigames.
"""

# ------ Imports  ------
from modules.ascii_art import Ascii_Art
from modules.menus import welcome_menu
from src.modules.narrative import Narrative
from src.modules.cat_selection import Cats

# ------ Global variables  ------


# ------ MAIN ------
def main():
    #Logo print
    ascii_obj = Ascii_Art()
    ascii_obj.logo()

    #Welcome menu
    welcome_menu.main_menu()

    narrative_obj = Narrative()
    narrative_obj.play_story()

    cat_selection_obj = Cats()
    cat_selection_obj.cat_sel()


if __name__ == "__main__":
    main()