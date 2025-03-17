class Cats:
    def __init__(self):
        self.cat_input = None

    def cat_sel(self):
        self.cat_input = input("Which of the cats will you try it out with? Type H for Hecate or R for Ragnar and press 'Enter': ").lower()
        active = False
        chosen_cat = None

        while not active:
            try:
                match self.cat_input:
                    case "h":
                        print("It worked! You are now on Hecate´s body and mind")
                        chosen_cat = "Hecate"
                        active = True
                    case "r":
                        print("It worked! You are now on Ragnar´s body and mind")
                        chosen_cat = "Ragnar"
                        active = True
                    case _:
                        raise ValueError  # Si no es "h" o "r", lanza error
            except ValueError:
                print("Invalid input. Please try again. Type H or R and press 'Enter'")
                self.cat_input = input().lower()  # Se vuelve a pedir la entrada

        return chosen_cat  # Se devuelve la elección válida

    def opposite_cat(self):
        if self.cat_input == "h":
            op_cat = "Ragnar"
        else:
            op_cat = "Hecate"
        return op_cat
