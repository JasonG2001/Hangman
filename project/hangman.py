class Hangman:

    def __init__(self):

        self.lives = 6


    def get_length_of_word(self, word: str) -> int:

        return len(word)


    def ask_for_word(self, word: str) -> str:

        return word


    def ask_for_letter(self, letter_guessed: str) -> str:

        return letter_guessed


    def check_if_letter_in_word(self, word: str, letter_guessed: str) -> bool:

        if letter_guessed in word:

            return True

        else:

            return False


    def show_current_word(self, word: str, letter_guessed: str, previous_word: str):

        for i, letter in enumerate(word):

            if letter_guessed == letter:

                previous_word: str = previous_word[:i] + letter + previous_word[i + 1:]

        current_word: str = previous_word

        return current_word


    def get_lives(self, word: str, letter_guessed: str) -> int:

        lives: int = self.lives

        if not self.check_if_letter_in_word(word, letter_guessed):

            lives -= 1

        return lives


    def play(self, word: str, letter_guessed: str):

        pass


