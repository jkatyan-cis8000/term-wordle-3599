import sys

from wordle.game import Game
from wordle.models import GuessResult


ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_GREY = "\033[90m"
ANSI_RESET = "\033[0m"


def display_board(guesses: list[GuessResult]) -> None:
    for guess_result in guesses:
        print(_format_guess(guess_result))
    for _ in range(6 - len(guesses)):
        print(" ".join(["_"] * 5))


def _format_guess(guess_result: GuessResult) -> str:
    formatted = []
    for i, char in enumerate(guess_result.guess):
        color = _get_color(guess_result.feedback[i])
        formatted.append(f"{color}{char}{ANSI_RESET}")
    return " ".join(formatted)


def _get_color(feedback: int) -> str:
    if feedback == 2:
        return ANSI_GREEN
    elif feedback == 1:
        return ANSI_YELLOW
    else:
        return ANSI_GREY


def get_user_guess() -> str:
    while True:
        try:
            user_input = input("Enter your 5-letter guess: ").strip().lower()
            if len(user_input) != 5:
                print("Please enter exactly 5 letters.")
                continue
            if not user_input.isalpha():
                print("Please enter only letters.")
                continue
            return user_input
        except EOFError:
            print("\nGame interrupted.")
            sys.exit(0)


def display_result(game: Game) -> None:
    if game.is_won():
        print(f"\n{ANSI_GREEN}Congratulations! You won!{ANSI_RESET}")
    else:
        print(f"\n{ANSI_GREY}Game over!{ANSI_RESET}")
    print(f"The word was: {ANSI_GREEN}{game._word}{ANSI_RESET}")
