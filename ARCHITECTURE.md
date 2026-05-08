# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- `wordle/game.py`: Core game logic - manages game state, tracks attempts, validates guesses, determines win/loss
- `wordle/words.py`: Word management - loads daily word from word list, handles word validation
- `wordle/ui.py`: Terminal UI - displays the game board, handles user input, renders colored feedback
- `wordle/__main__.py`: Entry point - initializes game and starts the main loop

## Interfaces

- `wordle/game.py`:
  - `Game(word: str)`: Constructor takes the target word
  - `guess(letter: str) -> GuessResult`: Takes a 5-letter guess, returns result with feedback
  - `is_won() -> bool`: Returns True if the player has won
  - `is_lost() -> bool`: Returns True if the player has exhausted all attempts
  - `get_attempts_remaining() -> int`: Returns number of attempts left

- `wordle/words.py`:
  - `load_daily_word() -> str`: Returns the 5-letter target word for today
  - `is_valid_word(word: str) -> bool`: Validates that a word is in the dictionary

- `wordle/ui.py`:
  - `display_board(guesses: list[GuessResult]) -> None`: Renders the game board to terminal
  - `get_user_guess() -> str`: Reads and validates user input from stdin
  - `display_result(game: Game) -> None`: Shows win/loss message with solution

- Shared data structures (passed between modules):
  - `GuessResult`: NamedTuple with fields `(guess: str, feedback: list[int], is_correct: bool)`
    - `feedback` is a list of 5 integers: 0=grey (invalid), 1=yellow (wrong position), 2=green (correct)
  - `BoardState`: List of `GuessResult` objects representing all guesses so far

## Shared Data Structures

```python
from typing import NamedTuple

class GuessResult(NamedTuple):
    guess: str           # The guessed word
    feedback: list[int]  # List of 5 integers: 0=grey, 1=yellow, 2=green
    is_correct: bool     # True if guess matches the target word
```

## External Dependencies

- Python 3.8+ (uses NamedTuple, standard library only)
- No external packages required - pure standard library implementation
