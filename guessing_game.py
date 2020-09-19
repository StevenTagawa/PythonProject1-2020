"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
By Steven Tagawa
September 2020
"""
import os
import random

RANGE = [10, 50, 100, 1000]
MODE_NAMES = ["Easy", "Medium", "Hard", "INSANE"]


def start_game(mode):
    answer = random.randint(1, RANGE[mode])
    guesses = 0
    os.system("cls" if "name" == "nt" else "clear")
    print("Ready to play?\n")
    if high_scores[mode]:
        print(
            f"Your current high score in {MODE_NAMES[mode].upper()} MODE is "
            f"{high_scores[mode]} {plural(high_scores[mode])}!\n")
    else:
        print(
            f"You haven't set a high score in {MODE_NAMES[mode].upper()} MODE "
            f"yet.\n")
    while True:
        guess = get_guess(guesses, answer, RANGE[mode])
        if not guess:
            return None
        else:
            guesses += 1
            if guess == answer:
                print("Woo hoo!  You got it right!")
                return guesses
            elif guess < answer:
                print("Nope!  Go higher!")
            else:
                print("Nope!  Go lower!")


def welcome():
    print("\n" + "=" * 40)
    print("Welcome to the Number Guessing Game")
    print("\nA Treehouse Python Techdegree Project")
    print("\nby Steven Tagawa")
    print("=" * 40)
    return


def goodbye():
    print("\n" + "=" * 40)
    print("Thanks for playing!  See you again soon!")
    print("=" * 40 + "\n")
    return


def plural(number):
    if number == 1:
        return "guess"
    else:
        return "guesses"


def check_score(score, high_scores, mode):
    if not score:
        return high_scores
    if high_scores[mode]:
        if score == high_scores[mode]:
            print(
                f"\nYou tied your best score in {MODE_NAMES[mode].upper()} "
                f"MODE of {high_scores[mode]} {plural(high_scores[mode])}!")
        elif score < high_scores[mode]:
            print(
                f"\nYou just beat your high score in "
                f"{MODE_NAMES[mode].upper()} MODE!")
            print(
                f"Your new high score in {MODE_NAMES[mode].upper()} MODE is "
                f"{score} {plural(score)}!")
            high_scores[mode] = score
        else:
            print(f"\nYour score was {score} {plural(score)}.")
    else:
        print(f"\nYour score was {score} {plural(score)}.")
        high_scores[mode] = score
    return high_scores


def select_mode():
    print("\n" + "=" * 40)
    print("Select Difficulty Level\n")
    for n, mode_name in enumerate(MODE_NAMES):
        option = str(n+1)+". " + mode_name + f"(1-{RANGE[n]})"
        print(
            option + (" " * (22 - len(option))) + "[High Score: " +
            str(high_scores[n]) + "]")
    print("=" * 40 + "\n")
    while True:
        mode_choice = input("What's your choice? [1-4]  ")
        if not check_empty(mode_choice):
            continue
        mode_choice = check_num(mode_choice)
        if not mode_choice:
            continue
        if not check_range(mode_choice, 1, 4):
            continue
        return mode_choice - 1


def check_num(string):
    try:
        number = int(string)
    except ValueError:
        print(f"Oops... {string} doesn't look like a number!  Try again.\n")
        return None
    return number


def check_range(number, minimum, maximum):
    if number < minimum or number > maximum:
        print(
            f"Uh oh... {number} isn't between {minimum} and {maximum}.  "
            f"Try again.\n")
        return False
    else:
        return True


def check_empty(string):
    if not string:
        print(f"You didn't enter anything!  Try again.\n")
        return False
    else:
        return True


def check_quit(guess, guesses, answer):
    if guess.lower() != "q":
        return False
    else:
        print(f"The number was {answer}.")
        print(f"You gave up after {guesses} {plural(guesses)}.")
        return True


def get_guess(guesses, answer, maximum):
    while True:
        print(f"Guess a number between 1 and {maximum}")
        guess = input(f"or enter 'Q' to give up:  ")
        if not check_empty(guess):
            continue
        if check_quit(guess, guesses, answer):
            return None
        guess = check_num(guess)
        if not guess:
            continue
        if not check_range(guess, 1, maximum):
            continue
        return guess


# EXECUTION STARTS HERE
high_scores = [None, None, None, None]
mode = None

welcome()
while True:
    if not mode:
        mode = select_mode()
    score = start_game(mode)
    high_scores = check_score(score, high_scores, mode)
    if input("\nDo you want to play again? [Y/N]  ").lower() == "y":
        if input(
            "\nDo you want to change the difficulty level? [Y/N]  "
        ).lower() == "y":
            mode = None
    else:
        break
goodbye()
# EXECUTION ENDS HERE
