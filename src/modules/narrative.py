"""
Class that introduces the main narrative of the game.
Uses ASCII formatted text and art to create an immersive experience.
"""

from src.modules.ascii_art import Ascii_Art
from src.modules.colors_and_formats import YELLOW, RESET


class Narrative:
    def __init__(self):
        self.YELLOW = YELLOW
        self.RESET = RESET
        self.ascii_art = Ascii_Art()


    def chilling(self):
        print(f"{YELLOW} After a long day, you're relaxed at home watching TV.{RESET}")
        self.ascii_art.armchair()

    def asleep(self):
        print(f"{YELLOW}Exhausted, you start to fall asleep with the ads. But, all of a sudden, one wakes you up...{RESET}")
        self.ascii_art.tv()

    def add(self):
        print(f"{YELLOW}Want to know what it feels like and how your pet lives? Introducing BioPet! The ultimate experience to connect with your furry best friend.\n Discover their world, understand their day-to-day life and improve their quality of life like never before. The BioPet has a comfortable wrist watch format, just lift its lid and put some hair of the pet whose mind you want to occupy.{RESET}")
        self.ascii_art.bio_pet()

    def buy(self):
        print(f"{YELLOW}You love it and buy it immediately to try it out with your two cats, Hecate and Ragnar. DING DONG! The doorbell has rung and the package is here. Such a fast delivery, right?\nIt's time to put it to the test.{RESET}")
        self.ascii_art.characters_info()

    def play_story(self):
        Narrative.chilling(self)
        Narrative.asleep(self)
        Narrative.add(self)
        Narrative.buy(self)




