"""
Class that introduces the main narrative of the game.
Uses ASCII formatted text and art to create an immersive experience.
"""

from modules.ascii_art import Ascii_Art

from src.main import YELLOW, RESET


class Narrative:

    def __init__(self):
        YELLOW.self = YELLOW
        RESET.self = RESET


    def intro(self):
        print(f"{YELLOW} After a long day, you're relaxed at home watching TV.{RESET}")
        ob_tv = Ascii_Art
        Ascii_Art.tv()



