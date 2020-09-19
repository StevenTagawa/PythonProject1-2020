"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
By Steven Tagawa
September 2020
"""
import random

RANGE = 10


def start_game():
    answer = random.randint(1, RANGE)
    guesses = 0
    print("Ready to play?\n")
    while True:
        guess = input(f"Guess a number between 1 and {RANGE}:  ")
        if not guess:
            print(f"You didn't enter anything!  Try again.\n")
            continue
        try:
            guess = int(guess)
        except ValueError:
            print(f"Oops... {guess} doesn't look like a number!  Try again.\n")
            continue
        # end try
        if guess < 1 or guess > RANGE:
            print(
                f"Uh oh... {guess} isn't between 1 and {RANGE}.  Try again.\n")
            continue
        # end if
        guesses += 1
        if guess == answer:
            print("Woo hoo!  You got it right!")
            return guesses
        elif guess < answer:
            print("Nope!  Go higher!")
        else:
            print("Nope!  Go lower!")
        # end if
    # end while


def welcome():
    print("\n", "=" * 40)
    print("Welcome to the Number Guessing Game")
    print("\nA Treehouse Python Techdegree Project")
    print("\nby Steven Tagawa")
    print("=" * 40)
    return
# end def


def goodbye():
    print("\n", "=" * 40)
    print("Thanks for playing!  See you again soon!")
    print("=" * 40, "\n")
    return
# end def


def plural(score):
    if score > 1:
        return "guesses"
    else:
        return "guess"
    # end if
# end def


def check_score(score, high_score):
    if high_score:
        if score == high_score:
            print(
                f"\nYou tied your best score of {high_score} "
                f"{plural(high_score)}!")
        elif score < high_score:
            print("\nYou just beat your high score!")
            print(f"Your new high score is {score} {plural(score)}!")
            high_score = score
        else:
            print(f"\nYour score was {score} {plural(score)}.")
        # end if
    else:
        print(f"\nYour score was {score} {plural(score)}.")
        high_score = score
    # end if
    return high_score
# end def


high_score = None

# EXECUTION STARTS HERE
welcome()
while True:
    score = start_game()
    high_score = check_score(score, high_score)
    if input("\nDo you want to play again? [Y/N]  ").lower() != "y":
        break
    # end if
# end while
goodbye()
# EXECUTION ENDS HERE
