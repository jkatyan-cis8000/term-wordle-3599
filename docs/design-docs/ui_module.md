# UI Module Design

## Overview

The `wordle/ui.py` module provides terminal user interface functionality for Term Wordle. It displays the game board with ANSI color coding, reads user input, and shows game results.

## Architecture

### ANSI Color Codes

The module uses the following ANSI escape codes:

- **Green** (correct position): `\033[32m`
- **Yellow** (wrong position): `\033[33m`
- **Grey** (invalid): `\033[90m`
- **Reset**: `\033[0m`

### Functions

**`display_board(guesses: list[GuessResult]) -> None`**

Renders the game board to the terminal.

**Behavior:**
- For each guess in the list, displays the formatted guess
- Displays empty rows (5 underscores) for unused attempts
- Maximum 6 rows total

**`_format_guess(guess_result: GuessResult) -> str`**

Formats a single guess with ANSI color codes.

**Parameters:**
- `guess_result`: A `GuessResult` object containing the guess and feedback

**Returns:**
- Formatted string with color-coded letters separated by spaces

**Example output:**
```
[32mP[0m [33mA[0m [90mP[0m [32mL[0m [33mE[0m
```

**`_get_color(feedback: int) -> str`**

Returns the appropriate ANSI color code for a feedback value.

**Parameters:**
- `feedback`: Integer (0, 1, or 2)

**Returns:**
- ANSI color escape code

**`get_user_guess() -> str`**

Reads and validates user input from stdin.

**Validation:**
- Exactly 5 characters
- Only alphabetic characters (a-z, A-Z)

**Error handling:**
- Prompts user to re-enter if validation fails
- Handles EOFError gracefully (exits with message)

**`display_result(game: Game) -> None`**

Shows the final game result.

**Behavior:**
- Displays the final board state
- Shows win message (green text) if won
- Shows game over message (grey text) if lost
- Reveals the target word (green text)

## Data Flow

```
Game State → display_board() → ANSI formatted output → Terminal
                   ↓
get_user_guess() ← Terminal input ← User
                   ↓
        Validation + Return
```

## Constraints

- ANSI codes may not display properly in all terminal environments
- Input validation is basic (length and alphabetic only)
- No dictionary validation at UI level (delegated to game/words modules)
- EOF handling exits the program cleanly
