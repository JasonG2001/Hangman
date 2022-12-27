class Hangman:

    def __init__(self, total_lives: int) -> None:

        self.lives: int = total_lives


    def ask_for_word(self) -> None: # O(1)

        word: str = input("Enter your word: ") # O(1)
        hidden_word: str =  len(word) * "_" # O(1)
        print(hidden_word)
        return self.play(hidden_word, word)


    def play(self, current_word: str, word: str, chances: int=0):

        if current_word == word:
            return "You win"

        if chances == self.lives:
            return "You lose"

        letter_guessed: str = input("Guess a letter: ")

        if letter_guessed in word:
            i: int
            letter: str
            for i, letter in enumerate(word):
                if letter == letter_guessed:
                    current_word: str = current_word[:i] + letter + current_word[i+1:]
        else:
            chances += 1

        print(current_word)
        print(f"You have {self.lives - chances} lives left")

        return self.play(current_word, word, chances)