from typing import NamedTuple

class GuessResult(NamedTuple):
    guess: str
    feedback: list[int]
    is_correct: bool
