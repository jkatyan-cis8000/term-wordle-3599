# Game Module Design

## Overview

The `wordle/game.py` module implements the core game logic for Term Wordle. It manages the game state, processes player guesses, calculates feedback, and determines win/loss conditions.

## Architecture

### Class: `Game`

The `Game` class encapsulates the entire game state and logic.

#### Constructor: `__init__(word: str)`

Initializes a new game with the target word.

**Parameters:**
- `word`: The 5-letter target word (case-insensitive, converted to uppercase internally)

**State tracked:**
- `self._word`: The target word in uppercase
- `self._guesses`: List of `GuessResult` objects representing all guesses
- `self._attempts_used`: Counter for attempts made

#### Methods

**`guess(letter: str) -> GuessResult`**

Processes a player's guess and returns the result.

**Parameters:**
- `letter`: The 5-letter guess (case-insensitive, converted to uppercase)

**Returns:**
- `GuessResult` with:
  - `guess`: The processed guess word
  - `feedback`: List of 5 integers (0=grey, 1=yellow, 2=green)
  - `is_correct`: Boolean indicating if guess matches target

**`_calculate_feedback(guess: str) -> list[int]`**

Calculates feedback for a guess using Wordle's rules:

1. First pass: Mark correct position letters as green (2)
2. Second pass: Mark wrong position letters as yellow (1)
3. All other letters are grey (0)

**Key constraint:** Duplicate letters are handled correctly. If the target has one 'P' and the guess has two 'P's, only one 'P' can be yellow/green.

**`is_won() -> bool`**

Returns `True` if the last guess was correct.

**`is_lost() -> bool`**

Returns `True` if all 6 attempts have been used and the player hasn't won.

**`get_attempts_remaining() -> int`**

Returns the number of attempts left (6 - attempts_used).

**`get_guesses() -> list[GuessResult]`**

Returns a copy of all guesses made so far.

## Data Flow

```
Player Input → Game.guess() → _calculate_feedback() → GuessResult → Store
                                                        ↓
                                                 Display via UI
```

## Constraints

- Maximum 6 attempts per game
- All words converted to uppercase for consistency
- Feedback calculation follows strict Wordle rules for duplicate letters
- Game ends immediately on win (no further guesses processed)
