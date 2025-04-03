"""
Main class
It runs the game flow, coordinates user interaction, narrative, and minigames.
"""

# ------ Imports  ------
from modules.ascii_art import Ascii_Art
from modules.menus import welcome_menu
from src.modules.colors_and_formats import YELLOW, RESET, ITALICA
from src.modules.menus.minigames_menu import games_menu
from src.modules.narrative import Narrative
from src.modules.cat_selection import Cats
from src.modules.cat_colors import Cats_Colors
from src.modules.menus import minigames_menu


# ------ Global variables  ------
LIVES = 9


# ------ MAIN ------
def main():
    #Logo print
    ascii_obj = Ascii_Art()
    ascii_obj.logo()

    #Welcome menu
    active_game = welcome_menu.main_menu()

    if not active_game:
        print("")
        return
    #Game start
    else:
        #Intro narrative
        narrative_obj = Narrative()
        narrative_obj.play_story()

        #User chooses the character to play with
        cat_selection_obj = Cats(LIVES)
        chosen_cat = cat_selection_obj.cat_sel()
        op_cat = cat_selection_obj.opposite_cat()

        #Sets text color according to character
        cat_colors_obj = Cats_Colors(chosen_cat, op_cat)
        m_cat_color = cat_colors_obj.main_cat_color(chosen_cat)
        op_cat_color = cat_colors_obj.op_cat_color(op_cat)

        print(f"{YELLOW}Both cats were asleep together. You leaped up in {m_cat_color}{chosen_cat}´s{YELLOW} body and { op_cat} got scared. {RESET}\n")

        print(f" {ITALICA}{op_cat_color} -{op_cat}: Meow, you nearly made my heart stop {chosen_cat}! But well, it´s still time to wake up. *stretches*. Where do you want to go?{RESET}")

        #Minigames menu
        games_menu()


if __name__ == "__main__":
    main()