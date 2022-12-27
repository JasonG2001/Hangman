class Hangman:

    def __init__(self) -> None:

        self.lives = 6


    def ask_for_word(self):

        word: str = input("Enter your word: ")
        hidden_word: str =  len(word) * "_"
        return hidden_word


    def play(self):

        pass


