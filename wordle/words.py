"""Word management module for Term Wordle.

Provides functionality to load a daily 5-letter word based on the current date
and validate guesses against the dictionary of valid words.
"""

import datetime
from typing import Set

_VALID_WORDS_RAW: Set[str] = {
    "apple", "brave", "chain", "eager", "faith", "grand", "happy",
    "ideal", "joint", "lemon", "mango", "noble", "ocean", "piano",
    "quiet", "radio", "sugar", "train", "unity", "vivid", "watch",
    "yacht", "adventure", "basket", "cactus", "diamond", "elephant",
    "flavor", "guitar", "harbor", "island", "jungle", "landscape",
    "mountain", "napkin", "office", "pencil", "racoon", "salad",
    "tiger", "umbrella", "violet", "window", "amaze",
    "candy", "dancer", "eagle", "fable", "garden", "harvest", "igloo",
    "jacket", "kite", "lantern", "magnet", "nugget", "orbit", "parrot", "quilt",
    "rabbit", "snail", "tornado", "valley", "whale", "yogurt", "zoology"
}

# Filter to only 5-letter words
_VALID_WORDS: Set[str] = {w for w in _VALID_WORDS_RAW if len(w) == 5}

_DAYS_OFFSET: int = 5


def _get_date_seed(date: datetime.date = None) -> int:
    """Calculate a seed value from the date for deterministic word selection."""
    if date is None:
        date = datetime.date.today()
    days_since_epoch = date.toordinal()
    return days_since_epoch + _DAYS_OFFSET


def load_daily_word(date: datetime.date = None) -> str:
    """Load the daily 5-letter word based on the current date.
    
    Args:
        date: Optional date to use instead of today's date.
        
    Returns:
        A 5-letter word from the valid words list.
    """
    seed = _get_date_seed(date)
    words_list = list(_VALID_WORDS)
    index = seed % len(words_list)
    return words_list[index]


def is_valid_word(word: str) -> bool:
    """Check if a word is in the dictionary of valid 5-letter words.
    
    Args:
        word: The word to validate.
        
    Returns:
        True if the word is valid, False otherwise.
    """
    return word.lower() in _VALID_WORDS
