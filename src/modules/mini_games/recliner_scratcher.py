"""
In this mini-game, the player must scratch a recliner while avoiding being caught by humans. The game includes the following mechanics:

    - Lives system: the player begins with a set number of lives. Each time the player is caught by a human, a life is lost.
    - Time limit: the game has a fixed duration, and the player must complete the task within this time frame.
        If the time expires before the player scratches the recliner, the game ends.
    - Goal: The player must avoid humans and successfully scratch the recliner to score points. The game ends when the player either loses all lives or runs out of time.
"""

from src.modules.shared.state import state
from src.modules.colors_and_formats import RED, YELLOW, RESET, ITALICA, CYAN, MAGENTA


import random
import time

def scratcher_game(chosen_cat, op_cat, m_cat_color, op_cat_color):
    recliner_instructions(op_cat, op_cat_color)
    scratcher_dynamics(chosen_cat, op_cat, m_cat_color, op_cat_color)
    return state.lives_left

def recliner_instructions(op_cat, op_cat_color):
    print(f"{ITALICA}{op_cat_color}: -{op_cat}It´s time to face our worst enemy, the recliner. When we lean on it´s back to scratch and sharpen our claws, it leans back to scares us. WE'VE GOT TO GIVE IT WHAT IT DESERVES .'{RESET}")

    print(f"{ITALICA}{op_cat_color}: -{op_cat} You must scratch the recliner. Be careful, we might get caught! We'll have to play it cool when the humans come. LET´S GO!{RESET}")

    print(f"{YELLOW} Press {CYAN}'Enter'{YELLOW} to {CYAN}scratch{YELLOW} and {MAGENTA}meow{YELLOW} to {MAGENTA}play it cool{RESET}. ")


def scratcher_dynamics(chosen_cat, op_cat, m_cat_color, op_cat_color):

    print(f"{YELLOW}You have 20 seconds and {state.lives_left} lives. The countdown starts when you press {CYAN}Enter{YELLOW}. Good luck!")
    input()

    active = True
    scratch_count = 0
    meow_count = 0
    start_time = time.time()
    TIME_LIMIT = 30
    next_interrupt = time.time() + random.randint(1,5)


    while active and state.lives_left > 0:
        current_time = time.time()

        #End game if time runs out
        if current_time - start_time >= TIME_LIMIT:
            print(f"{YELLOW}No time left!{RESET}")
            active = False

        elif current_time >= next_interrupt:
            print(f"{op_cat_color}{ITALICA}Someone´s coming! Type 'meow' and press 'Enter' to play it cool{RESET}")
            user_input = input().strip()

            if user_input == "meow":
                print(f"{op_cat_color}{ITALICA}Great, keep going!{RESET}")
                meow_count += 1
                next_interrupt = time.time() + random.randint(1,5)

            else:
                state.lives_left -= 1
                print(f"{RED}-1 life. Lives remaining: {state.lives_left}")

                if state.lives_left == 0:
                    print(f"{RED}OH NO! You´re out of lives.{RESET}")
                    active = False

        else:
            print(f"{op_cat_color}{ITALICA}Scratch now! (Press Enter){RESET}")
            user_input = input()

            if user_input == "":
                scratch_count += 1
            else:
                state.lives_left -= 1
                print(f"{YELLOW}Press blank 'Enter', -1 life. Lives remaining: {state.lives_left}")

                if state.lives_left == 0:
                    print(f"{YELLOW}OH NO! You´re out of lives.{RESET}")
                    active = False

    if state.lives_left > 0:
        print(f"{op_cat_color}{ITALICA}{op_cat}: Woho! We did it! The recliner won´t scare us again any time soon!{RESET}")
        print(f"{YELLOW}Total scratches: {scratch_count}, succesful distractions: {meow_count} and lives left: {state.lives_left}")

        end_message = ("You´re a natural, " if scratch_count >= 20 else "Not bad, ")
        print(op_cat_color+ITALICA+ end_message + chosen_cat + RESET)

        time.sleep(0.1)

    return state.lives_left














