from src.modules.colors_and_formats import RED
from src.modules.shared.state import state


class Cats:
    def __init__(self):
        self.cat_input = None
        self.lives = state.lives_left


    def cat_sel(self):
        self.cat_input = input("Which of the cats will you try it out with? Type H for Hecate or R for Ragnar and press 'Enter': ").lower()

        active = False
        chosen_cat = None

        while not active:
            try:
                match self.cat_input:
                    case "h":
                        print(f"It worked! You are now on Hecate´s body and mind. You have {self.lives} lives, good luck Hecate! ")
                        chosen_cat = "Hecate"
                        active = True
                    case "r":
                        print(f"It worked! You are now on Ragnar´s body and mind.  You have {self.lives} lives, good luck Ragnar! ")
                        chosen_cat = "Ragnar"
                        active = True
                    case _:
                        raise ValueError  # If the input is different to r or h, error
            except ValueError:
                print(f"{RED}Invalid input. Please try again. Type H or R and press 'Enter'")
                self.cat_input = input().lower()  # Asks for a new input

        return chosen_cat

    def opposite_cat(self):
        if self.cat_input == "h":
            op_cat = "Ragnar"
        else:
            op_cat = "Hecate"
        return op_cat
