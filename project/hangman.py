class Hangman:

    def __init__(self):

        pass


    def get_length_of_word(self, word: str):

        return len(word)


    def ask_for_word(self, word: str):

        return word


    def ask_for_letter(self, letter: str):

        return letter


    def check_if_letter_in_word(self, word: str, letter: str) -> bool:

        if letter in word:

            return True

        else:

            return False

    def play(self, word: str, letter: str):

        pass


