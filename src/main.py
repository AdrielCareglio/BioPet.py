"""
Main class
It runs the game flow, coordinates user interaction, narrative, and minigames.
"""

# ------ Imports  ------
from modules.ascii_art import Ascii_Art
from modules.menus import welcome_menu
from src.modules.narrative import Narrative

# ------ Global variables  ------

# - Colors and format -

# Reset (Reset color)
RESET = "\033[0m"

# Text colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Text styles
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
BLINKING = "\033[5m"
INVERTED = "\033[7m"
HIDDEN = "\033[8m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


def main():
    #Logo print
    ascii_obj = Ascii_Art(RESET, BLUE, GREEN)
    ascii_obj.logo()

    #Welcome menu
    welcome_menu.main_menu()

    narrative_obj = Narrative
    narrative_obj.intro(YELLOW, RESET)








if __name__ == "__main__":
    main()