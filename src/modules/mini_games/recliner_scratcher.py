"""
In this mini-game, the player must scratch a recliner while avoiding being caught by humans. The game includes the following mechanics:

    - Lives system: the player begins with a set number of lives. Each time the player is caught by a human, a life is lost.
    - Time limit: the game has a fixed duration, and the player must complete the task within this time frame.
        If the time expires before the player scratches the recliner, the game ends.
    - Goal: The player must avoid humans and successfully scratch the recliner to score points. The game ends when the player either loses all lives or runs out of time.
"""
from src.modules.colors_and_formats import RED, YELLOW, RESET, ITALICA, CYAN, MAGENTA
from src.modules.cat_selection import Cats
from src.modules.cat_colors import Cats_Colors

import random

def scratcher_game():
    recliner_instructions()
    scratcher_dynamics()

def recliner_instructions():
    print(f"{ITALICA}{op_cat_color} -{op_cat}It´s time to face our worst enemy, the recliner. When we lean on it´s back to scratch and sharpen our claws, it leans back to scares us. WE'VE GOT TO GIVE IT WHAT IT DESERVES .'{RESET}")

    print(f"{ITALICA}{op_cat_color} -{op_cat} You must scratch the recliner. Be careful, we might get caught! We'll have to play it cool when the humans come. LET´S GO!")

    print(f"{YELLOW} Press {CYAN}'Enter'{YELLOW} to {CYAN}scratch{YELLOW} and {MAGENTA}meow{YELLOW} to {MAGENTA}play it cool{YELLOW}. ")

    print(f"{YELLOW}You have 20 seconds, and the countdown starts when you press {CYAN}Enter{YELLOW}. Good luck!")

def scratcher_dynamics():






