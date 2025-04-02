class Cats_Colors:
    def __init__(self, chosen_cat, op_cat):
        self.chosen_cat = chosen_cat
        self.op_cat = op_cat

    def main_cat_color(self, chosen_cat):
        self.chosen_cat = chosen_cat
        if chosen_cat == "Ragnar":
            m_cat_color =  "\033[34m"
        else:
            m_cat_color = "\033[32m"

        return m_cat_color

    def op_cat_color(self, op_cat):
        self.op_cat = op_cat
        if op_cat == "Ragnar":
            op_cat_color = "\033[34m"
        else:
            op_cat_color = "\033[32m"
        return op_cat_color

