import sys
import datetime

from wordle.game import Game
from wordle.models import GuessResult
from wordle.ui import display_board, get_user_guess, display_result
from wordle.words import load_daily_word


def main() -> None:
    # Load daily word based on current date
    target_word = load_daily_word(datetime.date.today())
    
    game = Game(target_word)
    
    while not game.is_won() and not game.is_lost():
        display_board(game.get_guesses())
        print(f"\nAttempts remaining: {game.get_attempts_remaining()}")
        
        guess = get_user_guess()
        game.guess(guess)
    
    display_board(game.get_guesses())
    display_result(game)


if __name__ == "__main__":
    main()
