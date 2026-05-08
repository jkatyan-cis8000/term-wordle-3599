from wordle.models import GuessResult


class Game:
    MAX_ATTEMPTS = 6

    def __init__(self, word: str):
        self._word = word.upper()
        self._guesses: list[GuessResult] = []
        self._attempts_used = 0

    def guess(self, letter: str) -> GuessResult:
        guess_word = letter.upper()
        feedback = self._calculate_feedback(guess_word)
        is_correct = guess_word == self._word
        
        result = GuessResult(
            guess=guess_word,
            feedback=feedback,
            is_correct=is_correct
        )
        
        self._guesses.append(result)
        self._attempts_used += 1
        
        return result

    def _calculate_feedback(self, guess: str) -> list[int]:
        feedback = [0] * 5
        target_chars = list(self._word)
        guess_chars = list(guess)
        
        for i in range(5):
            if guess_chars[i] == target_chars[i]:
                feedback[i] = 2
                target_chars[i] = None
        
        for i in range(5):
            if feedback[i] == 0:
                if guess_chars[i] in target_chars:
                    feedback[i] = 1
                    target_chars[target_chars.index(guess_chars[i])] = None
        
        return feedback

    def is_won(self) -> bool:
        if not self._guesses:
            return False
        return self._guesses[-1].is_correct

    def is_lost(self) -> bool:
        return self._attempts_used >= self.MAX_ATTEMPTS and not self.is_won()

    def get_attempts_remaining(self) -> int:
        return self.MAX_ATTEMPTS - self._attempts_used

    def get_guesses(self) -> list[GuessResult]:
        return list(self._guesses)
