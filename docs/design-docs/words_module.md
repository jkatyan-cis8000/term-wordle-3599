# Word Management Module

This document describes the `wordle/words.py` module, which handles word loading and validation for the Term Wordle game.

## Overview

The module provides two core functions:
- `load_daily_word()` - Returns the 5-letter target word for the current day
- `is_valid_word()` - Validates that a guess is in the dictionary of valid words

## Implementation Details

### Word List

The module embeds a set of ~100 valid 5-letter English words directly in the source code. This approach:
- Requires no external dependencies
- Works offline
- Keeps the codebase simple and self-contained
- Ensures consistent behavior across environments

### Daily Word Selection

The daily word is selected deterministically based on the current date using this algorithm:

1. Calculate the number of days since the Unix epoch
2. Add a constant offset (_DAYS_OFFSET = 5) to avoid edge cases
3. Use modulo arithmetic to select an index from the word list

This ensures that:
- The same date always produces the same word
- Words cycle through the list evenly
- The word changes at midnight (local time)

### Validation

Word validation is straightforward - the input word is converted to lowercase and checked against the `_VALID_WORDS` set. This provides O(1) lookup time and handles case-insensitive matching.

## Usage Examples

```python
from wordle.words import load_daily_word, is_valid_word

# Get today's target word
target = load_daily_word()

# Validate a guess
if is_valid_word("apple"):
    print("Valid word!")
```

## Non-Obvious Constraints

- All words in the dictionary must be exactly 5 letters
- The word list is static and embedded (no external file loading)
- Date-based selection uses local time, not UTC
- Validation is case-insensitive but returns True only if the lowercase version matches