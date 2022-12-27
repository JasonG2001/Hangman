class Hangman:

    def __init__(self) -> None:

        self.lives = 6


    def ask_for_word(self) -> None: # O(1)

        word: str = input("Enter your word: ") # O(1)
        hidden_word: str =  len(word) * "_" # O(1)
        print(hidden_word)
        return self.play(hidden_word, word)


    def play(self, current_word: str, word: str):

        if current_word == word:
            return "You win"

        letter_guessed: str = input("Guess a letter: ")

        i: int
        letter: str
        for i, letter in enumerate(word):
            if letter == letter_guessed:
                current_word: str = current_word[:i] + letter + current_word[i+1:]

        print(current_word)

        return self.play(current_word, word)